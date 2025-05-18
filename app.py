import streamlit as st

st.set_page_config(layout="wide")

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

html, body, .block-container {
    padding: 0 !important;
    margin: 0 !important;
    height: 100vh;
    overflow: hidden;
    font-family: 'Noto Sans Thai', sans-serif;
}

section.main > div {
    padding: 0 !important;
}

.container {
    display: flex;
    width: 100vw;
    height: 100vh;
}

.left {
    width: 40%;
    background-color: #f6f8f9;
    padding: 60px 80px;
    box-sizing: border-box;
}

.right {
    width: 60%;
    background-color: #123d2d;
    padding: 60px 80px;
    color: white;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.stTextInput > div > input {
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #ccc;
    font-size: 16px;
    background-color: #fff;
}

.stButton > button {
    background-color: #123d2d;
    color: white;
    padding: 14px;
    border-radius: 12px;
    font-weight: bold;
    font-size: 16px;
    border: none;
    width: 100%;
}

.social-button {
    background: white;
    color: black;
    padding: 12px;
    border-radius: 12px;
    border: 1px solid #ccc;
    text-align: center;
    margin-top: 12px;
    font-size: 15px;
}

.card-box {
    background: white;
    color: black;
    padding: 24px;
    border-radius: 20px;
    max-width: 400px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
    margin-bottom: 40px;
}

.earnings {
    background-color: #f0f4f5;
    padding: 10px 16px;
    border-radius: 10px;
    display: inline-block;
    margin-top: 12px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Layout แบบ 40% / 60%
st.markdown('<div class="container">', unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown('<div class="left">', unsafe_allow_html=True)

        st.markdown("## Sign in")
        st.markdown("Don't have an account? [Create now](#)")

        email = st.text_input("E-mail", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password", placeholder="@#*%")
        remember = st.checkbox("Remember me")
        st.markdown("[Forgot Password?](#)", unsafe_allow_html=True)

        login_btn = st.button("Sign in")

        st.markdown('<div style="text-align:center;margin:20px 0;">— or —</div>', unsafe_allow_html=True)
        st.markdown('<div class="social-button">🔵 Continue with Google</div>', unsafe_allow_html=True)
        st.markdown('<div class="social-button">🔷 Continue with Facebook</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="right">', unsafe_allow_html=True)

        st.markdown('<div class="card-box">', unsafe_allow_html=True)
        st.markdown("### Reach financial goals faster")
        st.write("Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.")
        st.button("Learn more")
        st.markdown('<div class="earnings">📈 Earnings: $350.40</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("### Introducing new features")
        st.write("Analyzing previous trends ensures that businesses always make the right decision. And as the scale of the decision and its impact magnifies…")

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
