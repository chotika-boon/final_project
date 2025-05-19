import streamlit as st
import pandas as pd

def show_register():
    df = pd.read_csv("credit_card.csv")

    # ------- Setup state -------
    if "selected_product" not in st.session_state:
        st.session_state.selected_product = None

    st.markdown("<h2 style='text-align:center;'>สมัครสมาชิก</h2>", unsafe_allow_html=True)

    # -------- 💳 Dropdown อยู่ด้านนอก form --------
    st.markdown("### 💳 ข้อมูลบัตรเครดิต")

    col1, col2 = st.columns(2)

    with col1:
        product_options = sorted(df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
        selected_product = st.selectbox(
            "ชื่อบัตร",
            options=product_options,
            key="selected_product"
        )

    with col2:
        # เชื่อมผู้ออกบัตรจากชื่อบัตรที่เลือก
        issuer_df = df[df["ผลิตภัณฑ์/ชื่อบัตร"] == st.session_state.selected_product]
        issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())

        if issuer_options:
            selected_issuer = st.selectbox("ผู้ออกบัตร", options=issuer_options, key="selected_issuer")
        else:
            st.warning("ไม่พบผู้ออกบัตรสำหรับชื่อบัตรนี้")

    # -------- 👤 แบบฟอร์มบัญชีผู้ใช้ (อยู่ใน form จริง) --------
    st.markdown("### 👤 ข้อมูลบัญชีผู้ใช้")

    with st.form("register_form"):
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

        submitted = st.form_submit_button("✅ สมัครสมาชิก")

        if submitted:
            if not username or not email or not password:
                st.warning("กรุณากรอกข้อมูลให้ครบ")
            elif password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success(f"✅ ยินดีต้อนรับคุณ {username}!")
                st.session_state.page = "login"
                st.rerun()

    # -------- 🔁 ลิงก์เข้าสู่ระบบ --------
    if st.button("มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
