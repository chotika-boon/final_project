import streamlit as st
import base64
from login import show_login, init_session_state
from register import show_register

# ✅ set page config ต้องเป็นบรรทัดแรก
st.set_page_config(page_title="Final Project", page_icon="🔐", layout="wide")

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

# ✅ Init session
init_session_state()

# ✅ Routing based on session
if st.session_state.get("page") == "login":
    show_login()
elif st.session_state.get("page") == "register":
    show_register()
elif st.session_state.get("logged_in"):
    st.success("🎉 เข้าสู่ระบบเรียบร้อยแล้ว!")
    st.write("นี่คือหน้าหลังล็อกอิน (restaurant_app)")
else:
    st.session_state.page = "login"
    st.rerun()
