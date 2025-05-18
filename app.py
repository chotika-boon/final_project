import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

html, body, .block-container {
    margin: 0 !important;
    padding: 0 !important;
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

input[type="text"], input[type="password"] {
    width: 100%;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #ccc;
    margin-bottom: 16px;
    font-size: 16px;
}

button {
    background-color: #123d2d;
    color: white;
    padding: 14px;
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
    font-size: 16px;
    border: none;
    margin-top: 10px;
}

.social {
    background: white;
    color: black;
    padding: 12px;
    border-radius: 12px;
    border: 1px solid #ccc;
    margin-top: 12px;
    text-align: center;
}

.card-box {
    background: white;
    color: black;
    padding: 24px;
    border-radius: 20px;
    max-width: 400px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
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

<div class="container">
  <div class="left">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Vanamo_Logo.png/240px-Vanamo_Logo.png" width="100"/>
    <h1>Sign in</h1>
    <p>Don’t have an account? <a href="#">Create now</a></p>

    <label>Email</label>
    <input type="text" placeholder="example@gmail.com" />

    <label>Password</label>
    <input type="password" placeholder="@#*%" />

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <label><input type="checkbox" /> Remember me</label>
      <a href="#">Forgot Password?</a>
    </div>

    <button>Sign in</button>

    <div style="text-align: center; margin: 20px 0;">— or —</div>

    <div class="social">🔵 Continue with Google</div>
    <div class="social">🔷 Continue with Facebook</div>
  </div>

  <div class="right">
    <div class="card-box">
      <h3>Reach financial goals faster</h3>
      <p>Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.</p>
      <button style="width:auto; padding:10px 20px; margin-top: 10px;">Learn more</button>
      <div class="earnings">📈 Earnings: $350.40</div>
    </div>

    <div style="margin-top: 80px;">
      <h2>Introducing new features</h2>
      <p>Analyzing previous trends ensures that businesses always make the right decision. And as the scale of the decision and its impact magnifies…</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
