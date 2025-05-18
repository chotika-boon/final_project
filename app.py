import streamlit as st
import base64

# ✅ ต้องอยู่บรรทัดแรก
st.set_page_config(page_title="เข้าสู่ระบบ", layout="wide")

# ✅ CSS Style
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }
    .container {
        display: flex;
        height: 100vh;
        overflow: hidden;
    }
    .left-side {
        flex: 1;
        padding: 60px;
        background-color: #f5f7f6;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .right-side {
        flex: 1;
        background-color: #0e3c2e;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 60px;
    }
    .form-title {
        font-size: 36px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .form-subtitle {
        color: #5f6d6d;
        margin-bottom: 32px;
    }
    .social-btn {
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #ccc;
        background-color: white;
        color: #333;
        font-weight: 500;
        margin-top: 10px;
        text-align: center;
    }
    .learn-btn {
        background-color: white;
        color: #0e3c2e;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 10px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ เริ่ม layout
st.markdown('<div class="container">', unsafe_allow_html=True)

# ✅ Left section
st.markdown('<div class="left-side">', unsafe_allow_html=True)

# ใส่โลโก้คู่คิด
with open("คู่คิด-removebg-preview.png", "rb") as f:
    img_bytes = f.read()
    encoded = base64.b64encode(img_bytes).decode()
    st.markdown(f'<img src="data:image/png;base64,{encoded}" width="100">', unsafe_allow_html=True)

st.markdown("""
    <div class="form-title">Sign in</div>
    <div class="form-subtitle">ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></div>
""", unsafe_allow_html=True)

username = st.text_input("E-mail", placeholder="example@gmail.com")
password = st.text_input("Password", type="password", placeholder="รหัสผ่าน")

col1, col2 = st.columns([1, 1])
with col1:
    st.checkbox("Remember me")
with col2:
    st.markdown('<div style="text-align:right"><a href="#">Forgot Password?</a></div>', unsafe_allow_html=True)

st.button("เข้าสู่ระบบ", use_container_width=True)

st.markdown("<hr style='margin:20px 0;'>", unsafe_allow_html=True)
st.markdown('<div class="social-btn">🔵 Continue with Google</div>', unsafe_allow_html=True)
st.markdown('<div class="social-btn">🔵 Continue with Facebook</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ✅ Right section
st.markdown('<div class="right-side">', unsafe_allow_html=True)
st.markdown("""
    <h3>Reach financial goals faster</h3>
    <p>ใช้บัตรเครดิต Venus ของคุณทั่วโลกโดยไม่มีค่าธรรมเนียมแอบแฝง โอน ใช้จ่าย อย่างอิสระ</p>
""", unsafe_allow_html=True)
st.markdown('<button class="learn-btn">Learn more</button>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
