import streamlit as st
import pandas as pd

def show_register():
    # ---------- Load data ----------
    df = pd.read_csv("credit_card.csv")

    st.markdown("<h2 style='text-align:center;'>สมัครสมาชิก</h2>", unsafe_allow_html=True)

    # ---------- Section: ข้อมูลผู้ใช้ ----------
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

    # ---------- Section: ข้อมูลบัตรเครดิต ----------
    st.markdown("### 💳 ข้อมูลบัตรเครดิต")

    if "credit_cards" not in st.session_state:
        st.session_state.credit_cards = []

    if "card_count" not in st.session_state:
        st.session_state.card_count = 1

    for i in range(st.session_state.card_count):
        with st.expander(f"📄 ข้อมูลบัตรที่ {i+1}", expanded=True):
            bank_list = sorted(df["ธนาคาร"].dropna().unique())
            selected_bank = st.selectbox(f"🏦 เลือกธนาคาร", options=bank_list, key=f"bank_{i}")

            product_df = df[df["ธนาคาร"] == selected_bank]
            product_list = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
            selected_product = st.selectbox(f"💳 เลือกชื่อบัตร", options=product_list, key=f"product_{i}")

            issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
            issuer_list = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
            selected_issuer = st.selectbox(f"🏢 เลือกผู้ออกบัตร", options=issuer_list, key=f"issuer_{i}")

            # เก็บข้อมูลลง session_state
            if len(st.session_state.credit_cards) <= i:
                st.session_state.credit_cards.append({
                    "bank": selected_bank,
                    "product": selected_product,
                    "issuer": selected_issuer
                })
            else:
                st.session_state.credit_cards[i] = {
                    "bank": selected_bank,
                    "product": selected_product,
                    "issuer": selected_issuer
                }

    if st.button("➕ เพิ่มบัตร"):
        st.session_state.card_count += 1

    # ---------- Submit Button ----------
    if st.button("✅ สมัครสมาชิก"):
        if not username or not email or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
        elif password != confirm_password:
            st.error("❌ รหัสผ่านไม่ตรงกัน")
        else:
            st.success(f"✅ สมัครสำเร็จ! ยินดีต้อนรับคุณ {username} 🎉")
            st.write("📋 บัตรทั้งหมดที่คุณเพิ่ม:")
            st.write(pd.DataFrame(st.session_state.credit_cards))
            st.session_state.page = "login"
            st.rerun()

    if st.button("🔁 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ"):
        st.session_state.page = "login"
        st.rerun()
