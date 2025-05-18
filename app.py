import streamlit as st

st.set_page_config(layout="wide")

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

html, body, .block-container {
    margin: 0 !important;
    padding: 0 !important;
    height: 100vh;
    overflow-x: hidden;
    font-family: 'Noto Sans Thai', sans-serif;
}

.container {
    display: flex;
    width: 100vw;
    height: 100vh;
}

.left, .right {
    padding: 60px;
    box-sizing: border-box;
    height: 100vh;
}

.left {
    width: 40%;
    background-color: #f5f9f7;
}

.right {
    width: 60%;
    background-color: #123d2d;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.button-primary {
    background-color: #123d2d;
    color: white;
    width: 100%;
    padding: 14px;
    border-radius: 12px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    margin-top: 16px;
}

.social-button {
    background: white;
    padding: 12px;
    border-radius: 12px;
    border: 1px solid #ccc;
    text-align: center;
    margin-top: 10px;
}

.card-box {
    background-color: white;
    padding: 24px;
    border-radius: 20px;
    max-width: 400px;
    color: black;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}

.earnings {
    background-color: #f2f4f6;
    padding: 10px;
    border-radius: 10px;
    display: inline-block;
    margin-top: 12px;
}
</style>
""", unsafe_allow_html=True)

# Layout Structure
st.markdown("""
<div class="container">
  <div class="left">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Vanamo_Logo.png/240px-Vanamo_Logo.png" width="100"/>
    <h1>Sign in</h1>
    <p>Don’t have an account? <a href="#">Create now</a></p>

    <label for="email">E-mail</label>
    <input type="text" id="email" placeholder="example@gmail.com" style="width:100%; padding:12px; margin-bottom:16px; border-radius:10px; border:1px solid #ccc;" />

    <label for="password">Password</label>
    <input type="password" id="password" placeholder="@#*%" style="width:100%; padding:12px; margin-bottom:16px; border-radius:10px; border:1px solid #ccc;" />

    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
      <label><input type="checkbox" /> Remember me</label>
      <a href="#">Forgot Password?</a>
    </div>

    <button class="button-primary">Sign in</button>

    <hr style="margin: 30px 0;" />

    <div class="social-button">🔵 Continue with Google</div>
    <div class="social-button">🔷 Continue with Facebook</div>
  </div>

  <div class="right">
    <div class="card-box">
      <h3>Reach financial goals faster</h3>
      <p>Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.</p>
      <button class="button-primary" style="width: auto; padding: 10px 20px; margin-top: 10px;">Learn more</button>
      <div class="earnings">📈 Earnings: <strong>$350.40</strong></div>
    </div>

    <div style="margin-top: 80px;">
      <h2>Introducing new features</h2>
      <p>Analyzing previous trends ensures that businesses always make the right decision. And as the scale of the decision and its impact magnifies…</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
