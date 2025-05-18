import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, .block-container {
        padding: 0 !important;
        margin: 0 !important;
        overflow-x: hidden;
        height: 100vh;
        font-family: 'Noto Sans Thai', sans-serif;
    }

    .left, .right {
        height: 100vh;
        padding: 60px;
        box-sizing: border-box;
    }

    .left {
        background-color: #f7f9fa;
    }

    .right {
        background-color: #113c2c;
        color: white;
    }

    .card-box {
        background-color: white;
        color: black;
        border-radius: 16px;
        padding: 24px;
        max-width: 400px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }

    .earnings {
        margin-top: 16px;
        background-color: #f0f4f5;
        padding: 10px;
        border-radius: 10px;
        display: inline-block;
    }

    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 3])  # 40% / 60%

with col1:
    st.markdown("### Sign in")
    st.write("Don't have an account? [Create now](#)")

    email = st.text_input("E-mail", placeholder="example@gmail.com")
    password = st.text_input("Password", type="password", placeholder="@#*%")
    remember = st.checkbox("Remember me")
    st.markdown("[Forgot Password?](#)")

    st.button("Sign in")

    st.markdown("---")
    st.button("🔵 Continue with Google")
    st.button("🔷 Continue with Facebook")

with col2:
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown("### Reach financial goals faster")
    st.write("Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.")
    st.button("Learn more")
    st.markdown('<div class="earnings">📈 Earnings: <strong>$350.40</strong></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Introducing new features")
    st.write("Analyzing previous trends ensures that businesses always make the right decision. "
             "And as the scale of the decision and its impact magnifies…")
