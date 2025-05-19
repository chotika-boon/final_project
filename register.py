import streamlit as st
import pandas as pd

def show_register():
    df = pd.read_csv("credit_card.csv")

    # -------------- CSS Modern UI ----------------
    st.markdown("""
    <style>
        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2.5rem;
            background-color: #ffffff;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.06);
            font-family: 'Noto Sans Thai', sans-serif;
        }
        .section-title {
            font-size: 20px;
            font-weight: 600;
            margin: 1.5rem 0 1rem 0;
            color: #333;
        }
        .stTextInput input, .stSelectbox div div {
            font-size: 16px !important;
            padding: 10px !important;
        }
        .stButton > button {
            font-size: 16px;
            padding: 10px 16px;
            border-radius: 8px;
            background-color: #0084ff;
            color: white;
            font-weight: bold;
            width: 100%;
            margin-top: 1.5rem;
        }
        .login-link {
            text-align: center;
            margin-top: 1.5rem;
            color: #666;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("## 📝 สมัครสมาชิก", unsafe_allow_html=True)

    # -------------- Section: ข้อมูลผู้ใช้ --------------
    st.markdown("<div class='section-title'>👤 ข้อมูลบัญชีผู้ใช้</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("ชื่อผู้ใช้", value=st.session_state.get("username", ""))
    with col2:
        email = st.text_input("อีเมล", value=st.session_state.get("email", ""))

    col1, col2 = st.columns(2)
    with col1:
        password = st.text_input("รหัสผ่าน", type="password")
    with col2:
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

    # เก็บค่า
    st.session_state.username = username
    st.session_state.email = email

    # -------------- Section: บัตรเครดิต --------------
    st.markdown("<div class='section-title'>💳 ข้อมูลบัตรเครดิต</div>", unsafe_allow_html=True)

    # 1️⃣ ธนาคาร
    banks = sorted(df["ธนาคาร"].dropna().unique())
    default_bank = st.session_state.get("selected_bank", banks[0])
    selected_bank = st.selectbox("🏦 เลือกธนาคาร", banks, index=banks.index(default_bank))
    st.session_state.selected_bank = selected_bank

    # 2️⃣ ชื่อบัตร
    filtered_df = df[df["ธนาคาร"] == selected_bank]
    products = sorted(filtered_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
    default_product = st.session_state.get("selected_product", products[0])
    selected_product = st.selectbox("💳 เลือกชื่อบัตร", products, index=products.index(default_product))
    st.session_state.selected_product = selected_product

    # 3️⃣ ผู้ออกบัตร
    issuer_df = filtered_df[filtered_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
    issuers = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
    default_issuer = st.session_state.get("selected_issuer", issuers[0])
    selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", issuers, index=issuers.index(default_issuer))
    st.session_state.selected_issuer = selected_issuer

    # -------------- ปุ่มสมัครสมาชิก --------------
    if st.button("✅ สมัครสมาชิก"):
        if not username or not email or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
        elif password != confirm_password:
            st.error("❌ รหัสผ่านไม่ตรงกัน")
        else:
            st.success(f"✅ สมัครสำเร็จ! ยินดีต้อนรับคุณ {username} 🎉")
            st.session_state.page = "login"
            st.rerun()

    # -------------- ลิงก์เข้าสู่ระบบ --------------
    st.markdown("""
        <div class="login-link">
            มีบัญชีอยู่แล้ว? <a href="#" onclick="window.location.reload();">เข้าสู่ระบบ</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # ปิด container
