import streamlit as st
import pandas as pd

def show_register():

    # อ่านไฟล์ CSV (คุณเปลี่ยน path ได้)
    df = pd.read_csv("credit_card.csv")

    st.markdown("## 💳 ค้นหาบัตรเครดิต")

# --- 1. Dropdown: เลือกธนาคาร ---
    bank_options = sorted(df["ธนาคาร"].dropna().unique())
    selected_bank = st.selectbox("เลือกธนาคาร", bank_options)

# --- 2. กรองตามธนาคาร แล้วเลือกชื่อบัตร ---
    product_df = df[df["ธนาคาร"] == selected_bank]
    product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
    selected_product = st.selectbox("เลือกชื่อบัตร", product_options)

# --- 3. กรองตามชื่อบัตร แล้วเลือกผู้ออกบัตร ---
    issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
    issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
    selected_issuer = st.selectbox("เลือกผู้ออกบัตร", issuer_options)

# --- แสดงผลลัพธ์ที่เลือก ---
    st.markdown("### 📄 รายละเอียดบัตรที่เลือก")
    filtered = issuer_df[issuer_df["ผู้ออกบัตร"] == selected_issuer]
    st.dataframe(filtered)
    st.markdown("<h2>ลงทะเบียน</h2>", unsafe_allow_html=True)

    with st.form("register_form"):
        username = st.text_input("ชื่อผู้ใช้")
        password = st.text_input("รหัสผ่าน", type="password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")
        bank = st.selectbox("ธนาคารที่ถือบัตรเครดิต", options=BANKS)

        submitted = st.form_submit_button("สมัครสมาชิก")

        if submitted:
            if password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จ!")
                st.session_state.page = "login"
                st.rerun()

    if st.button("มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
