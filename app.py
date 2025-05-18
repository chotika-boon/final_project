import streamlit as st
from PIL import Image
import importlib.util
import sys
import os
import uuid
import time
from google.cloud import bigquery
import base64

# Load engine.py dynamically
spec = importlib.util.spec_from_file_location("engine", os.path.join(os.path.dirname(__file__), "engine.py"))
engine = importlib.util.module_from_spec(spec)
sys.modules["engine"] = engine
spec.loader.exec_module(engine)

UserManager = engine.UserManager
BANKS = engine.BANKS
CARD_TYPES = engine.CARD_TYPES
LIFESTYLES = engine.LIFESTYLES
RestaurantSelector = engine.RestaurantSelector
CardRecommender = engine.CardRecommender

st.set_page_config(layout="wide")

# อ่านไฟล์ฟอนต์ TTF
with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
    font_data = f.read()
    base64_font = base64.b64encode(font_data).decode()

# Inject font ผ่าน CSS
st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'Noto Sans Thai';
        src: url(data:font/ttf;base64,{base64_font}) format('truetype');
        font-weight: 300 600;
    }}

    html, body, div, span, input, label, textarea, button, select, h1, h2, h3, h4, h5, h6, p, a, ul, li {{
        font-family: 'Noto Sans Thai', sans-serif !important;
    }}
    </style>
""", unsafe_allow_html=True)

user_manager = UserManager()
restaurant_selector = RestaurantSelector()
card_recommender = CardRecommender()

def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'show_register' not in st.session_state:
        st.session_state.show_register = False
    if "selected_restaurant" not in st.session_state:
        st.session_state["selected_restaurant"] = None
    if "search_query" not in st.session_state:
        st.session_state["search_query"] = ""

def modern_login_page():
    left, right = st.columns([0.4, 0.6])

    with left:
        st.image("คู่คิด-removebg-preview.png", width=80)
        st.markdown("""
        <h2 style="font-weight: 700;">Sign in</h2>
        <p>ยังไม่มีบัญชี? <a href="#" style="color:#0e3c2e;font-weight:bold;">สร้างบัญชี</a></p>
        """, unsafe_allow_html=True)

        email = st.text_input("E-mail", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password", placeholder="@#*%")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.checkbox("จำฉันไว้")
        with col2:
            st.markdown("<div style='text-align:right;'><a href='#'>ลืมรหัสผ่าน?</a></div>", unsafe_allow_html=True)

        st.button("เข้าสู่ระบบ", use_container_width=True)
        st.markdown("<hr><p style='text-align:center;'>หรือ</p>", unsafe_allow_html=True)
        st.button("🔵 เข้าสู่ระบบด้วย Google", use_container_width=True)
        st.button("🔵 เข้าสู่ระบบด้วย Facebook", use_container_width=True)

    with right:
        st.markdown("""
        <div style="background:#0e3c2e;padding:40px;border-radius:16px;color:white;">
            <h4>📌 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</h4>
            <p>ใช้บัตร Venus ของคุณทั่วโลก โดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้งานได้ทันที</p>
            <button style="padding: 10px 20px; background:white; color:#0e3c2e; border:none; border-radius:8px;">ดูเพิ่มเติม</button>
        </div>
        """, unsafe_allow_html=True)

def main():
    init_session_state()
    if not st.session_state.logged_in:
        modern_login_page()
    else:
        restaurant_app()  # ใช้ของเดิม

if __name__ == "__main__":
    main()
