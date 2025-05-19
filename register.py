import streamlit as st

def show_register():
    st.markdown("<h3 style='text-align:center;'>สมัครสมาชิก</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        username = st.text_input(" ", placeholder="ชื่อผู้ใช้", key="username_input", label_visibility="collapsed")

    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        email = st.text_input(" ", placeholder="อีเมล", key="reg_email", label_visibility="collapsed")

    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        password = st.text_input(" ", placeholder="รหัสผ่าน", type="password", key="reg_password", label_visibility="collapsed")

    st.markdown("""
        <button class="custom-login-btn" onclick="document.querySelector('[data-testid=register-btn]').click()">สมัครสมาชิก</button>
    """, unsafe_allow_html=True)

    if st.button("ยืนยันสมัคร", key="register-btn"):
        st.success("🎉 สมัครสมาชิกเรียบร้อยแล้ว!")

    st.markdown("""
        <div class="signup-link" style="text-align:center;">
            <a href="/?page=login">มีบัญชีอยู่แล้ว? <strong>เข้าสู่ระบบ</strong></a>
        </div>
    """, unsafe_allow_html=True)
