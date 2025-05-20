import streamlit as st
import pandas as pd
import os

CSV_FILE = "user_data.csv"

def authenticate_user(email, password, file_path=CSV_FILE):
    if not os.path.exists(file_path):
        return False, None

    df = pd.read_csv(file_path)
    match = df[(df["email"] == email) & (df["password"] == password)]
    if not match.empty:
        return True, match.iloc[0]["name"]  # ✅ return name
    return False, None

def init_session_state():
    defaults = {
        "logged_in": False,
        "logged_in_email": None,
        "username": None,
        "page": "login",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def show_login():
    st.markdown("<h3 style='text-align:center;'>เข้าสู่ระบบ</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        email = st.text_input(" ", placeholder="อีเมล", key="email_input", label_visibility="collapsed")

    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        password = st.text_input(" ", placeholder="รหัสผ่าน", type="password", key="password_input", label_visibility="collapsed")

    col1, col2, col3 = st.columns([1, 0.6, 1])
    with col2:
        if st.button("เข้าสู่ระบบ"):
            if email and password:
                success, name = authenticate_user(email, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.logged_in_email = email
                    st.session_state.username = name
                    st.session_state.page = "home"
                    st.success("เข้าสู่ระบบสำเร็จ")
                    st.rerun()
                else:
                    st.error("อีเมลหรือรหัสผ่านไม่ถูกต้อง")
            else:
                st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")

    with col2:
        if st.button("ยังไม่มีบัญชี? สมัครสมาชิก"):
            st.session_state.page = "register"
            st.rerun()
