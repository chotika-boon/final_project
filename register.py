import streamlit as st
import pandas as pd

def show_register():
    df = pd.read_csv("credit_card.csv")

    # -------- CSS Modern --------
    st.markdown("""
    <style>
    .register-container {
        max-width: 720px;
        margin: 3rem auto;
        padding: 2rem 2.5rem;
        background-color: #fff;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .register-title {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        padding: 0.6rem 0.75rem;
        font-size: 15px;
    }
    .form-footer {
        margin-top: 2rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='register-container'>", unsafe_allow_html=True)
    st.markdown("<div class='register-title'>📝 สมัครสมาชิก</div>", unsafe_allow_html=True)

    with st.form("register_form"):
        col1, col2 = st.columns(2)

        with col1:
            username = st.text_input("👤 ชื่อผู้ใช้")
        with col2:
            password = st.text_input("🔐 รหัสผ่าน", type="password")

        col1, col2 = st.columns(2)
        with col1:
            confirm_password = st.text_input("🔐 ยืนยันรหัสผ่าน", type="password")

        # Dropdown: ธนาคาร
        bank_options = sorted(df["ธนาคาร"].dropna().unique())
        col1, col2 = st.columns(2)
        with col1:
            selected_bank = st.selectbox("🏦 เลือกธนาคาร", bank_options)

        # Dropdown: ชื่อบัตร
        product_df = df[df["ธนาคาร"] == selected_bank]
        product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
        with col2:
            selected_product = st.selectbox("💳 เลือกชื่อบัตร", product_options)

        # Dropdown: ผู้ออกบัตร
        issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
        issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
        col1, col2 = st.columns(2)
        with col1:
            selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", issuer_options)

        # ปุ่ม Submit — อยู่ล่างสุด
        submit = st.form_submit_button("✅ สมัครสมาชิก", use_container_width=True)

        if submit:
            if password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จแล้ว!")
                st.session_state.page = "login"
                st.rerun()

    st.markdown("<div class='form-footer'>", unsafe_allow_html=True)
    if st.button("🔁 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # ปิด container
