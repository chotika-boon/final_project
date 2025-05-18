import streamlit as st
from PIL import Image
import os

# st.set_page_config must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Sign In")

# Custom CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }
        .container {
            display: flex;
            height: 100vh;
            overflow: hidden;
        }
        .left-side {
            background-color: #f7f9f8;
            flex: 1;
            padding: 4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .right-side {
            background-color: #0e3c2e;
            flex: 1;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }
        .title {
            font-size: 2.5rem;
            font-weight: 700;
        }
        .subtitle {
            color: #5f6d6d;
            font-size: 1rem;
        }
        .input-box {
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            width: 100%;
            margin-bottom: 16px;
        }
        .btn-main {
            background-color: #0e3c2e;
            color: white;
            width: 100%;
            padding: 12px;
            font-weight: bold;
            border-radius: 8px;
            margin-top: 10px;
        }
        .social-btn {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 8px;
            margin-top: 12px;
            background: white;
            color: #333;
            font-weight: 500;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Layout with 2 columns
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown("""
        <div class="left-side">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Logo_placeholder.svg/512px-Logo_placeholder.svg.png" width="100" />
            <div class="title">Sign in</div>
            <div class="subtitle">Don't have an account? <a href="#">Create now</a></div>
            <br>
    """, unsafe_allow_html=True)

    username = st.text_input("E-mail", placeholder="example@gmail.com")
    password = st.text_input("Password", placeholder="@#*%", type="password")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.checkbox("Remember me")
    with col2:
        st.markdown("<div style='text-align: right;'><a href='#'>Forgot Password?</a></div>", unsafe_allow_html=True)

    st.button("Sign in", use_container_width=True)

    st.markdown("<hr style='margin:20px 0;'>", unsafe_allow_html=True)

    st.markdown("<div class='social-btn'>🔵 Continue with Google</div>", unsafe_allow_html=True)
    st.markdown("<div class='social-btn'>🔵 Continue with Facebook</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.markdown("""
        <div class='right-side'>
            <div>
                <h3>Reach financial goals faster</h3>
                <p>Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.</p>
                <button style='padding: 10px 20px; background: white; color: #0e3c2e; border-radius: 8px; border: none;'>Learn more</button>
            </div>
        </div>
    """, unsafe_allow_html=True)
