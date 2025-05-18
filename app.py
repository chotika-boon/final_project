import streamlit as st
import base64
import os

# Load and embed custom font
with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
    font_data = f.read()
    base64_font = base64.b64encode(font_data).decode()

st.set_page_config(layout="wide")

# Apply custom font and center styling
st.markdown(f"""
    <style>
    @font-face {{
        font-family: 'Noto Sans Thai';
        src: url(data:font/ttf;base64,{base64_font}) format('truetype');
    }}

    html, body, [class*="st-"], [class*="css"] {{
        font-family: 'Noto Sans Thai', sans-serif !important;
    }}

    .login-container {{
        max-width: 400px;
        margin: 0 auto;
        padding: 60px 30px;
        background-color: #f9f9f9;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}

    .login-button, .social-button {{
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
    }}

    .login-button-primary {{
        background-color: #0e3c2e;
        color: white;
        font-weight: bold;
        margin-top: 20px;
        border: none;
    }}

    .center-wrapper {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}
    </style>
""", unsafe_allow_html=True)

# ✅ Center content
st.markdown('<div class="center-wrapper"><div class="login-container">', unsafe_allow_html=True)

# ✅ Logo
st.image("คู่คิด-removebg-preview.png", width=80)

# ✅ Header
st.markdown("""
<h2 style="font-weight:700;">Sign in</h2>
<p style="margin-bottom:25px;">ยังไม่มีบัญชี? <a href="#" style="font-weight:bold;color:#0e3c2e;">สร้างบัญชี</a></p>
""", unsafe_allow_html=True)

# ✅ Inputs
email = st.text_input("E-mail", placeholder="example@gmail.com")
password = st.text_input("Password", type="password", placeholder="@#*%")

col1, col2 = st.columns([1, 1])
with col1:
    st.checkbox("จำฉันไว้")
with col2:
    st.markdown("<div style='text-align:right;'><a href='#'>ลืมรหัสผ่าน?</a></div>", unsafe_allow_html=True)

# ✅ Sign-in Button
st.markdown('<button class="login-button login-button-primary">เข้าสู่ระบบ</button>', unsafe_allow_html=True)

# ✅ Divider
st.markdown("<hr><p style='text-align:center;'>หรือ</p>", unsafe_allow_html=True)

# ✅ Google Login
st.markdown("""
<button class="social-button">
    <img src="https://static2.wongnai.com/static2/images/21qexS5.svg" width="20" />
    เข้าสู่ระบบด้วย Google
</button>
""", unsafe_allow_html=True)

# ✅ Facebook Login
st.markdown("""
<button class="social-button">
    <img src="https://static2.wongnai.com/static2/images/3F9TqCg.svg" width="20" />
    เข้าสู่ระบบด้วย Facebook
</button>
""", unsafe_allow_html=True)

# ✅ End center container
st.markdown("</div></div>", unsafe_allow_html=True)
