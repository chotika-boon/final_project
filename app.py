import streamlit as st
import base64

# ✅ ต้องมาก่อนทุกคำสั่ง Streamlit
st.set_page_config(layout="wide", page_title="เข้าสู่ระบบ")

# ✅ โหลดฟอนต์
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif !important;
        margin: 0;
        padding: 0;
    }
    .wrapper {
        display: flex;
        height: 100vh;
    }
    .left {
        flex: 1;
        padding: 4rem;
        background: #f4f6f5;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .right {
        flex: 1;
        background: #0e3c2e;
        color: white;
        padding: 4rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 8px;
    }
    .subtitle {
        color: #6c757d;
        margin-bottom: 24px;
    }
    .subtitle a {
        font-weight: bold;
        color: #0e3c2e;
        text-decoration: none;
    }
    .login-btn, .social-btn {
        padding: 12px;
        border: none;
        border-radius: 8px;
        width: 100%;
        font-weight: 600;
    }
    .login-btn {
        background: #0e3c2e;
        color: white;
        margin-top: 10px;
    }
    .social-btn {
        background: white;
        color: #333;
        border: 1px solid #ccc;
        margin-top: 10px;
    }
    .highlight {
        font-size: 24px;
        font-weight: bold;
    }
    .learn-btn {
        margin-top: 20px;
        padding: 10px 20px;
        background: white;
        color: #0e3c2e;
        border: none;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Load logo image
with open("คู่คิด-removebg-preview.png", "rb") as f:
    img_data = base64.b64encode(f.read()).decode()

# ✅ เริ่ม Layout
st.markdown('<div class="wrapper">', unsafe_allow_html=True)

# ⬅️ LEFT SIDE
st.markdown(f"""
<div class="left">
    <img src="data:image/png;base64,{img_data}" width="100">
    <div class="title">Sign in</div>
    <div class="subtitle">ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></div>
""", unsafe_allow_html=True)

email = st.text_input("E-mail", placeholder="example@gmail.com", key="email")
password = st.text_input("Password", placeholder="รหัสผ่าน", type="password", key="pwd")

col1, col2 = st.columns([1, 1])
with col1:
    st.checkbox("จำฉันไว้", value=False)
with col2:
    st.markdown("<div style='text-align:right;'><a href='#'>ลืมรหัสผ่าน?</a></div>", unsafe_allow_html=True)

st.markdown('<button class="login-btn">เข้าสู่ระบบ</button>', unsafe_allow_html=True)
st.markdown('<div class="social-btn">🔵 เข้าสู่ระบบด้วย Google</div>', unsafe_allow_html=True)
st.markdown('<div class="social-btn">🔵 เข้าสู่ระบบด้วย Facebook</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ➡️ RIGHT SIDE
st.markdown("""
<div class="right">
    <div class="highlight">📈 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</div>
    <p>ใช้บัตร Venus ของคุณทั่วโลกโดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้จ่ายได้ทันที</p>
    <button class="learn-btn">ดูเพิ่มเติม</button>
</div>
""", unsafe_allow_html=True)

# ✅ Close wrapper
st.markdown('</div>', unsafe_allow_html=True)
