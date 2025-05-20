import streamlit as st
import pandas as pd
import json
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
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
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

    # User Info
    st.subheader("👤 ข้อมูลผู้ใช้ที่เข้าสู่ระบบ")
    if st.session_state.get("username"):
        st.markdown(f"**ชื่อผู้ใช้:** {st.session_state.username}")
        st.markdown(f"**อีเมล:** {st.session_state.get('logged_in_email', '-')}")
    else:
        st.warning("คุณยังไม่ได้เข้าสู่ระบบ")

    user_cards = []
    try:
        df = pd.read_csv(CSV_FILE)
        current_user = df[df['email'] == st.session_state.get("logged_in_email")]
        if not current_user.empty:
            user_row = current_user.iloc[-1]
            st.markdown(f"**จำนวนบัตรเครดิตที่สมัคร:** {user_row['card_count']}")
            user_cards = user_row['cards'].split(",") if 'cards' in user_row else []
        else:
            st.info("ไม่พบข้อมูลผู้ใช้นี้ในระบบ")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการโหลดข้อมูลผู้ใช้: {e}")

    st.divider()

    # Promotions
    st.subheader("🎁 โปรโมชั่นจากบัตรเครดิตที่ร่วมรายการ")
    try:
        promo_df = pd.read_csv(PROMO_FILE)
        promo_df.rename(columns={promo_df.columns[5]: "Link"}, inplace=True)
        filtered = promo_df[promo_df["Store"].str.contains(r["name"], case=False, na=False)]

        if not filtered.empty:
            st.dataframe(filtered[["Card_name", "Benefit_detail", "Date", "Link"]])

            # AI Prompt
            prompt = f"""
คุณคือผู้ช่วยด้านการเงินและโปรโมชั่นบัตรเครดิต

ร้าน: {r['name']}
ผู้ใช้มีบัตร: {', '.join(user_cards)}

จากโปรโมชั่นด้านล่าง โปรดวิเคราะห์:
1. โปรโมชั่นไหนคุ้มค่าที่สุด
2. เหมาะกับใคร (กินคนเดียว / กลุ่ม)
3. ต้องจ่ายขั้นต่ำเท่าไหร่
4. ให้คำแนะนำแบบสั้น เช่น “คุ้มเมื่อจ่ายเกิน 500 บาท”, “เหมาะกับปิ้งย่าง”

ตอบกลับในรูปแบบ JSON เท่านั้น:
[
  {{
    "ร้าน": "Bar B Q Plaza",
    "บัตร": "KTC Platinum",
    "ประโยชน์": "ลด 80 บาท เมื่อใช้ 699 คะแนน",
    "ขั้นต่ำ": 699,
    "เหมาะกับ": "กลุ่ม",
    "แนะนำ": "คุ้มเมื่อจ่ายเยอะ"
  }}
]

โปรโมชั่น:
{filtered[['Store', 'Card_name', 'Benefit_detail']].to_csv(index=False)}
"""

            # Call OpenAI
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            with st.spinner("🤖 AI กำลังวิเคราะห์โปรโมชั่น..."):
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2
                )
                result = response.choices[0].message.content
                try:
                    parsed = json.loads(result)
                    st.markdown('<div class="card-grid">', unsafe_allow_html=True)
                    for item in parsed:
                        st.markdown(f"""
                        <div class="card">
                            <h4>{item['ร้าน']}</h4>
                            <p><strong>บัตร:</strong> {item['บัตร']}</p>
                            <p><strong>ประโยชน์:</strong> {item['ประโยชน์']}</p>
                            <p><strong>ขั้นต่ำ:</strong> {item['ขั้นต่ำ']} บาท</p>
                            <p><strong>เหมาะกับ:</strong> {item['เหมาะกับ']}</p>
                            <p><strong>คำแนะนำ:</strong> {item['แนะนำ']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                except:
                    st.warning("⚠️ ไม่สามารถแปลงผลลัพธ์เป็น JSON ได้ แสดงแบบข้อความแทน")
                    st.markdown(result)

        else:
            st.info("ไม่มีโปรโมชั่นสำหรับร้านนี้ในขณะนี้")
    except Exception as e:
        st.error(f"ไม่สามารถโหลดไฟล์โปรโมชั่นได้: {e}")

    if st.button("🔙 กลับไปหน้าหลัก"):
        st.session_state.page = "home"
        st.rerun()
