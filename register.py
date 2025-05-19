import streamlit as st
import pandas as pd
import os

CSV_FILE = "user_data.csv"
CARD_DATA_FILE = "credit_card.csv"

# ---------- บันทึกข้อมูลลง CSV ----------
def save_to_csv(row, file_path=CSV_FILE):
    df_new = pd.DataFrame([row])
    if not os.path.exists(file_path):
        df_new.to_csv(file_path, index=False)
    else:
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(file_path, index=False)

# ---------- เช็คอีเมลซ้ำ ----------
def is_duplicate_email(email, file_path=CSV_FILE):
    if not os.path.exists(file_path):
        return False
    df = pd.read_csv(file_path)
    return email in df["email"].values

# ---------- หน้า Register ----------
def show_register():
    if "register_visited" not in st.session_state:
        st.session_state.register_visited = True
        st.session_state.credit_cards = []
        st.session_state.card_count = 1

    df = pd.read_csv(CARD_DATA_FILE)

    st.markdown("<h2 style='text-align:center;'>สมัครสมาชิก</h2>", unsafe_allow_html=True)

    # ข้อมูลผู้ใช้
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

    # เตรียม credit card slots
    while len(st.session_state.credit_cards) < st.session_state.card_count:
        st.session_state.credit_cards.append({
            "bank": "",
            "product": "",
            "issuer": ""
        })

    # ข้อมูลบัตรเครดิต
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

    # ✅ สมัครสมาชิก
    if st.button("✅ สมัครสมาชิก"):
        if not username or not email or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
        elif password != confirm_password:
            st.error("❌ รหัสผ่านไม่ตรงกัน")
        elif is_duplicate_email(email):
            st.error("❌ อีเมลนี้ถูกใช้งานแล้ว")
        else:
            for card in st.session_state.credit_cards:
                row = {
                    "name": username,
                    "email": email,
                    "password": password,
                    "bank": card["bank"],
                    "credit_type": card["issuer"],
                    "credit_name": card["product"],
                    "card_count": st.session_state.card_count
                }
                save_to_csv(row)
            st.success(f"✅ สมัครสำเร็จ! ยินดีต้อนรับคุณ {username} 🎉")
            st.session_state.page = "login"
            st.rerun()

    # 🔁 ลิงก์ไปหน้า Login
    if st.button("🔁 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
