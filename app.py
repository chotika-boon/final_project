def modern_login_page():
    st.markdown('<div class="center-wrapper"><div class="login-container">', unsafe_allow_html=True)

    st.markdown("""
        <h2 style="font-weight: 700; margin-bottom: 1.5rem;">เข้าสู่ระบบ</h2>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="max-width: 320px; width: 100%; margin: 0 auto;">
    """, unsafe_allow_html=True)

    email = st.text_input("เบอร์โทร/อีเมล", key="email")

    col1, col2 = st.columns([2, 1])
    with col2:
        if st.button("ถัดไป", key="next"):
            st.session_state.logged_in = True

    password = st.text_input("รหัสผ่าน", type="password", key="password")

    st.markdown("""
        </div>
        <div style="text-align:right; margin-top: 0.5rem; font-size: 14px;">
            <a href="#">ยังไม่มีบัญชี? <strong>สมัครสมาชิก</strong></a>
        </div>
        <div class="divider">หรือ</div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="display:flex; justify-content:center; flex-direction: column; align-items:center;">
            <button class="social-button">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="20" />
                เข้าสู่ระบบด้วย Facebook
            </button>
            <button class="social-button">
                <img src="https://cdn-icons-png.flaticon.com/512/2111/2111396.png" width="20" />
                เข้าสู่ระบบด้วย LINE
            </button>
            <button class="social-button">
                <img src="https://cdn-icons-png.flaticon.com/512/281/281764.png" width="20" />
                เข้าสู่ระบบด้วย Google
            </button>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)
