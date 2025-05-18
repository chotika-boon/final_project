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

st.set_page_config(page_title="Login", page_icon="🔐", layout="wide")

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
    }}

    .center-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        background: #fff;
    }}

    .login-container {{
        width: 100%;
        max-width: 400px;
        background: white;
        padding: 2.5rem 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        text-align: center;
    }}

    .login-button-primary {{
        background-color: #0084ff;
        color: white;
        font-weight: bold;
        font-size: 16px;
        padding: 10px;
        border: none;
        border-radius: 8px;
        width: 100%;
        cursor: pointer;
    }}

    .social-button {{
        width: 100%;
        padding: 10px;
        border-radius: 6px;
        border: 1px solid #ccc;
        background: white;
        font-size: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-top: 10px;
    }}

    .divider {{
        display: flex;
        align-items: center;
        text-align: center;
        margin: 20px 0;
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
        <h2 style="font-weight: 700; margin-bottom: 1rem;">เข้าสู่ระบบ</h2>
    """, unsafe_allow_html=True)

    email = st.text_input("เบอร์โทร/อีเมล")
    if st.button("ถัดไป", use_container_width=True):
        st.session_state.logged_in = True

    st.markdown("""
        <div style="text-align:right; margin-top: 0.5rem;">
            <a href="#" style="font-size: 14px;">สมัครสมาชิก</a>
        </div>
        <div class="divider">หรือ</div>
    """, unsafe_allow_html=True)

    # Social buttons
    st.markdown("""
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
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

def main():
    init_session_state()
    if not st.session_state.logged_in:
        modern_login_page()
    else:
        restaurant_app()  # Use original function for logged-in experience

if __name__ == "__main__":
    main()
