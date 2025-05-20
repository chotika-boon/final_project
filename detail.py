import streamlit as st
import pandas as pd
import os
from openai import OpenAI

CSV_FILE = "user_data.csv"
PROMO_FILE = "CoolKid_promotion_creditcard - Sheet2.csv"

openai_api_key = os.getenv("OPENAI_API_KEY")

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
            เรามีข้อมูลโปรโมชั่นจากร้าน {r['name']} ที่รองรับบัตรเครดิตหลายประเภท ข้อมูลประกอบด้วยบัตรที่คุณมี และบัตรอื่น ๆ:

            - จงเรียงลำดับบัตรที่คุ้มค่าที่สุดจากทั้ง 2 กลุ่ม (ที่คุณมี และที่คุณไม่มี)
            - พิจารณาจาก: จำนวนเงินที่ต้องจ่ายน้อยที่สุด (amount), ความง่ายในการใช้, ความคุ้มค่าที่ได้รับจริง
            - ช่วยระบุว่าโปรโมชั่นใดเหมาะกับ:
              - กินคนเดียว
              - กินเป็นกลุ่ม
              - ใช้เมื่อใช้จ่ายเกินราคาเท่าไหร่
            - ช่วยสรุปรายละเอียดของแต่ละบัตรสั้น ๆ

            นี่คือตารางข้อมูลโปรโมชั่น:

            {filtered.to_markdown(index=False)}
            """

            if openai_api_key:
                client = OpenAI(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "คุณเป็นผู้ช่วยด้านการเงินและการตลาด"},
                        {"role": "user", "content": prompt}
                    ]
                )
                st.markdown(response.choices[0].message.content)
            else:
                st.info("❗️ยังไม่ได้ตั้งค่า OPENAI_API_KEY จึงไม่สามารถเชื่อมต่อ AI ได้")
        else:
            st.info("ไม่มีโปรโมชั่นสำหรับร้านนี้ในขณะนี้")
    except Exception as e:
        st.error(f"ไม่สามารถโหลดไฟล์โปรโมชั่นได้: {e}")

    if st.button("🔙 กลับไปหน้าหลัก"):
        st.session_state.page = "home"
        st.rerun()
