import streamlit as st
import pandas as pd
import os
from openai import OpenAI

CSV_FILE = "user_data.csv"
PROMO_FILE = "CoolKid_promotion_creditcard - Sheet2.csv"

def show_detail():
    r = st.session_state.get("restaurant_detail")
    if not r:
        st.warning("ไม่พบข้อมูลร้านที่เลือก")
        return

    st.markdown("""
        <style>
        .detail-header {
            display: flex;
            gap: 20px;
            align-items: flex-start;
        }
        .detail-image {
            flex: 1;
        }
        .detail-info {
            flex: 2;
        }
        .badge {
            background-color: #e3e3e3;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 13px;
            margin-right: 6px;
            display: inline-block;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<div class='detail-header'>", unsafe_allow_html=True)
    st.image(r["image_url"], width=300)
    st.markdown("<div class='detail-info'>", unsafe_allow_html=True)
    st.title(r["name"])
    st.markdown(f"<div class='badge'>{r['category']}</div>", unsafe_allow_html=True)
    st.markdown(f"<p>⭐ <b>{r['rating']}</b> ({r['reviews']} รีวิว)</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{r.get('description', 'ไม่มีรายละเอียดเพิ่มเติม')}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()
    st.subheader("👤 ข้อมูลผู้ใช้ที่เข้าสู่ระบบ")
    user_cards = []
    if st.session_state.get("username"):
        st.markdown(f"**ชื่อผู้ใช้:** {st.session_state.username}")
        st.markdown(f"**อีเมล:** {st.session_state.get('logged_in_email', '-')}")
    else:
        st.warning("คุณยังไม่ได้เข้าสู่ระบบ")

    try:
        df = pd.read_csv(CSV_FILE)
        current_user = df[df['email'] == st.session_state.get("logged_in_email")]
        if not current_user.empty:
            user_row = current_user.iloc[-1]
            st.markdown(f"**จำนวนบัตรเครดิตที่สมัคร:** {user_row['card_count']}")
            user_cards = current_user['credit_name'].unique().tolist()
        else:
            st.info("ไม่พบข้อมูลผู้ใช้นี้ในระบบ")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการโหลดข้อมูลผู้ใช้: {e}")

    st.divider()
    st.subheader("🎁 โปรโมชั่นจากบัตรเครดิตที่ร่วมรายการ")

    try:
        promo_df = pd.read_csv(PROMO_FILE)
        filtered = promo_df[promo_df["Store"].str.contains(r["name"], case=False, na=False)]

        if not filtered.empty:
            user_card_match = filtered[filtered['Card_name'].isin(user_cards)]
            other_card = filtered[~filtered['Card_name'].isin(user_cards)]

            st.markdown("### ✅ บัตรที่คุณมี")
            st.dataframe(user_card_match if not user_card_match.empty else pd.DataFrame([{"ข้อความ": "ไม่มีบัตรที่คุณถือร่วมรายการ"}]))

            st.markdown("### 💳 บัตรอื่น ๆ ที่มีโปรโมชั่น")
            st.dataframe(other_card if not other_card.empty else pd.DataFrame([{"ข้อความ": "ไม่มีบัตรอื่นร่วมรายการ"}]))

            st.divider()
            st.subheader("🤖 คำแนะนำจาก AI")

            prompt = f"""
คุณคือผู้ช่วยด้านการเงินและโปรโมชั่นบัตรเครดิต

ร้าน: {r['name']}
ข้อมูลโปรโมชั่นทั้งหมด:
{filtered[['Card_name', 'Benefit_detail']].to_csv(index=False)}
อันนี้ต้องถูก filter ตามร้านที่เลือกเท่านั้น
โดยมีคอลัมน์สำคัญ:
- Card_name: ชื่อบัตร
- Benefit_detail: สิทธิประโยชน์ เช่น ส่วนลด หรือของแถม

ผู้ใช้มีบัตรดังต่อไปนี้:
{', '.join(user_cards)}

กรุณาช่วย:
1.  **เรียงลำดับบัตรจากแต่ละกลุ่ม** โดยพิจารณาจาก:
   - จำนวนเงินที่ต้องจ่ายน้อยที่สุด (amount)
   - ความง่ายในการใช้ (เงื่อนไขไม่ซับซ้อน)
   - มูลค่า benefit ที่ได้รับจริง (เช่น ลด %, ของแถม, เงินคืน)
    **จัดกลุ่มบัตร** เป็น:
   - ✅ บัตรที่ผู้ใช้มี
   - 💳 บัตรที่ผู้ใช้ไม่มี
2. ในรายละเอียดแต่ละบัตรให้ระบุให้หน่อย  
   - กินคนเดียว
   - กินเป็นกลุ่ม
   - ใช้เมื่อจ่ายเกินราคาเท่าไหร่
   - คุ้มยังไง
3. **สรุปแบบตาราง** พร้อมชื่อบัตร, benefit และคำแนะนำสั้น ๆ เช่น “แนะนำ”, “คุ้มเมื่อจ่ายเยอะ”, “เหมาะสำหรับกลุ่ม”, เป็นต้น

ข้อมูลโปรโมชั่นทั้งหมด:
{filtered[['Card_name', 'Benefit_detail']].to_csv(index=False)}
            """


            try:
                openai_api_key = st.secrets["OPENAI_API_KEY"]
                client = OpenAI(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "คุณเป็นผู้ช่วยด้านการเงินและการตลาด"},
                        {"role": "user", "content": prompt}
                    ]
                )
                st.markdown(response.choices[0].message.content)
            except Exception as ai_error:
                st.info(f"❗️ยังไม่ได้ตั้งค่า OPENAI_API_KEY หรือเชื่อมต่อ AI ไม่สำเร็จ: {ai_error}")
        else:
            st.info("ไม่มีโปรโมชั่นสำหรับร้านนี้ในขณะนี้")
    except Exception as e:
        st.error(f"ไม่สามารถโหลดไฟล์โปรโมชั่นได้: {e}")

    if st.button("🔙 กลับไปหน้าหลัก"):
        st.session_state.page = "home"
        st.rerun()
