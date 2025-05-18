import streamlit as st
from PIL import Image

# Must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Solara - Sign In")

# CSS for layout
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
        margin-bottom: 60px;
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
    .stButton > button {
        background-color: #153f2e;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 20px;
        width: 100%;
        border: none;
    }
    .learn-more button {
        background-color: #1f5a43 !important;
    }
    .divider {
        display: flex;
        align-items: center;
        text-align: center;
        margin: 25px 0;
    }
    .divider::before, .divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid #ddd;
    }
    .divider span {
        padding: 0 10px;
        color: #777;
        font-size: 12px;
    }
    .password-container {
        position: relative;
    }
    .password-eye {
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        cursor: pointer;
        color: #666;
    }
    .card-img {
        max-width: 180px;
        margin-top: -20px;
        position: absolute;
        right: 30px;
        top: 50%;
    }
    .earnings {
        position: absolute;
        bottom: 20px;
        right: 20px;
        text-align: right;
    }
    .earnings-label {
        font-size: 12px;
        color: #ccc;
    }
    .earnings-value {
        font-size: 24px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='container'>", unsafe_allow_html=True)

# Left Side
st.markdown("<div class='left'>", unsafe_allow_html=True)

# Logo
st.markdown("""
    <div class="logo">
        <svg width="140" height="40" viewBox="0 0 140 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M40 20C40 31.0457 31.0457 40 20 40C8.9543 40 0 31.0457 0 20C0 8.9543 8.9543 0 20 0C31.0457 0 40 8.9543 40 20Z" fill="#0D3B2E" fill-opacity="0.1"/>
            <path d="M24.5 15L20 10.5L15.5 15M24.5 25L20 29.5L15.5 25" stroke="#0D3B2E" stroke-width="2"/>
            <path d="M56.3906 29V11H67.8125V14.2969H60.2656V18.4062H67.1719V21.7031H60.2656V29H56.3906ZM70.3906 29V16.25H74.0156V29H70.3906ZM72.2031 14.6562C71.6406 14.6562 71.1562 14.4688 70.75 14.0938C70.3438 13.7188 70.1406 13.2656 70.1406 12.7344C70.1406 12.2031 70.3438 11.75 70.75 11.375C71.1562 11 71.6406 10.8125 72.2031 10.8125C72.7656 10.8125 73.25 11 73.6562 11.375C74.0625 11.75 74.2656 12.2031 74.2656 12.7344C74.2656 13.2656 74.0625 13.7188 73.6562 14.0938C73.25 14.4688 72.7656 14.6562 72.2031 14.6562ZM81.2031 16.25L81.3281 17.8125C82.1719 16.625 83.3281 16.0312 84.7969 16.0312C87.1094 16.0312 88.2969 17.375 88.3594 20.0625V29H84.7344V20.25C84.7344 19.5938 84.6094 19.125 84.3594 18.8438C84.1094 18.5625 83.6562 18.4219 83 18.4219C82.125 18.4219 81.4844 18.8281 81.0781 19.6406V29H77.4531V16.25H81.2031ZM94.5312 13.0312V16.25H96.7656V18.4219H94.5312V25.2188C94.5312 25.6562 94.6094 25.9688 94.7656 26.1562C94.9219 26.3438 95.2188 26.4375 95.6562 26.4375C95.9688 26.4375 96.25 26.4219 96.5 26.3906V28.6562C95.7812 28.8438 95.0781 28.9375 94.3906 28.9375C91.9531 28.9375 90.7188 27.7188 90.6875 25.2812V18.4219H88.7969V16.25H90.6875V13.0312H94.5312ZM102.844 29.2188C100.781 29.2188 99.1406 28.5938 97.9219 27.3438C96.7031 26.0938 96.0938 24.4531 96.0938 22.4219V22.0625C96.0938 20.6875 96.3438 19.4688 96.8438 18.4062C97.3438 17.3438 98.0625 16.5156 99 15.9219C99.9375 15.3281 101.031 15.0312 102.281 15.0312C104.156 15.0312 105.625 15.6406 106.688 16.8594C107.75 18.0781 108.281 19.7656 108.281 21.9219V23.1719H99.7656C99.8594 24.0469 100.188 24.75 100.75 25.2812C101.312 25.8125 102.031 26.0781 102.906 26.0781C104.219 26.0781 105.25 25.6094 106 24.6719L108 26.7812C107.438 27.5625 106.688 28.1719 105.75 28.6094C104.812 29.0156 103.844 29.2188 102.844 29.2188ZM102.281 18.1875C101.562 18.1875 100.969 18.4219 100.5 18.8906C100.031 19.3594 99.75 20.0312 99.6562 20.9062H104.719V20.6562C104.688 19.8438 104.469 19.2344 104.062 18.8281C103.656 18.4219 103.062 18.1875 102.281 18.1875Z" fill="#0D3B2E"/>
        </svg>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='form-box'>", unsafe_allow_html=True)
st.markdown("<div class='form-title'>Sign in</div>", unsafe_allow_html=True)
st.markdown("<div class='form-subtitle'>Don't have an account? <a href='#'>Create now</a></div>", unsafe_allow_html=True)

email = st.text_input("E-mail", placeholder="example@gmail.com")

# Password field with eye icon
st.markdown("""
<div style="position: relative;">
    <label for="password">Password</label>
    <div class="password-container">
        <input type="password" id="password" name="password" placeholder="Enter your password" style="width: 100%; padding: 8px 30px 8px 12px; border: 1px solid #ddd; border-radius: 4px;">
        <div class="password-eye">👁️</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Create the password field in Streamlit (hidden but needed for functionality)
password = st.text_input("", type="password", label_visibility="collapsed")

col_remember, col_forgot = st.columns([1, 1])
with col_remember:
    st.checkbox("Remember me")
with col_forgot:
    st.markdown("<div style='text-align: right;'><a href='#' style='color: #153f2e; text-decoration: none;'>Forgot Password?</a></div>", unsafe_allow_html=True)

login = st.button("Sign in", use_container_width=True)

st.markdown("<div class='divider'><span>OR</span></div>", unsafe_allow_html=True)

st.markdown("""
<div class='social-btn'>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 48 48">
        <path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"></path>
        <path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"></path>
        <path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"></path>
        <path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"></path>
    </svg>
    Continue with Google
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='social-btn'>
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="#1877F2">
        <path d="M12 2.04C6.5 2.04 2 6.53 2 12.06C2 17.06 5.66 21.21 10.44 21.96V14.96H7.9V12.06H10.44V9.85C10.44 7.34 11.93 5.96 14.22 5.96C15.31 5.96 16.45 6.15 16.45 6.15V8.62H15.19C13.95 8.62 13.56 9.39 13.56 10.18V12.06H16.34L15.89 14.96H13.56V21.96C18.34 21.21 22 17.06 22 12.06C22 6.53 17.5 2.04 12 2.04Z" />
    </svg>
    Continue with Facebook
</div>
""", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# Right Side
st.markdown("<div class='right'>", unsafe_allow_html=True)
st.markdown("<div class='section' style='position: relative;'>", unsafe_allow_html=True)

st.markdown("<div class='highlight'>Reach financial goals faster</div>", unsafe_allow_html=True)
st.markdown("<div class='paragraph'>Use your Solara card around the world with no hidden fees. Hold, transfer and spend money.</div>", unsafe_allow_html=True)

# Credit card image
st.markdown("""
<div class="card-img">
    <svg width="160" height="100" viewBox="0 0 160 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect y="0" width="160" height="100" rx="10" fill="url(#paint0_linear)"/>
        <text x="20" y="30" fill="white" font-family="Arial" font-size="12">Solara</text>
        <text x="20" y="80" fill="white" font-family="Arial" font-size="14">7312 2199 0623 XXXX</text>
        <text x="20" y="95" fill="white" font-family="Arial" font-size="10">08/24</text>
        <defs>
            <linearGradient id="paint0_linear" x1="0" y1="0" x2="160" y2="100" gradientUnits="userSpaceOnUse">
                <stop stop-color="#1F5A43"/>
                <stop offset="1" stop-color="#0D3B2E"/>
            </linearGradient>
        </defs>
    </svg>
</div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="learn-more">', unsafe_allow_html=True)
    st.button("Learn more", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Earnings display
st.markdown("""
<div class="earnings">
    <div class="earnings-label">Earnings</div>
    <div class="earnings-value">$350.40</div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div style='margin-top: 40px; text-align: center;'>
    <h2 style='color: white; font-size: 28px; margin-bottom: 20px;'>Introducing new features</h2>
    <p style='color: #ccc; font-size: 14px; max-width: 400px; margin: 0 auto;'>
        Analyzing previous trends ensures that businesses always make the right decision. And as the scale of the decision and it's impact magnifies...
    </p>
    <div style='margin-top: 30px; display: flex; justify-content: center; gap: 20px;'>
        <button style='background: none; border: none; color: white; cursor: pointer;'>←</button>
        <div style='width: 20px; height: 20px; border-radius: 10px; background-color: #1F5A43;'></div>
        <button style='background: none; border: none; color: white; cursor: pointer;'>→</button>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Login check
if login:
    if email and password:
        st.success("Login Successful! ✅")
    else:
        st.error("Please enter both email and password ❌")
