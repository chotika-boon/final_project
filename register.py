import streamlit as st
import pandas as pd

def show_register():
    # Load data
    df = pd.read_csv("credit_card.csv")

    # CSS for layout & design
    st.markdown("""
    <style>
    .form-box {
        max-width: 700px;
        margin: 3rem auto;
        padding: 2rem 2.5rem;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    }
    .form-title {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 2rem;
        color: #333;
    }
    .section-title {
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-size: 18px;
        font-weight: 600;
        color: #222;
    }
    .footer-link {
        text-align: center;
        margin-top: 1rem;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Start container
    st.markdown("<div class='form-box'>", unsafe_allow_html=True)
    st.markdown("<div class='form-title'>📝 สมัครสมาชิก</div>", unsafe_allow_html=True)

    with st.form("register_form"):

        # 🔐 Section 1: ข้อมูลบัญชีผู้ใช้
        st.markdown("<div class='section-title'>👤 ข้อมูลบัญชีผู้ใช้</div>", unsafe_allow_html=True)

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

        # 💳 Section 2: ข้อมูลบัตร (ไม่เชื่อมกัน)
        st.markdown("<div class='section-title'>💳 ข้อมูลบัตรเครดิต</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            selected_bank = st.selectbox("ธนาคาร", sorted(df["ธนาคาร"].dropna().unique()))
        with col2:
            selected_product = st.selectbox("ชื่อบัตร", sorted(df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique()))

        col1, col2 = st.columns(2)
        with col1:
            selected_issuer = st.selectbox("ผู้ออกบัตร", sorted(df["ผู้ออกบัตร"].dropna().unique()))

        # ✅ Submit
        st.markdown(" ")
        submitted = st.form_submit_button("✅ สมัครสมาชิก", use_container_width=True)

        if submitted:
            if not username or not email or not password:
                st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
            elif password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จ! ยินดีต้อนรับคุณ 🎉")
                st.session_state.page = "login"
                st.rerun()

    # Footer link
    st.markdown("""
        <div class="footer-link">
            🔁 มีบัญชีอยู่แล้ว? <a href="#" onclick="window.location.reload();">เข้าสู่ระบบ</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # Close container
