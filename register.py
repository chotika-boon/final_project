import streamlit as st
import pandas as pd

def show_register():
    # โหลดข้อมูลจาก CSV
    df = pd.read_csv("credit_card.csv")

    st.markdown("<h2>ลงทะเบียน</h2>", unsafe_allow_html=True)

    with st.form("register_form"):
        # --- 1. ข้อมูลผู้ใช้ ---
        username = st.text_input("ชื่อผู้ใช้")
        password = st.text_input("รหัสผ่าน", type="password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

        # --- 2. Dropdown ธนาคาร (Chained) ---
        bank_options = sorted(df["ธนาคาร"].dropna().unique())
        selected_bank = st.selectbox("เลือกธนาคาร", bank_options)

        product_df = df[df["ธนาคาร"] == selected_bank]
        product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
        selected_product = st.selectbox("เลือกชื่อบัตร", product_options)

        issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
        issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
        selected_issuer = st.selectbox("เลือกผู้ออกบัตร", issuer_options)

        # --- Submit ---
        submitted = st.form_submit_button("สมัครสมาชิก")

        if submitted:
            if password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จ!")
                st.session_state.page = "login"
                st.rerun()

    # ปุ่มกลับไปหน้า login
    if st.button("มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
