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


# Load font
with open("NotoSansThai-VariableFont_wdth,wght.ttf", "rb") as f:
    base64_font = base64.b64encode(f.read()).decode()

# Page config

# Dummy app after login
def restaurant_app():
    st.success("🎉 เข้าสู่ระบบเรียบร้อยแล้ว!")
    st.write("นี่คือหน้าหลังล็อกอิน (restaurant_app)")

# Main
def main():
    init_session_state()
    if not st.session_state.logged_in:
        show_login()
    else:
        show_register()

if __name__ == "__main__":
    main()

