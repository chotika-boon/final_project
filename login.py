import streamlit as st


def show_login():
    with st.container():
        st.markdown("<h3 style='text-align:center;'>เข้าสู่ระบบ</h3>", unsafe_allow_html=True)

    # Email input
    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        email = st.text_input(" ", placeholder="เบอร์โทร/อีเมล", key="email_input", label_visibility="collapsed")

    # Password input
    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        password = st.text_input(" ", placeholder="รหัสผ่าน", type="password", key="password_input", label_visibility="collapsed")

    # Custom HTML login button inside center column
    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        st.markdown("""
            <button class="custom-login-btn" onclick="document.querySelector('[data-testid=login-btn]').click()">ตกลง</button>
        """, unsafe_allow_html=True)

    # Hidden real st.button for triggering backend
    st.markdown("<div style='display:none;'>", unsafe_allow_html=True)
    if st.button("เข้าสู่ระบบ", key="login-btn"):
        st.session_state.logged_in = True
    st.markdown("</div>", unsafe_allow_html=True)

    # Register link
    st.markdown("""
        <div class="signup-link">
            <a href="#">ยังไม่มีบัญชี? <strong>สมัครสมาชิก</strong></a>
        </div>
    """, unsafe_allow_html=True)

    # Divider + social buttons
    st.markdown('<div class="divider">หรือ</div>', unsafe_allow_html=True)

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
