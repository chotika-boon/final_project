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
.container {
    display: flex;
    width: 100vw;
    height: 100vh;
}
.left {
    width: 40%;
    background-color: #f7f9fa;
    padding: 60px 80px;
    box-sizing: border-box;
}
.right {
    width: 60%;
    background-color: #113c2c;
    color: white;
    padding: 60px 80px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
input[type="text"], input[type="password"] {
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 10px;
    margin-bottom: 16px;
    font-size: 16px;
}
button.signin {
    background-color: #143d2c;
    color: white;
    padding: 12px;
    border: none;
    border-radius: 10px;
    width: 100%;
    font-weight: bold;
    font-size: 16px;
    margin-top: 10px;
}
.social {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
    margin-top: 10px;
    font-size: 15px;
    background-color: white;
    color: black;
}
.card-box {
    background-color: white;
    border-radius: 16px;
    padding: 24px;
    color: black;
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

<div class="container">
  <div class="left">
    <h1>Sign in</h1>
    <p>Don't have an account? <a href="#">Create now</a></p>

    <label>E-mail</label>
    <input type="text" placeholder="example@gmail.com" />

    <label>Password</label>
    <input type="password" placeholder="@#*%" />

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
      <label><input type="checkbox" /> Remember me</label>
      <a href="#">Forgot Password?</a>
    </div>

    <button class="signin">Sign in</button>

    <hr style="margin: 30px 0;"/>

    <div class="social">🔵 Continue with Google</div>
    <div class="social">🔷 Continue with Facebook</div>
  </div>

  <div class="right">
    <div class="card-box">
      <h3>Reach financial goals faster</h3>
      <p>Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.</p>
      <button style="background:#143d2c; color:white; padding:10px 20px; border:none; border-radius:8px;">Learn more</button>
      <div class="earnings">
        📈 Earnings: <strong>$350.40</strong>
      </div>
    </div>

    <div style="margin-top: 60px;">
      <h2>Introducing new features</h2>
      <p>Analyzing previous trends ensures that businesses always make the right decision. And as the scale of the decision and its impact magnifies…</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
