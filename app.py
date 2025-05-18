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

# Inject font ผ่าน CSS
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

    html, body, [class*="st-"], [class*="css"], h1, h2, h3, h4, h5, h6, p, span, div, input, button, label {{
        font-family: 'Noto Sans Thai', sans-serif !important;
    }}

    /* Optional: Set fallback color */
    h2, h1, h3, h4, h5, h6 {{
        color: #222;
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
    st.markdown("""
        <style>
        .center-wrapper {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-container {
            max-width: 400px;
            width: 100%;
            padding: 40px 30px;
            background: #f9f9f9;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        .login-button, .social-button {
            width: 100%;
            padding: 12px;
            font-size: 15px;
            border-radius: 999px;
            border: 1px solid #ccc;
            margin-top: 10px;
            background: white;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .login-button-primary {
            background-color: #0e3c2e;
            color: white;
            font-weight: bold;
            margin-top: 20px;
            border: none;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="center-wrapper"><div class="login-container">', unsafe_allow_html=True)

    st.image("คู่คิด-removebg-preview.png", width=80)
    st.markdown("""
        <h2 style="font-weight: 700;">Sign in</h2>
        <p>ยังไม่มีบัญชี? <a href="#" style="color:#0e3c2e;font-weight:bold;">สร้างบัญชี</a></p>
    """, unsafe_allow_html=True)

    email = st.text_input("E-mail", placeholder="example@gmail.com")
    password = st.text_input("Password", type="password", placeholder="@#*%")

    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("จำฉันไว้")
    with col2:
        st.markdown("<div style='text-align:right;'><a href='#'>ลืมรหัสผ่าน?</a></div>", unsafe_allow_html=True)

    st.markdown('<button class="login-button login-button-primary">เข้าสู่ระบบ</button>', unsafe_allow_html=True)
    st.markdown("<hr><p style='text-align:center;'>หรือ</p>", unsafe_allow_html=True)

    # Google Login
    st.markdown("""
        <button class="social-button">
            <img src="https://static2.wongnai.com/static2/images/21qexS5.svg" width="20" />
            เข้าสู่ระบบด้วย Google
        </button>
    """, unsafe_allow_html=True)

    # Facebook Login
    st.markdown("""
        <button class="social-button">
            <img src="https://static2.wongnai.com/static2/images/3F9TqCg.svg" width="20" />
            เข้าสู่ระบบด้วย Facebook
        </button>
    """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)




def main():
    init_session_state()
    if not st.session_state.logged_in:
        modern_login_page()
    else:
        restaurant_app()  # ใช้ของเดิม

if __name__ == "__main__":
    main()
