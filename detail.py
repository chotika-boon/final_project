import streamlit as st
import pandas as pd
import json
from openai import OpenAI

CSV_FILE = "user_data.csv"
PROMO_FILE = "CoolKid_promotion_creditcard - Sheet2.csv"

def render_cards_by_group(title, card_data):
    st.markdown(f"### {title}")
    st.markdown("""
    <style>
    .card-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 16px;
        margin-top: 10px;
    }
    .promo-card {
        background: white;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }
    .promo-card:hover {
        transform: translateY(-4px);
    }
    .badge {
        background-color: #f0f0f0;
        color: #333;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        display: inline-block;
        margin-bottom: 8px;
    }
    .store-name {
        font-weight: 700;
        font-size: 18px;
    }
    .benefit {
        margin: 8px 0;
    }
    .date {
        font-size: 13px;
        color: #777;
        margin-bottom: 10px;
    }
    .detail-link {
        font-weight: 600;
        color: #000;
    }
    </style>
    <div class="card-row">
    """, unsafe_allow_html=True)

    for card in card_data:
        st.markdown(f"""
        <div class="promo-card">
            <div class="store-name">{card['ร้าน']}</div>
            <div class="badge">{card.get('ประเภท', 'ไม่ระบุ')}</div>
            <div class="benefit">• {card['ประโยชน์']}</div>
            <div class="date">{card.get('ช่วงเวลา', 'ไม่ระบุวันที่')}</div>
            <div class="detail-link">อ่านรายละเอียดเพิ่มเติม ➝</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def show_detail():
    r = st.session_state.get("restaurant_detail")
    if not r:
        st.warning("ไม่พบข้อมูลร้านที่เลือก")
        return

    st.image(r["image_url"], width=300)
    st.title(r["name"])
    st.markdown(f"หมวดหมู่: {r['category']}")
    st.markdown(f"⭐ {r['rating']} ({r['reviews']} รีวิว)")
    st.markdown(r.get("description", "ไม่มีรายละเอียดเพิ่มเติม"))

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
            if 'cards' in user_row:
                user_cards = user_row['cards'].split(",")
    except Exception as e:
        st.error(f"โหลดข้อมูลผู้ใช้ล้มเหลว: {e}")
        return

    st.divider()
    st.subheader("🎁 โปรโมชั่นที่ร่วมรายการ")

    try:
        promo_df = pd.read_csv(PROMO_FILE)
        promo_df.rename(columns={promo_df.columns[5]: "Link"}, inplace=True)
        filtered = promo_df[promo_df["Store"].str.contains(r["name"], case=False, na=False)]

        if not filtered.empty:
            prompt = f'''
คุณคือผู้ช่วยด้านการเงินและโปรโมชั่นบัตรเครดิต

ร้าน: {r['name']}
ผู้ใช้มีบัตร: {', '.join(user_cards)}

จากโปรโมชั่นด้านล่าง โปรดวิเคราะห์:
1. โปรโมชั่นไหนคุ้มค่าที่สุด
2. เหมาะกับใคร (กินคนเดียว / กลุ่ม)
3. ต้องจ่ายขั้นต่ำเท่าไหร่
4. ให้คำแนะนำแบบสั้น เช่น “คุ้มเมื่อจ่ายเกิน 500 บาท”, “เหมาะกับปิ้งย่าง”
5. เพิ่ม field "กลุ่ม" เป็น ✅ ถ้าผู้ใช้มีบัตรนี้ และ 💳 ถ้าไม่มี

ตอบกลับ JSON เท่านั้น:
[
  {{
    "ร้าน": "Bar B Q Plaza",
    "บัตร": "KTC Platinum",
    "ประเภท": "ปิ้งย่าง",
    "ประโยชน์": "ลด 80 บาท เมื่อใช้ 699 คะแนน",
    "ขั้นต่ำ": 699,
    "เหมาะกับ": "กลุ่ม",
    "แนะนำ": "คุ้มเมื่อจ่ายเยอะ",
    "ช่วงเวลา": "1 มี.ค. 68 - 31 ส.ค. 68",
    "กลุ่ม": "✅"
  }}
]

โปรโมชั่น:
{filtered[['Store', 'Card_name', 'Benefit_detail', 'Date']].to_csv(index=False)}
'''

            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            with st.spinner("🔍 กำลังวิเคราะห์ด้วย AI..."):
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2
                )
                result = response.choices[0].message.content
                try:
                    parsed = json.loads(result)
                    user_has = [p for p in parsed if p["กลุ่ม"] == "✅"]
                    user_not_have = [p for p in parsed if p["กลุ่ม"] == "💳"]

                    render_cards_by_group("✅ บัตรที่คุณมี", user_has)
                    render_cards_by_group("💳 บัตรที่คุณยังไม่มี", user_not_have)

                except Exception as e:
                    st.error("⚠️ JSON ไม่ถูกต้อง")
                    st.code(result)
        else:
            st.info("ไม่มีโปรโมชั่นสำหรับร้านนี้")
    except Exception as e:
        st.error(f"โหลดโปรโมชั่นล้มเหลว: {e}")

    if st.button("🔙 กลับหน้าหลัก"):
        st.session_state.page = "home"
        st.rerun()
