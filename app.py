import streamlit as st

st.set_page_config(layout="wide", page_title="Login Page")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif;
    }
    .container {
        display: flex;
        height: 100vh;
        width: 100vw;
    }
    .left-panel {
        flex: 0.4;
        background: #f5f7f7;
        padding: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .right-panel {
        flex: 0.6;
        background: #0e3c2e;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 40px;
    }
    .input-box {
        padding: 10px;
        margin-bottom: 15px;
        width: 100%;
        border: 1px solid #ccc;
        border-radius: 8px;
        font-size: 16px;
    }
    .checkbox-group {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        margin-bottom: 20px;
    }
    .login-btn {
        background-color: #0e3c2e;
        color: white;
        border: none;
        padding: 12px;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        margin-bottom: 20px;
        cursor: pointer;
    }
    .social-btn {
        background: white;
        color: #333;
        text-align: center;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 8px;
        margin-bottom: 10px;
        font-weight: 500;
        cursor: pointer;
    }
    .right-card {
        max-width: 400px;
        text-align: center;
    }
    .right-card h4 {
        font-size: 20px;
        margin-bottom: 10px;
    }
    .right-card p {
        font-size: 14px;
        margin-bottom: 20px;
    }
    .right-card button {
        background: white;
        color: #0e3c2e;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="container">
    <div class="left-panel">
        <img src="https://i.ibb.co/3TScZSm/คู่คิด-removebg-preview.png" width="100"/>

        <h2>Sign in</h2>
        <p>ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></p>

        <input class="input-box" type="text" placeholder="example@gmail.com" />
        <input class="input-box" type="password" placeholder="รหัสผ่าน" />

        <div class="checkbox-group">
            <label><input type="checkbox"> จำฉันไว้</label>
            <a href="#">ลืมรหัสผ่าน?</a>
        </div>

        <button class="login-btn">เข้าสู่ระบบ</button>

        <div class="social-btn">🔵 เข้าสู่ระบบด้วย Google</div>
        <div class="social-btn">🔵 เข้าสู่ระบบด้วย Facebook</div>
    </div>

    <div class="right-panel">
        <div class="right-card">
            <h4>📌 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</h4>
            <p>ใช้บัตร Venus ของคุณทั่วโลก โดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้งานได้ทันที</p>
            <button>ดูเพิ่มเติม</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
