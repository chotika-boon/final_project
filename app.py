import streamlit as st

# ตั้งค่าให้เป็น layout กว้าง
st.set_page_config(layout="wide")

# นำเข้า font Noto Sans Thai
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif;
    }

    .login-container {
        display: flex;
        height: 100vh;
    }

    .left-panel {
        width: 50%;
        padding: 80px;
        background-color: #f8fafa;
    }

    .right-panel {
        width: 50%;
        background-color: #123d2d;
        color: white;
        padding: 80px;
    }

    .signin-button {
        background-color: #1d3c2e;
        color: white;
        padding: 10px 0;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
        margin-top: 20px;
    }

    .social-button {
        padding: 10px 0;
        border-radius: 12px;
        border: 1px solid #ddd;
        text-align: center;
        margin-top: 10px;
    }

    .feature-box {
        background-color: white;
        color: #123d2d;
        padding: 20px;
        border-radius: 12px;
        max-width: 400px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    .earnings-box {
        background-color: #f8fafa;
        color: #123d2d;
        border-radius: 12px;
        padding: 10px;
        margin-top: 10px;
        display: inline-block;
    }

    </style>
""", unsafe_allow_html=True)

# Layout ด้วย HTML/CSS แทน
st.markdown("""
<div class="login-container">
    <div class="left-panel">
        <h1>Sign in</h1>
        <p>Don't have an account? <a href="#">Create now</a></p>

        <label for="email">E-mail</label>
        <input type="text" id="email" placeholder="example@gmail.com" style="width:100%;padding:10px;border-radius:10px;border:1px solid #ccc;margin-bottom:15px;" />

        <label for="password">Password</label>
        <input type="password" id="password" placeholder="@#*%" style="width:100%;padding:10px;border-radius:10px;border:1px solid #ccc;margin-bottom:15px;" />

        <div style="display:flex;justify-content:space-between;align-items:center;">
            <label><input type="checkbox" /> Remember me</label>
            <a href="#">Forgot Password?</a>
        </div>

        <button class="signin-button">Sign in</button>

        <hr style="margin: 20px 0;" />
        <div class="social-button">🔵 Continue with Google</div>
        <div class="social-button">🟦 Continue with Facebook</div>
    </div>

    <div class="right-panel">
        <div class="feature-box">
            <h3>Reach financial goals faster</h3>
            <p>Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.</p>
            <button style="margin-top:10px;padding:10px 20px;border:none;border-radius:10px;background-color:#1d3c2e;color:white;">Learn more</button>
            <div class="earnings-box">
                📈 Earnings: <strong>$350.40</strong>
            </div>
        </div>

        <div style="margin-top: 60px;">
            <h2>Introducing new features</h2>
            <p>Analyzing previous trends ensures that businesses always make the right decision. And as the scale of the decision and its impact magnifies...</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
