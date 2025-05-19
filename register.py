import streamlit as st
import pandas as pd

def show_register():
    # ---------- Load data ----------
    df = pd.read_csv("credit_card.csv")

    st.markdown("<h2 style='text-align:center;'>สมัครสมาชิก</h2>", unsafe_allow_html=True)

    # ---------- Section: ข้อมูลผู้ใช้ ----------
    st.markdown("### 👤 ข้อมูลบัญชีผู้ใช้")

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

    # ---------- Section: ข้อมูลบัตรเครดิต ----------
    st.markdown("### 💳 ข้อมูลบัตรเครดิต")

    # ✅ Step 1: ธนาคาร
    bank_list = sorted(df["ธนาคาร"].dropna().unique())
    default_bank = bank_list[0] if bank_list else None
    selected_bank = st.selectbox("🏦 เลือกธนาคาร", options=bank_list, index=0)

    # ✅ Step 2: กรองชื่อบัตร
    product_df = df[df["ธนาคาร"] == selected_bank]
    product_list = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
    default_product = product_list[0] if product_list else None
    selected_product = st.selectbox("💳 เลือกชื่อบัตร", options=product_list, index=0)

    # ✅ Step 3: กรองผู้ออกบัตร
    issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
    issuer_list = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
    default_issuer = issuer_list[0] if issuer_list else None
    selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", options=issuer_list, index=0)

    # ---------- Submit Button ----------
    if st.button("✅ สมัครสมาชิก"):
        if not username or not email or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
        elif password != confirm_password:
            st.error("❌ รหัสผ่านไม่ตรงกัน")
        else:
            st.success(f"✅ สมัครสำเร็จ! ยินดีต้อนรับคุณ {username} 🎉")
            st.session_state.page = "login"
            st.rerun()

    # ---------- ลิงก์เข้าสู่ระบบ ----------
    if st.button("🔁 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
