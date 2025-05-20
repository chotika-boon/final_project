import streamlit as st
import pandas as pd

CSV_FILE = "user_data.csv"
PROMO_FILE = "mockup - Sheet1 (2).csv"

def render_cards(title, card_data):
    st.markdown(f"### {title}")

    cards_html = ""
    for _, row in card_data.iterrows():
        cards_html += f"""
        <div class="promo-card">
            <img class="card-image" src="{row['picture']}" />
            <div class="store-name">{row['Card_name']}</div>
            <div class="benefit">💳 {row['ประโยชน์']}</div>
            <div class="type">👥 เหมาะกับ: {row['เหมาะ']}</div>
            <div class="min">📌 ขั้นต่ำ: {row['ขั้นต่ำ']}</div>
            <div class="date">📅 {row['Date']}</div>
        </div>
        """

    st.markdown(f"""
    <style>
    .card-row {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-top: 10px;
    }}
    .promo-card {{
        background: white;
        border-radius: 14px;
        padding: 14px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        font-family: 'Noto Sans Thai', sans-serif;
    }}
    .promo-card:hover {{
        transform: translateY(-6px);
    }}
    .card-image {{
        width: 100%;
        height: 140px;
        object-fit: contain;
        margin-bottom: 10px;
        border-radius: 12px;
        background-color: #f9f9f9;
        padding: 6px;
    }}
    .store-name {{
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 6px;
    }}
    .benefit, .type, .min, .date {{
        font-size: 13px;
        margin-bottom: 4px;
    }}
    </style>

    <div class="card-row">
        {cards_html}
    </div>
    """, unsafe_allow_html=True)


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

    try:
        df = pd.read_csv(PROMO_FILE)
        filtered = df[df["Store"].str.contains(r["name"], case=False, na=False)]
        if not filtered.empty:
            sorted_df = filtered.sort_values(by="score", ascending=False).head(4)
            render_cards("🎁 โปรโมชั่นที่ร่วมรายการ", sorted_df)
        else:
            st.info("ไม่มีโปรโมชั่นสำหรับร้านนี้")
    except Exception as e:
        st.error(f"โหลดโปรโมชั่นล้มเหลว: {e}")

    if st.button("🔙 กลับหน้าหลัก"):
        st.session_state.page = "home"
        st.rerun()
