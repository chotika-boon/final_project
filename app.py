import streamlit as st

# Set wide layout as first Streamlit command
st.set_page_config(layout="wide", page_title="Sign In")

# Inject custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }

    .main-container {
        display: flex;
        flex-direction: row;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
    }

    .left-section {
        width: 50%;
        padding: 4rem;
        background-color: #f7f9f8;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .right-section {
        width: 50%;
        padding: 3rem;
        background-color: #0e3c2e;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .form-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .form-subtitle {
        font-size: 14px;
        color: #777;
        margin-bottom: 2rem;
    }

    .input-box {
        padding: 12px;
        margin-bottom: 16px;
        border-radius: 8px;
        border: 1px solid #ddd;
        width: 100%;
    }

    .checkbox-group {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
        font-size: 14px;
    }

    .login-btn {
        padding: 12px;
        background-color: #0e3c2e;
        color: white;
        width: 100%;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        margin-bottom: 1rem;
    }

    .social-btn {
        background: white;
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 12px;
        margin-bottom: 0.75rem;
        font-weight: 500;
        text-align: center;
        cursor: pointer;
    }

    .right-card {
        background-color: white;
        color: #0e3c2e;
        border-radius: 12px;
        padding: 2rem;
        max-width: 400px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }

    .right-card h4 {
        margin-bottom: 1rem;
        font-weight: bold;
    }

    .right-card p {
        font-size: 14px;
        margin-bottom: 1.5rem;
    }

    .right-card button {
        background-color: #0e3c2e;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 16px;
        font-weight: bold;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Layout
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Left Section
st.markdown("<div class='left-section'>", unsafe_allow_html=True)
st.image("คู่คิด-removebg-preview.png", width=80)
st.markdown("<div class='form-title'>Sign in</div>", unsafe_allow_html=True)
st.markdown("<div class='form-subtitle'>ยังไม่มีบัญชี? <a href='#'>สร้างบัญชี</a></div>", unsafe_allow_html=True)

st.markdown("""
<input class="input-box" type="text" placeholder="example@gmail.com" />
<input class="input-box" type="password" placeholder="รหัสผ่าน" />

<div class="checkbox-group">
    <label><input type="checkbox"> จำฉันไว้</label>
    <a href="#">ลืมรหัสผ่าน?</a>
</div>

<button class="login-btn">เข้าสู่ระบบ</button>

<div class="social-btn">🔵 เข้าสู่ระบบด้วย Google</div>
<div class="social-btn">🔵 เข้าสู่ระบบด้วย Facebook</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Right Section
st.markdown("<div class='right-section'>", unsafe_allow_html=True)
st.markdown("""
    <div class="right-card">
        <h4>📌 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</h4>
        <p>ใช้บัตร Venus ของคุณทั่วโลก โดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้งานได้ทันที</p>
        <button>ดูเพิ่มเติม</button>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)
