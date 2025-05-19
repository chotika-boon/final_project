import streamlit as st

# ✅ ต้องอยู่ตรงนี้เลย! ด้านบนสุด
st.set_page_config(page_title="Final Project", page_icon="🔐", layout="wide")

# 🧠 แล้วค่อย import ที่เหลือ
from PIL import Image
import importlib.util
import sys
import os
import uuid
import time
from google.cloud import bigquery
import base64
from login import show_login
from register import show_register
from login import init_session_state



# Load font
with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
    base64_font = base64.b64encode(f.read()).decode()

# Page config

# Dummy app after login
def restaurant_app():
    st.success("🎉 เข้าสู่ระบบเรียบร้อยแล้ว!")
    st.write("นี่คือหน้าหลังล็อกอิน (restaurant_app)")


# Routing
# ✅ Initialize session state
init_session_state()

# ✅ Routing logic
if st.session_state.get("page") == "login":
    init_session_state()
elif st.session_state.get("page") == "register":
    show_register()
elif st.session_state.get("logged_in"):
    # แสดงหลัง login สำเร็จ
    st.success("🎉 เข้าสู่ระบบเรียบร้อยแล้ว!")
    st.write("นี่คือหน้าหลังล็อกอิน (restaurant_app)")
else:
    # fallback เผื่อ state หาย
    st.session_state.page = "login"
    show_login()
