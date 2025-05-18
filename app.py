import streamlit as st

st.set_page_config(layout="wide")

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

html, body, .block-container {
    padding: 0 !important;
    margin: 0 !important;
    height: 100vh;
    overflow: hidden;
    font-family: 'Noto Sans Thai', sans-serif;
    background-color: #f0f2f5;
}

.container {
    display: flex;
    flex-direction: row;
    width: 100vw;
    height: 100vh;
}

.left-panel {
    width: 40%;
    background-color: white;
    padding: 80px 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 4px 0 16px rgba(0,0,0,0.05);
}

.right-panel {
    width: 60%;
    background: linear-gradient(135deg, #123d2d 0%, #0a1f17 100%);
    color: white;
    padding: 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.stTextInput > div > input {
    padding: 14px;
    border-radius: 10px;
    border: 1px solid #ddd;
    font-size: 16px;
    background-color: #fff;
}

.stButton > button {
    background-color: #123d2d;
    color: white;
    padding: 14px;
    border-radius: 10px;
    font-weight: bold;
    font-size: 16px;
    border: none;
    width: 100%;
    transition: background 0.3s ease;
}

.stButton > button:hover {
    background-color: #0e2f22;
}

.social-button {
    background: #fff;
    color: #333;
    padding: 12px;
    border-radius: 12px;
    border: 1px solid #ccc;
    text-align: center;
    margin-top: 12px;
    font-size: 15px;
    cursor: pointer;
    transition: background 0.2s ease;
}

.social-button:hover {
    background: #f1f1f1;
}

.link {
    color: #0066cc;
    font-size: 14px;
}

.card-box {
    background: white;
    color: black;
    padding: 24px;
    border-radius: 20px;
    max-width: 420px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 40px;
}

.earnings {
    background-color: #e6f4ea;
    padding: 10px 16px;
    border-radius: 10px;
    display: inline-block;
    margin-top: 12px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Layout
st.markdown('<div class="container">', unsafe_allow_html=True)

# Left Side (Login Form)
st.markdown('<div class="left-panel">', unsafe_allow_html=True)
st.markdown("## 👋 Welcome Back")
st.markdown("ยังไม่มีบัญชี? <span class='link'>สร้างบัญชี</span>", unsafe_allow_html=True)

email = st.text_input("อีเมล", placeholder="example@gmail.com")
password = st.text_input("รหัสผ่าน", type="password", placeholder="@#*%")
st.checkbox("จดจำฉัน")
st.markdown("<div style='text-align:right; margin-bottom:16px;'><span class='link'>ลืมรหัสผ่าน?</span></div>", unsafe_allow_html=True)

st.button("เข้าสู่ระบบ")

st.markdown('<div style="text-align:center;margin:20px 0;">— หรือ —</div>', unsafe_allow_html=True)
st.markdown('<div class="social-button">🔵 เข้าสู่ระบบด้วย Google</div>', unsafe_allow_html=True)
st.markdown('<div class="social-button">🔷 เข้าสู่ระบบด้วย Facebook</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Right Side (Info Panel)
st.markdown('<div class="right-panel">', unsafe_allow_html=True)
st.markdown('<div class="card-box">', unsafe_allow_html=True)
st.markdown("### ✨ บรรลุเป้าหมายทางการเงินเร็วขึ้น")
st.write("ใช้บัตร Venus ของคุณทั่วโลกโดยไม่มีค่าธรรมเนียมแอบแฝง โอนและใช้จ่ายได้อย่างมั่นใจ")
st.button("เรียนรู้เพิ่มเติม")
st.markdown('<div class="earnings">📈 รายได้สะสม: ฿12,000.00</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### 🚀 ฟีเจอร์ใหม่มาแล้ว!")
st.write("วิเคราะห์แนวโน้มย้อนหลังเพื่อช่วยให้ธุรกิจตัดสินใจได้อย่างมั่นใจ ยิ่งการตัดสินใจมีผลกระทบมาก ความแม่นยำยิ่งสำคัญ")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
