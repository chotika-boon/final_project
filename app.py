import streamlit as st
st.set_page_config(page_title="Final Project", page_icon="🔐", layout="wide")

import base64
from login import show_login, init_session_state
from register import show_register
from home import show_home

# ✅ set page config ต้องเป็นบรรทัดแรก
# ✅ Load Thai font & inject CSS
with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
    font_data = f.read()
    base64_font = base64.b64encode(font_data).decode()

st.markdown(f"""
<style>
@font-face {{
    font-family: 'Noto Sans Thai';
    src: url(data:font/ttf;base64,{base64_font}) format('truetype');
}}
html, body, [class*="st-"] {{
    font-family: 'Noto Sans Thai', sans-serif !important;
}}
</style>
""", unsafe_allow_html=True)

def inject_global_css():
    with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
        font_data = f.read()
        base64_font = base64.b64encode(font_data).decode()

    st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'Noto Sans Thai';
        src: url(data:font/ttf;base64,{base64_font}) format('truetype');
    }}
    html, body, [class*="st-"] {{
        font-family: 'Noto Sans Thai', sans-serif !important;
    }}

    .custom-login-btn {{
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
    .custom-login-btn:hover {{
        background-color: #0070dd;
    }}

    .signup-link {{
        width: 100%;
        text-align: right;
        font-size: 14px;
        margin-top: 10px;
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
        margin: 8px auto;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        transition: background 0.2s ease;
    }}
    .social-button:hover {{
        background: #f3f3f3;
    }}
    </style>
    """, unsafe_allow_html=True)


# ✅ Init session
inject_global_css()
init_session_state()

from detail import show_detail  # เพิ่มไฟล์ detail.py แยกหน้า detail

# ...

# ✅ Routing
if st.session_state.get("page") == "login":
    show_login()
elif st.session_state.get("page") == "register":
    show_register()
elif st.session_state.get("page") == "detail":
    show_detail()
elif st.session_state.get("logged_in"):
    show_home()
else:
    st.session_state.page = "login"
    st.rerun()
