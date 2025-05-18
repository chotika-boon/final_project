import streamlit as st

# ✅ set_page_config ต้องมาก่อน
st.set_page_config(layout="wide", page_title="Sign In")

# ✅ ใช้ฟอนต์ Noto Sans Thai
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif;
        margin: 0;
        padding: 0;
    }

    .container {
        display: flex;
        height: 100vh;
        overflow: hidden;
    }

    .left {
        flex: 0.4;
        background-color: #f4f7f6;
        padding: 5rem 3rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .right {
        flex: 0.6;
        background-color: #0d3b2e;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        padding: 4rem;
    }

    .logo {
        width: 80px;
        margin-bottom: 1rem;
    }

    .title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        color: #526262;
        margin-bottom: 2rem;
    }

    .input {
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 8px;
        width: 100%;
        margin-bottom: 1rem;
    }

    .btn-main {
        background-color: #0d3b2e;
        color: white;
        font-weight: bold;
        padding: 12px;
        width: 100%;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: none;
    }

    .social {
        background-color: white;
        color: #333;
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 10px;
        width: 100%;
        text-align: center;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }

    .right-box {
        background: white;
        color: #0d3b2e;
        border-radius: 16px;
        padding: 2rem;
        max-width: 400px;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Layout แบบ Flexbox แท้
st.markdown("""
<div class="container">
    <div class="left">
        <img class="logo" src="https://i.imgur.com/BOZ4rEJ.png" />
        <div class="title">Sign in</div>
        <div class="subtitle">ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></div>

        <div class="input">E-mail</div>
        <input type="text" class="input" placeholder="example@gmail.com" />

        <div class="input">Password</div>
        <input type="password" class="input" placeholder="รหัสผ่าน" />

        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div><input type="checkbox"/> จำฉันไว้</div>
            <a href="#">ลืมรหัสผ่าน?</a>
        </div><br>

        <button class="btn-main">เข้าสู่ระบบ</button>

        <div class="social">🔵 เข้าสู่ระบบด้วย Google</div>
        <div class="social">🔵 เข้าสู่ระบบด้วย Facebook</div>
    </div>

    <div class="right">
        <div class="right-box">
            <h4>📌 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</h4>
            <p>ใช้บัตร Venus ของคุณทั่วโลก โดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้งานได้ทันที</p>
            <button class="btn-main" style="background:white; color:#0d3b2e;">ดูเพิ่มเติม</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
