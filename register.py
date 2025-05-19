import streamlit as st
import pandas as pd

def show_register():
    # Load credit card CSV
    df = pd.read_csv("credit_card.csv")

    # 💡 สีหลักของ Wongnai ประมาณ #00A8E8 หรือ #0084FF
    PRIMARY_COLOR = "#0084FF"

    # 🎨 Custom CSS ให้ฟีล Web จริง
    st.markdown(f"""
    <style>
    .signup-container {{
        max-width: 720px;
        margin: 3rem auto;
        padding: 2.5rem;
        background: #ffffff;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
        font-family: "Noto Sans Thai", sans-serif;
    }}
    .form-title {{
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #222;
        margin-bottom: 2rem;
    }}
    .section-title {{
        font-size: 18px;
        font-weight: 600;
        color: #444;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }}
    .stTextInput > div > div > input,
    .stSelectbox > div > div {{
        padding: 0.6rem 0.75rem;
        font-size: 15px;
    }}
    .stButton button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 0.6rem 1rem;
        border-radius: 8px;
        width: 100%;
        border: none;
        margin-top: 1.5rem;
    }}
    .footer {{
        text-align: center;
        font-size: 14px;
        margin-top: 1.5rem;
        color: #666;
    }}
    </style>
    """, unsafe_allow_html=True)

    # 🧱 Start layout
    st.markdown("<div class='signup-container'>", unsafe_allow_html=True)
    st.markdown("<div class='form-title'>สมัครสมาชิก Wongnai</div>", unsafe_allow_html=True)

    # ---------------- ข้อมูลบัญชีผู้ใช้ ----------------
    st.markdown("<div class='section-title'>🧑‍💼 ข้อมูลบัญชีผู้ใช้</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("ชื่อผู้ใช้")
    with col2:
        email = st.text_input("อีเมล")

    col1, col2 = st.columns(2)
    with col1:
        password = st.text_input("รหัสผ่าน", type="password")
    with col2:
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

    # ---------------- ข้อมูลบัตรเครดิต (ไม่เชื่อมกัน) ----------------
    st.markdown("<div class='section-title'>💳 ข้อมูลบัตรเครดิต</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        selected_bank = st.selectbox("ธนาคาร", sorted(df["ธนาคาร"].dropna().unique()))
    with col2:
        selected_product = st.selectbox("ชื่อบัตร", sorted(df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique()))

    col1, col2 = st.columns(2)
    with col1:
        selected_issuer = st.selectbox("ผู้ออกบัตร", sorted(df["ผู้ออกบัตร"].dropna().unique()))

    # ---------------- ปุ่มสมัคร ----------------
    if st.button("✅ สมัครสมาชิก"):
        if not username or not email or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
        elif password != confirm_password:
            st.error("❌ รหัสผ่านไม่ตรงกัน")
        else:
            st.success("✅ สมัครสำเร็จแล้ว! ยินดีต้อนรับคุณ 🎉")
            st.session_state.page = "login"
            st.rerun()

    # ---------------- ลิงก์เข้าสู่ระบบ ----------------
    st.markdown("""
        <div class="footer">
            มีบัญชีอยู่แล้ว? <a href="#" onclick="window.location.reload();">เข้าสู่ระบบ</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
