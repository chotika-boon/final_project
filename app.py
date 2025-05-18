def modern_login_page():
    st.markdown("""
        <style>
            html, body, [class*="css"]  {
                height: 100%;
                margin: 0;
                padding: 0;
            }
            .container {
                display: flex;
                height: 100vh;
                width: 100vw;
                overflow: hidden;
            }
            .left, .right {
                flex: 1;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .left {
                background-color: #f8f9fa;
            }
            .right {
                background-color: #0d3b2e;
                color: white;
                flex-direction: column;
                padding: 40px;
            }
            .form-box {
                max-width: 400px;
                width: 100%;
                padding: 40px;
            }
            .form-title {
                font-size: 32px;
                font-weight: 700;
                margin-bottom: 10px;
            }
            .form-subtitle {
                font-size: 14px;
                color: #666;
                margin-bottom: 30px;
            }
            .form-subtitle a {
                color: #153f2e;
                text-decoration: none;
                font-weight: bold;
            }
            .login-button {
                width: 100%;
                padding: 12px;
                background-color: #153f2e;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
            }
            .social-btn {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 10px;
                margin-top: 10px;
                text-align: center;
                font-size: 14px;
                background-color: white;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""<div class='container'>""", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        st.markdown("<div class='left'>", unsafe_allow_html=True)
        st.markdown("<div class='form-box'>", unsafe_allow_html=True)
        st.markdown("<div class='form-title'>Sign in</div>", unsafe_allow_html=True)
        st.markdown("<div class='form-subtitle'>Don’t have an account? <a href='#'>Create now</a></div>", unsafe_allow_html=True)

        username = st.text_input("E-mail", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        col_remember, col_forgot = st.columns([1, 1])
        with col_remember:
            st.checkbox("Remember me")
        with col_forgot:
            st.markdown("<div style='text-align: right;'><a href='#'>Forgot Password?</a></div>", unsafe_allow_html=True)

        login = st.button("Sign in", use_container_width=True)

        st.markdown("""<hr style='margin: 25px 0;'>""", unsafe_allow_html=True)
        st.markdown("<div class='social-btn'>Continue with Google</div>", unsafe_allow_html=True)
        st.markdown("<div class='social-btn'>Continue with Facebook</div>", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='right'>", unsafe_allow_html=True)
        st.markdown("""
            <h3 style='font-size: 28px;'>Reach financial goals faster</h3>
            <p style='font-size: 14px; max-width: 400px;'>
                Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.
            </p>
            <button class='login-button' style='margin-top: 20px;'>Learn more</button>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if login:
        if username == "admin" and password == "1234":
            st.success("Login Success! ✅")
        else:
            st.error("Login Failed ❌")
