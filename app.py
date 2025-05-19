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

# Components from engine
UserManager = engine.UserManager
BANKS = engine.BANKS
CARD_TYPES = engine.CARD_TYPES
LIFESTYLES = engine.LIFESTYLES
RestaurantSelector = engine.RestaurantSelector
CardRecommender = engine.CardRecommender

st.set_page_config(page_title="Login", page_icon="🔐", layout="wide")

# Inject Thai font
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

    .full-page-center {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}


    .login-input {{
        width: 20rem;
        margin: 0 auto 1rem auto;
    }}
    .input[type="text"], input[type="password"] {{
        width: 100% !important;
        border-radius: 8px;
        padding: 10px;
        font-size: 15px;
        box-sizing: border-box;
    }}
    
    .login-button {{
        width: 100%;
        background-color: #0084ff;
        color: white;
        font-weight: bold;
        font-size: 16px;
        padding: 10px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        margin-top: 1rem;
    }}

    .social-button {{
        width: 20rem;
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
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        transition: background 0.2s ease;
    }}
    .social-button:hover {{
        background: #f3f3f3;
    }}

    .divider {{
        width: 100%;
        text-align: center;
        border-bottom: 1px solid #ccc;
        line-height: 0.1em;
        margin: 1.5rem 0;
    }}

    .divider span {{
        background:#fff;
        padding:0 10px;
        font-size: 14px;
        color: #888;
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize backend managers
user_manager = UserManager()
restaurant_selector = RestaurantSelector()
card_recommender = CardRecommender()

# Initialize session state
def init_session_state():
    defaults = {
        "logged_in": False,
        "username": None,
        "show_register": False,
        "selected_restaurant": None,
        "search_query": ""
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# UI: Modern Login Page
def modern_login_page():
    with st.container():
        st.markdown("<h3 style='text-align:center;'>เข้าสู่ระบบ</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        email = st.text_input(" ", placeholder="เบอร์โทร/อีเมล", key="email_input", label_visibility="collapsed")

# Password input
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        password = st.text_input(" ", placeholder="รหัสผ่าน", type="password", key="password_input", label_visibility="collapsed")


        if st.button("ถัดไป", key="login_btn"):
            st.session_state.logged_in = True

        st.markdown("""
            <div style="text-align:right; font-size: 14px; width: 100%; margin-top: 0.5rem;">
                <a href="#">ยังไม่มีบัญชี? <strong>สมัครสมาชิก</strong></a>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="divider"><span>หรือ</span></div>', unsafe_allow_html=True)

        # Social buttons (HTML only for now)
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


# Dummy app after login
def restaurant_app():
    st.success("🎉 เข้าสู่ระบบเรียบร้อยแล้ว!")
    st.write("นี่คือหน้าหลังล็อกอิน (restaurant_app)")

# Main
def main():
    init_session_state()
    if not st.session_state.logged_in:
        modern_login_page()
    else:
        restaurant_app()

if __name__ == "__main__":
    main()
