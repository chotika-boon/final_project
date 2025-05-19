import streamlit as st
import base64
from login import show_login
from register import show_register

# Load logo
with open("logo.png", "rb") as img_file:
    logo_base64 = base64.b64encode(img_file.read()).decode()

# Load font
with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
    base64_font = base64.b64encode(f.read()).decode()

# Page config
st.set_page_config(page_title="Final Project", page_icon="🔐", layout="wide")

# Inject CSS + Logo Navbar
st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'Noto Sans Thai';
        src: url(data:font/ttf;base64,{base64_font}) format('truetype');
    }}
    html, body, h1, h2, h3, h4, h5, h6, div, span, [class*="st-"] {{
        font-family: 'Noto Sans Thai', sans-serif !important;
    }}
    .top-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 60px;
        background-color: #000;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 2rem;
        z-index: 999;
    }}
    .top-navbar img {{
        height: 38px;
    }}
    .top-navbar a {{
        color: white;
        text-decoration: none;
        margin-left: 1.5rem;
        font-weight: 500;
        font-size: 15px;
    }}
    .stApp {{ padding-top: 70px; }}
    </style>

    <div class="top-navbar">
        <img src="data:image/png;base64,{logo_base64}" alt="Logo">
        <div>
            <a href="/?page=login">เข้าสู่ระบบ</a>
            <a href="/?page=register">สมัครสมาชิก</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Routing
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["login"])[0]

if page == "login":
    show_login()
elif page == "register":
    show_register()
else:
    st.error("ไม่พบหน้า 😢")
