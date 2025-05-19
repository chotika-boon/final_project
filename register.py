import streamlit as st
from engine import BANKS  # ✅ อย่าลืม import

def show_register():
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
