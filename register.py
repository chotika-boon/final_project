import streamlit as st
import pandas as pd

def show_register():
    df = pd.read_csv("credit_card.csv")

    # --------- เตรียม State ครั้งแรก ---------
    if "selected_bank" not in st.session_state:
        st.session_state.selected_bank = df["ธนาคาร"].dropna().unique()[0]
    if "selected_product" not in st.session_state:
        st.session_state.selected_product = None

    st.markdown("<h2 style='text-align:center;'>สมัครสมาชิก</h2>", unsafe_allow_html=True)

    with st.form("register_form"):
        # ---------------- ข้อมูลผู้ใช้ ----------------
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

        # ---------------- Dropdown 1: ธนาคาร ----------------
        bank_options = sorted(df["ธนาคาร"].dropna().unique())
        selected_bank = st.selectbox(
            "🏦 เลือกธนาคาร",
            options=bank_options,
            index=bank_options.index(st.session_state.selected_bank) if st.session_state.selected_bank in bank_options else 0,
            key="selected_bank"
        )

        # ---------------- Dropdown 2: ชื่อบัตร ----------------
        product_df = df[df["ธนาคาร"] == st.session_state.selected_bank]
        product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())

        if st.session_state.selected_product not in product_options:
            st.session_state.selected_product = product_options[0] if product_options else None

        selected_product = st.selectbox(
            "💳 เลือกชื่อบัตร",
            options=product_options,
            index=product_options.index(st.session_state.selected_product) if st.session_state.selected_product in product_options else 0,
            key="selected_product"
        )

        # ---------------- Dropdown 3: ผู้ออกบัตร ----------------
        issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == st.session_state.selected_product]
        issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
        selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", options=issuer_options)

        # ---------------- Submit ----------------
        submitted = st.form_submit_button("✅ สมัครสมาชิก")

        if submitted:
            if not username or not email or not password:
                st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
            elif password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จ! ยินดีต้อนรับคุณ 🎉")
                st.session_state.page = "login"
                st.rerun()

    # ---------------- กลับเข้าสู่ระบบ ----------------
    if st.button("มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
