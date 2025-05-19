import streamlit as st
import pandas as pd

def show_register():
    # ✅ Load CSV
    df = pd.read_csv("credit_card.csv")

    st.markdown("## 📝 ลงทะเบียน")

    # -------- 👤 USER INFO FORM (form จะมีแต่ input user/pass) --------
    with st.form("user_register_form"):
        username = st.text_input("ชื่อผู้ใช้")
        password = st.text_input("รหัสผ่าน", type="password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

        submitted = st.form_submit_button("สมัครสมาชิก")

        if submitted:
            if password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จ!")
                st.session_state.page = "login"
                st.rerun()

    st.markdown("## 💳 ข้อมูลบัตรเครดิต")

    # -------- 🏦 Dropdown 1: ธนาคาร --------
    bank_options = sorted(df["ธนาคาร"].dropna().unique())
    selected_bank = st.selectbox("เลือกธนาคาร", bank_options)

    # -------- 💳 Dropdown 2: ชื่อบัตร --------
    product_df = df[df["ธนาคาร"] == selected_bank]
    product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
    selected_product = st.selectbox("เลือกชื่อบัตร", product_options)

    # -------- 🏢 Dropdown 3: ผู้ออกบัตร --------
    issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
    issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
    selected_issuer = st.selectbox("เลือกผู้ออกบัตร", issuer_options)

    # ❗ Note: dropdown ทั้ง 3 จะเชื่อมกัน "ทันที" เพราะอยู่นอก form

    # ปุ่มกลับหน้า login
    if st.button("มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
