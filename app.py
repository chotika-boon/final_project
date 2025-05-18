import streamlit as st
from PIL import Image

# 🚀 Must be the first command
st.set_page_config(layout="wide")

# 🌟 CSS for layout
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        height: 100%;
        margin: 0;
        padding: 0;
        font-family: 'Segoe UI', sans-serif;
    }
    .container {
        display: flex;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
        background-color: #f5f7f6;
    }
    .left, .right {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        flex-direction: column;
    }
    .left {
        padding: 40px;
    }
    .right {
        background-color: #0d3b2e;
        color: white;
        padding: 60px;
    }
    .form-box {
        max-width: 400px;
        width: 100%;
    }
    .logo {
        width: 100px;
        margin-bottom: 20px;
    }
    .form-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .form-subtitle {
        font-size: 14px;
        color: #666;
        margin-bottom: 30px;
    }
    .form-subtitle a {
        color: #153f2e;
        text-decoration: none;
        font-weight: bold;
    }
    .login-button {
        width: 100%;
        padding: 12px;
        background-color: #153f2e;
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        font-weight: bold;
        margin-top: 12px;
    }
    .social-btn {
        width: 100%;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 12px;
        margin-top: 10px;
        text-align: center;
        font-size: 14px;
        background-color: white;
        display: flex;
        align-items: center;
        gap: 10px;
        justify-content: center;
    }
    .section {
        max-width: 400px;
        padding: 40px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.1);
    }
    .highlight {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .paragraph {
        font-size: 14px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='container'>", unsafe_allow_html=True)

# 🏠 Left Side
st.markdown("<div class='left'>", unsafe_allow_html=True)\nst.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Logo_placeholder.svg/512px-Logo_placeholder.svg.png", width=100)

st.markdown("<div class='form-box'>", unsafe_allow_html=True)

st.markdown("<div class='form-title'>Sign in</div>", unsafe_allow_html=True)

st.markdown("<div class='form-subtitle'>Don’t have an account? <a href='#'>Create now</a></div>", unsafe_allow_html=True)

username = st.text_input("E-mail", placeholder="example@gmail.com")
password = st.text_input("Password", type="password", placeholder="Enter your password")

col_remember, col_forgot = st.columns([1, 1])
with col_remember:
    st.checkbox("Remember me")
with col_forgot:
    st.markdown("<div style='text-align: right;'><a href='#'>Forgot Password?</a></div>", unsafe_allow_html=True)

login = st.button("Sign in", use_container_width=True)

st.markdown("""<hr style='margin: 25px 0;'>""", unsafe_allow_html=True)

st.markdown("<div class='social-btn'>🚀 Continue with Google</div>", unsafe_allow_html=True)
st.markdown("<div class='social-btn'>📲 Continue with Facebook</div>", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# 🌍 Right Side
st.markdown("<div class='right'>", unsafe_allow_html=True)
st.markdown("<div class='section'>", unsafe_allow_html=True)

st.markdown("<div class='highlight'>Reach financial goals faster</div>", unsafe_allow_html=True)
st.markdown("<div class='paragraph'>Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.</div>", unsafe_allow_html=True)
st.button("Learn more", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div style='margin-top: 40px; text-align: center;'>Introducing <strong>new features</strong><br><span style='font-size: 13px;'>Analyzing previous trends ensures that businesses always make the right decision.</span></div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 🚀 Fake Login Check
if login:
    if username == "admin" and password == "1234":
        st.success("Login Success! ✅")
    else:
        st.error("Login Failed ❌")
