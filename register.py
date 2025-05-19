import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

def insert_to_gsheet(data):
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key("17os24Dmfczb2qAuy9yUR87vw_6oDWunQulRthw3ZyBg").sheet1
    sheet.append_row(data)

def show_register():
    if "register_visited" not in st.session_state:
        st.session_state.register_visited = True
        st.session_state.credit_cards = []
        st.session_state.card_count = 1

    df = pd.read_csv("credit_card.csv")

    st.markdown("<h2 style='text-align:center;'>สมัครสมาชิก</h2>", unsafe_allow_html=True)

    st.markdown("### 👤 ข้อมูลบัญชีผู้ใช้")
    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("ชื่อผู้ใช้")
    with col2:
        email = st.text_input("อีเมล")

    col1, col2 = st.columns(2)
    with col1:
        password = st.text_input("รหัสผ่าน", type="password")
    with col2:
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

    while len(st.session_state.credit_cards) < st.session_state.card_count:
        st.session_state.credit_cards.append({
            "bank": "",
            "product": "",
            "issuer": ""
        })

    st.markdown("### 💳 ข้อมูลบัตรเครดิต")
    remove_index = None

    for i in range(st.session_state.card_count):
        with st.expander(f"📄 ข้อมูลบัตรที่ {i+1}", expanded=True):
            bank_list = sorted(df["ธนาคาร"].dropna().unique())
            selected_bank = st.selectbox("🏦 เลือกธนาคาร", options=bank_list, key=f"bank_{i}")

            product_df = df[df["ธนาคาร"] == selected_bank]
            product_list = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
            selected_product = st.selectbox("💳 เลือกชื่อบัตร", options=product_list, key=f"product_{i}")

            issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
            issuer_list = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
            selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", options=issuer_list, key=f"issuer_{i}")

            st.session_state.credit_cards[i] = {
                "bank": selected_bank,
                "product": selected_product,
                "issuer": selected_issuer
            }

            if st.session_state.card_count > 1:
                if st.button(f"🗑️ ลบบัตรที่ {i+1}", key=f"remove_{i}"):
                    remove_index = i

    if remove_index is not None:
        del st.session_state.credit_cards[remove_index]
        st.session_state.card_count -= 1
        st.rerun()

    if st.button("➕ เพิ่มบัตร"):
        st.session_state.card_count += 1
        st.rerun()

    if st.button("✅ สมัครสมาชิก"):
        if not username or not email or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
        elif password != confirm_password:
            st.error("❌ รหัสผ่านไม่ตรงกัน")
        else:
            st.success(f"✅ สมัครสำเร็จ! ยินดีต้อนรับคุณ {username} 🎉")
            st.write(pd.DataFrame(st.session_state.credit_cards))

            for card in st.session_state.credit_cards:
                row = [
                    username,
                    email,
                    password,
                    card["bank"],
                    card["issuer"],
                    card["product"],
                    st.session_state.card_count
                ]
                insert_to_gsheet(row)

            st.session_state.page = "login"
            st.rerun()

    if st.button("🔁 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
