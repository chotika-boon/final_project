import streamlit as st

st.set_page_config(layout="wide")

# ลบ padding + ใส่ฟอนต์
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
    
    html, body, .block-container {
        padding: 0 !important;
        margin: 0 !important;
        height: 100vh;
        overflow-x: hidden;
        font-family: 'Noto Sans Thai', sans-serif;
    }
    .card-box {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        max-width: 400px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 40px;
    }
    .earnings {
        background-color: #f0f4f5;
        padding: 10px 16px;
        border-radius: 10px;
        display: inline-block;
        margin-top: 16px;
        color: #123d2d;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Layout แบบ 40% / 60% โดยไม่มีขอบ
col1, col2 = st.columns([2, 3], gap="none")

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
    st.markdown('<div class="earnings">📈 Earnings: $350.40</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Introducing new features")
    st.write("Analyzing previous trends ensures that businesses always make the right decision. "
             "And as the scale of the decision and its impact magnifies…")
