import streamlit as st
import os
import uuid
import time
from google.cloud import bigquery

st.set_page_config(layout="wide")

# --- STYLES ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: 'Segoe UI', sans-serif;
        }
        .full-container {
            display: flex;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }
        .left-panel, .right-panel {
            width: 50vw;
            height: 100vh;
            padding: 60px;
            box-sizing: border-box;
        }
        .left-panel {
            background: #f5f7f6;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .right-panel {
            background: #0d3b2e;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .login-box {
            max-width: 400px;
            margin: auto;
        }
        .login-box h1 {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 8px;
        }
        .login-box p {
            margin-bottom: 24px;
            font-size: 14px;
        }
        .login-box .input {
            width: 100%;
            padding: 12px;
            margin-bottom: 16px;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 14px;
        }
        .login-box .button {
            background: #153f2e;
            border: none;
            padding: 12px;
            color: white;
            font-size: 16px;
            border-radius: 12px;
            width: 100%;
            font-weight: bold;
            margin-top: 8px;
        }
        .social {
            background: white;
            color: #333;
            padding: 10px;
            margin-top: 10px;
            border-radius: 12px;
            border: 1px solid #ddd;
            text-align: center;
            font-size: 14px;
        }
        .highlight-card {
            background: white;
            color: black;
            padding: 30px;
            border-radius: 20px;
            max-width: 400px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# --- SESSION ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "register_mode" not in st.session_state:
    st.session_state.register_mode = False

# --- UI ---
def login_register_ui():
    st.markdown("<div class='full-container'>", unsafe_allow_html=True)

    # LEFT
    st.markdown("<div class='left-panel'><div class='login-box'>", unsafe_allow_html=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Logo_placeholder.svg/512px-Logo_placeholder.svg.png", width=80)

    if st.session_state.register_mode:
        st.markdown("<h1>Sign up</h1>", unsafe_allow_html=True)
        st.markdown("<p>Already have an account? <a href='#' onclick=\"window.location.reload()\">Sign in</a></p>", unsafe_allow_html=True)
        email = st.text_input("E-mail", key="email_register")
        password = st.text_input("Password", type="password", key="password_register")
        confirm = st.text_input("Confirm Password", type="password", key="confirm")
        if st.button("Create Account", use_container_width=True):
            if password != confirm:
                st.error("Passwords do not match")
            else:
                row = [{"customer_id": str(uuid.uuid4()), "username": email, "password": password, "bank": "-", "credit_name": "", "card_type": "-"}]
                errors = client.insert_rows_json(BQ_TABLE, row)
                if not errors:
                    st.success("Registered successfully!")
                    st.session_state.register_mode = False
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("BigQuery insert failed")
    else:
        st.markdown("<h1>Sign in</h1>", unsafe_allow_html=True)
        st.markdown("<p>Don't have an account? <a href='#' onclick=\"window.location.reload()\">Create now</a></p>", unsafe_allow_html=True)
        email = st.text_input("E-mail", key="email_login")
        password = st.text_input("Password", type="password", key="password_login")
        if st.button("Sign in", use_container_width=True):
            query = f"SELECT * FROM `{BQ_TABLE}` WHERE username='{email}' AND password='{password}'"
            rows = list(client.query(query).result())
            if rows:
                st.session_state.logged_in = True
                st.success("Welcome back!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid credentials")

        st.markdown("<div class='social'>Continue with Google</div>", unsafe_allow_html=True)
        st.markdown("<div class='social'>Continue with Facebook</div>", unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # RIGHT
    st.markdown("<div class='right-panel'>", unsafe_allow_html=True)
    st.markdown("""
        <div class='highlight-card'>
          <h3>Reach financial goals faster</h3>
          <p>Use your Venus card around the world with no hidden fees. Hold, transfer and spend money.</p>
          <button class='button' style='margin-top:20px;'>Learn more</button>
        </div>
        <div style='margin-top:40px; text-align:center;'>
          Introducing <strong>new features</strong><br>
          <span style='font-size: 13px;'>Analyzing previous trends ensures better business decisions.</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

# --- MAIN ---
if not st.session_state.logged_in:
    login_register_ui()
else:
    st.success("🎉 Logged in successfully!")
    st.write("This would be your home/dashboard page.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
