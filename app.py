import streamlit as st

# ✅ set config ต้องมาก่อน
st.set_page_config(layout="wide", page_title="เข้าสู่ระบบ")

# ✅ CSS ตกแต่ง
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }

    .container {
        display: flex;
        height: 100vh;
    }

    .left-panel {
        flex: 0.4;
        background-color: #f4f7f6;
        padding: 60px 40px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .right-panel {
        flex: 0.6;
        background-color: #0d3b2e;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 40px;
    }

    .logo {
        width: 80px;
        margin-bottom: 1rem;
    }

    .title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .subtitle {
        font-size: 14px;
        color: #333;
        margin-bottom: 20px;
    }

    .subtitle a {
        color: #0d3b2e;
        font-weight: 600;
        text-decoration: none;
    }

    .input-box {
        padding: 10px;
        border-radius: 8px;
        width: 100%;
        border: 1px solid #ccc;
        margin-bottom: 15px;
    }

    .checkbox-group {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 14px;
        margin-bottom: 15px;
    }

    .login-btn {
        background-color: #0d3b2e;
        color: white;
        padding: 12px;
        width: 100%;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .social-btn {
        background: white;
        padding: 10px;
        text-align: center;
        border-radius: 8px;
        border: 1px solid #ccc;
        margin-bottom: 10px;
        font-weight: 500;
        color: #333;
    }

    .right-card {
        background: white;
        color: #0d3b2e;
        padding: 30px;
        border-radius: 16px;
        text-align: left;
        max-width: 400px;
    }

    .right-card h4 {
        margin-bottom: 12px;
    }

    .right-card p {
        font-size: 14px;
        margin-bottom: 16px;
    }

    .right-card button {
        background: #0d3b2e;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Layout หลัก
st.markdown("""
<div class="container">
    <div class="left-panel">
        <img class="logo" src="https://i.imgur.com/BOZ4rEJ.png" />
        <div class="title">Sign in</div>
        <div class="subtitle">ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></div>

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
