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

    html, body, h1, h2, h3, h4, h5, h6, p, div, span, [class*="st-"], [class*="css"] {{
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
    display: flex;
    align-items: center;
    text-align: center;
    width: 20rem;
    margin: 2rem auto;
    color: #888;
}}

    .divider::before,
    .divider::after {{
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
    .custom-login-btn {{
    width: 20rem;
    background-color: #0084ff;
    color: white;
    font-weight: bold;
    font-size: 16px;
    padding: 10px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    display: block;
    margin: 1rem auto;
    transition: background 0.2s ease;
}}
    .custom-login-btn:hover {{
    background-color: #0070dd;
}}
    .signup-link {{
    width: 20rem;
    margin: 0 auto;
    text-align: right;
    font-size: 14px;
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
def show_login():
    with st.container():
        st.markdown("<h3 style='text-align:center;'>เข้าสู่ระบบ</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        email = st.text_input(" ", placeholder="เบอร์โทร/อีเมล", key="email_input", label_visibility="collapsed")

# Password input
    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        password = st.text_input(" ", placeholder="รหัสผ่าน", type="password", key="password_input", label_visibility="collapsed")


# ปุ่ม HTML ตรงกลาง
    st.markdown("""
    <button class="custom-login-btn" onclick="document.querySelector('[data-testid=login-btn]').click()">ตกลง</button>
""", unsafe_allow_html=True)    

    
    st.markdown("""
    <div class="signup-link">
        <a href="/?page=register" target="_self">ยังไม่มีบัญชี? <strong>สมัครสมาชิก</strong></a>
    </div>
""", unsafe_allow_html=True)
    if st.button("ยังไม่มีบัญชี? สมัครสมาชิก"):
        st.session_state.page = "register"
        st.experimental_rerun()  # 🔁 บังคับ Streamlit reload เพื่อให้ routing ทำงาน

    st.markdown('<div class="divider">หรือ</div>', unsafe_allow_html=True)

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
