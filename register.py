import streamlit as st
import pandas as pd

def show_register():
    df = pd.read_csv("credit_card.csv")

    # 🎯 Session state สำหรับควบคุม dropdown link
    if "selected_bank" not in st.session_state:
        st.session_state.selected_bank = None
    if "selected_product" not in st.session_state:
        st.session_state.selected_product = None
    if "selected_issuer" not in st.session_state:
        st.session_state.selected_issuer = None

    st.markdown("<h2 style='text-align:center;'>สมัครสมาชิก</h2>", unsafe_allow_html=True)

    with st.form("register_form"):
        # ---------------- 🧑‍💼 ข้อมูลผู้ใช้ ----------------
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

        # ---------------- 💳 ชื่อบัตร ----------------
        product_options = sorted(df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
        selected_product = st.selectbox(
            "💳 เลือกชื่อบัตร",
            options=product_options,
            index=product_options.index(st.session_state.selected_product) if st.session_state.selected_product in product_options else 0,
            key="selected_product"
        )

        # ✔️ บันทึกการเลือกไว้ใน session
        st.session_state.selected_product = selected_product

        # ---------------- 🏢 ผู้ออกบัตร (เชื่อมจากชื่อบัตร) ----------------
        filtered_df = df[df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
        issuer_options = sorted(filtered_df["ผู้ออกบัตร"].dropna().unique())

        # ให้ค่า default ถ้าไม่เคยเลือก
        if st.session_state.selected_issuer not in issuer_options:
            st.session_state.selected_issuer = issuer_options[0] if issuer_options else None

        selected_issuer = st.selectbox(
            "🏢 เลือกผู้ออกบัตร",
            options=issuer_options,
            index=issuer_options.index(st.session_state.selected_issuer) if st.session_state.selected_issuer in issuer_options else 0,
            key="selected_issuer"
        )

        st.session_state.selected_issuer = selected_issuer

        # ---------------- ✅ ปุ่มสมัคร ----------------
        submitted = st.form_submit_button("สมัครสมาชิก")

        if submitted:
            if not username or not email or not password:
                st.warning("กรุณากรอกข้อมูลให้ครบ")
            elif password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จ! 🎉")
                st.session_state.page = "login"
                st.rerun()

    # ---------------- 🔁 ลิงก์เข้าสู่ระบบ ----------------
    if st.button("มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
