import streamlit as st

# ✅ ต้องอยู่บรรทัดแรก
st.set_page_config(page_title="Sign In", layout="wide")

# ✅ HTML + CSS แบบ full screen ซ้าย-ขวา
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
        flex-direction: row;
        height: 100vh;
        width: 100vw;
    }
    .left {
        flex: 1;
        background-color: #f3f5f4;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 60px;
    }
    .right {
        flex: 1;
        background-color: #0e3c2e;
        color: white;
        padding: 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 1rem;
        margin-bottom: 30px;
        color: #666;
    }
    .subtitle a {
        font-weight: bold;
        color: #0e3c2e;
        text-decoration: none;
    }
    .input {
        width: 100%;
        margin-bottom: 16px;
    }
    .btn-main {
        background-color: #0e3c2e;
        color: white;
        width: 100%;
        padding: 12px;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        margin-top: 10px;
    }
    .social {
        width: 100%;
        margin-top: 16px;
        padding: 10px;
        border-radius: 8px;
        background: white;
        color: #333;
        font-weight: 500;
        border: 1px solid #ccc;
        text-align: center;
    }
    .card-right {
        background-color: white;
        color: black;
        padding: 30px;
        border-radius: 16px;
        max-width: 400px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="container">
  <div class="left">
    <img src="https://i.ibb.co/yhR2r0Z/logo-kooddee.png" width="100" style="margin-bottom: 20px;" />
    <div class="title">Sign in</div>
    <div class="subtitle">ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></div>
    
    <div class="input">E-mail</div>
    <input type="text" class="input" placeholder="example@gmail.com" style="padding:10px;width:100%;border-radius:8px;border:1px solid #ddd;"/>

    <div class="input">Password</div>
    <input type="password" class="input" placeholder="รหัสผ่าน" style="padding:10px;width:100%;border-radius:8px;border:1px solid #ddd;"/>

    <div style="display: flex; justify-content: space-between; align-items: center;">
      <div><input type="checkbox"/> จำฉันไว้</div>
      <a href="#">ลืมรหัสผ่าน?</a>
    </div>

    <button class="btn-main">เข้าสู่ระบบ</button>
    <div class="social">🔵 เข้าสู่ระบบด้วย Google</div>
    <div class="social">🔵 เข้าสู่ระบบด้วย Facebook</div>
  </div>

  <div class="right">
    <div class="card-right">
        <h3>📌 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</h3>
        <p>ใช้บัตร Venus ของคุณทั่วโลก โดยไม่ต้องกังวลเรื่องแปลงสกุลเงิน พร้อมโอนและใช้จ่ายได้ทันที</p>
        <button class="btn-main" style="background:white;color:#0e3c2e;margin-top: 10px;">ดูเพิ่มเติม</button>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
