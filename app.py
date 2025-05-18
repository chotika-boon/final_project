import streamlit as st
import base64

# ✅ คำสั่งแรกสุด
st.set_page_config(layout="wide", page_title="เข้าสู่ระบบ", initial_sidebar_state="collapsed")

# ✅ โหลด font Noto Sans Thai
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
        margin: 0;
        padding: 0;
    }
    .left-pane {
        flex: 1;
        background-color: #f5f7f6;
        padding: 60px 80px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .right-pane {
        flex: 1;
        background-color: #0e3c2e;
        color: white;
        padding: 60px 40px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: flex-start;
    }
    .title {
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .subtitle {
        font-size: 16px;
        color: #5f6d6d;
        margin-bottom: 32px;
    }
    .subtitle a {
        font-weight: bold;
        color: #0e3c2e;
        text-decoration: none;
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
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Layout เริ่มต้น
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ✅ LEFT PANEL
st.markdown('<div class="left-pane">', unsafe_allow_html=True)

# โลโก้
with open("คู่คิด-removebg-preview.png", "rb") as f:
    image_data = f.read()
    encoded = base64.b64encode(image_data).decode()
    st.markdown(f'<img src="data:image/png;base64,{encoded}" width="120">', unsafe_allow_html=True)

# ฟอร์ม login
st.markdown('<div class="title">Sign in</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></div>', unsafe_allow_html=True)

email = st.text_input("E-mail", placeholder="example@gmail.com")
password = st.text_input("Password", type="password", placeholder="รหัสผ่าน")

col1, col2 = st.columns([1, 1])
with col1:
    st.checkbox("จำฉันไว้", value=False)
with col2:
    st.markdown('<div style="text-align:right;"><a href="#">ลืมรหัสผ่าน?</a></div>', unsafe_allow_html=True)

st.button("เข้าสู่ระบบ", use_container_width=True)

st.markdown("<hr style='margin: 30px 0;'>", unsafe_allow_html=True)

st.markdown('<div class="social-btn">🔵 เข้าสู่ระบบด้วย Google</div>', unsafe_allow_html=True)
st.markdown('<div class="social-btn">🔵 เข้าสู่ระบบด้วย Facebook</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ✅ RIGHT PANEL
st.markdown('<div class="right-pane">', unsafe_allow_html=True)
st.markdown("### 🚀 บรรลุเป้าหมายทางการเงินได้ไวขึ้น")
st.markdown("ใช้บัตร Venus ของคุณทั่วโลกโดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้จ่ายได้ทันที")
st.markdown('<button class="learn-btn">ดูเพิ่มเติม</button>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ✅ Close main
st.markdown('</div>', unsafe_allow_html=True)
