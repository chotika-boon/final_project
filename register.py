import streamlit as st

def show_register():
    """Render registration page"""
    st.title("ลงทะเบียน")
    
    with st.form("register_form"):
        username = st.text_input("ชื่อผู้ใช้", key="register_username")
        password = st.text_input("รหัสผ่าน", type="password", key="register_password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password", key="confirm_password")
        
        bank = st.selectbox("ธนาคารที่ถือบัตรเครดิต", options=BANKS)
        card_type = st.selectbox("ประเภทบัตรเครดิตที่ถือ", options=CARD_TYPES)
        lifestyle = st.selectbox("ไลฟ์สไตล์ของคุณ", options=LIFESTYLES)
        
        col1, col2 = st.columns(2)
        with col1:
            submit_button = st.form_submit_button("ลงทะเบียน")
        with col2:
            back_button = st.form_submit_button("กลับ")
    
    if submit_button:
        if password != confirm_password:
            st.error("รหัสผ่านไม่ตรงกัน")
        elif not username or not password:
            st.error("กรุณากรอกชื่อผู้ใช้และรหัสผ่าน")
        else:
            success, message = user_manager.register_user(username, password, bank, card_type, lifestyle)
            if success:
                st.success(message)
                st.session_state.show_register = False
                st.rerun()
            else:
                st.error(message)
    
    if back_button:
        st.session_state.show_register = False
        st.rerun()
