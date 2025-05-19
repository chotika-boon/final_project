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

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered", initial_sidebar_state="collapsed")

# Inject font
with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
    font_data = f.read()
    base64_font = base64.b64encode(font_data).decode()

st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'Noto Sans Thai';
        src: url(data:font/ttf;base64,{base64_font}) format('truetype');
        font-weight: 300 600;
    }}

    html, body, [class*="st-"], [class*="css"] {{
        font-family: 'Noto Sans Thai', sans-serif !important;
        height: 100vh;
        background: linear-gradient(to right, #ff5858, #f09819);
        margin: 0;
        padding: 0;
    }}

    .center-wrapper {{
        display: flex;
        justify-content: center;
        align-items: flex-start;
        min-height: 100vh;
        padding-top: 5vh;
    }}

    .login-container {{
        width: 100%;
        max-width: 360px;
        background: white;
        padding: 2rem 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        text-align: center;
    }}

    .login-button-primary {{
        background-color: #0084ff;
        color: white;
        font-weight: bold;
        font-size: 15px;
        padding: 8px 20px;
        border: none;
        border-radius: 6px;
        margin-top: 1rem;
        cursor: pointer;
    }}

    .social-button {{
        width: 100%;
        max-width: 280px;
        padding: 10px;
        border-radius: 6px;
        border: 1px solid #ccc;
        background: white;
        font-size: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin: 8px auto;
    }}

    .divider {{
        display: flex;
        align-items: center;
        text-align: center;
        margin: 2rem 0 1.5rem;
    }}
    .divider::before, .divider::after {{
        content: '';
        flex: 1;
        border-bottom: 1px solid #ccc;
    }}
    .divider:not(:empty)::before {{
        margin-right: .75em;
    }}
    .divider:not(:empty)::after {{
        margin-left: .75em;
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
    st.markdown('<div class="center-wrapper"><div class="login-container">', unsafe_allow_html=True)

    st.markdown("""
        <h2 style="font-weight: 700; margin-bottom: 1.25rem;">เข้าสู่ระบบ</h2>
    """, unsafe_allow_html=True)

    email = st.text_input("เบอร์โทร/อีเมล")
    password = st.text_input("รหัสผ่าน", type="password")

    if st.button("ถัดไป", key="login_button"):
        st.session_state.logged_in = True

    st.markdown("""
        <div style="text-align:right; margin-top: 0.5rem;">
            <a href="#" style="font-size: 14px;">ยังไม่มีบัญชี? <strong>สมัครสมาชิก</strong></a>
        </div>
        <div class="divider">หรือ</div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="display:flex; justify-content:center; flex-direction: column; align-items:center;">
            <button class="social-button">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="20" />
                เข้าสู่ระบบด้วย Facebook
            </button>
            <button class="social-button">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111396.png" width="20" />
                เข้าสู่ระบบด้วย LINE
            </button>
            <button class="social-button">
                <img src="https://cdn-icons-png.flaticon.com/512/281/281764.png" width="20" />
                เข้าสู่ระบบด้วย Google
            </button>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

def main():
    init_session_state()
    if not st.session_state.logged_in:
        modern_login_page()
    else:
        st.write("You're logged in.")

if __name__ == "__main__":
    main()
