import streamlit as st
import pandas as pd

def show_register():
    # --------- โหลดข้อมูล ---------
    df = pd.read_csv("credit_card.csv")

    # --------- CSS สไตล์ MODERN ---------
    st.markdown("""
    <style>
        .register-box {
            max-width: 500px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }

        .register-title {
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }

        .input-label {
            font-size: 16px;
            margin-top: 1rem;
        }

        .icon {
            font-size: 20px;
            margin-right: 8px;
        }

        .form-footer {
            margin-top: 1.5rem;
            text-align: center;
        }

        .divider {
            text-align: center;
            margin: 1.5rem 0;
            color: #888;
        }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='register-box'>", unsafe_allow_html=True)
    st.markdown("<div class='register-title'>📝 สมัครสมาชิก</div>", unsafe_allow_html=True)

    # --------- ฟอร์ม (ชื่อผู้ใช้/รหัสผ่าน) ---------
    with st.form("user_register_form"):
        st.markdown("#### 👤 ข้อมูลบัญชีผู้ใช้")

        username = st.text_input("ชื่อผู้ใช้")
        password = st.text_input("รหัสผ่าน", type="password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

        submitted = st.form_submit_button("สมัครสมาชิก")

        if submitted:
            if password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จแล้ว!")
                st.session_state.page = "login"
                st.rerun()

    # --------- Divider ---------
    st.markdown("<div class='divider'>หรือเลือกข้อมูลบัตร</div>", unsafe_allow_html=True)

    # --------- Dropdown เชื่อมกัน 3 ชั้น ---------
    st.markdown("#### 💳 ข้อมูลบัตรเครดิต")

    bank_options = sorted(df["ธนาคาร"].dropna().unique())
    selected_bank = st.selectbox("🏦 เลือกธนาคาร", bank_options)

    product_df = df[df["ธนาคาร"] == selected_bank]
    product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
    selected_product = st.selectbox("💳 เลือกชื่อบัตร", product_options)

    issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
    issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
    selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", issuer_options)

    # --------- ปุ่มกลับเข้าสู่ระบบ ---------
    st.markdown("""
        <div class='form-footer'>
            <a href="#" onclick="window.location.reload();">
                <button style="background: none; border: none; color: #0084ff; font-size: 15px; cursor: pointer;">
                    🔙 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # ปิด box
import streamlit as st
import pandas as pd

def show_register():
    # --------- โหลดข้อมูล ---------
    df = pd.read_csv("credit_card.csv")

    # --------- CSS สไตล์ MODERN ---------
    st.markdown("""
    <style>
        .register-box {
            max-width: 500px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }

        .register-title {
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }

        .input-label {
            font-size: 16px;
            margin-top: 1rem;
        }

        .icon {
            font-size: 20px;
            margin-right: 8px;
        }

        .form-footer {
            margin-top: 1.5rem;
            text-align: center;
        }

        .divider {
            text-align: center;
            margin: 1.5rem 0;
            color: #888;
        }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='register-box'>", unsafe_allow_html=True)
    st.markdown("<div class='register-title'>📝 สมัครสมาชิก</div>", unsafe_allow_html=True)

    # --------- ฟอร์ม (ชื่อผู้ใช้/รหัสผ่าน) ---------
    with st.form("user_register_form"):
        st.markdown("#### 👤 ข้อมูลบัญชีผู้ใช้")

        username = st.text_input("ชื่อผู้ใช้")
        password = st.text_input("รหัสผ่าน", type="password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

        submitted = st.form_submit_button("สมัครสมาชิก")

        if submitted:
            if password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จแล้ว!")
                st.session_state.page = "login"
                st.rerun()

    # --------- Divider ---------
    st.markdown("<div class='divider'>หรือเลือกข้อมูลบัตร</div>", unsafe_allow_html=True)

    # --------- Dropdown เชื่อมกัน 3 ชั้น ---------
    st.markdown("#### 💳 ข้อมูลบัตรเครดิต")

    bank_options = sorted(df["ธนาคาร"].dropna().unique())
    selected_bank = st.selectbox("🏦 เลือกธนาคาร", bank_options)

    product_df = df[df["ธนาคาร"] == selected_bank]
    product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
    selected_product = st.selectbox("💳 เลือกชื่อบัตร", product_options)

    issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
    issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
    selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", issuer_options)

    # --------- ปุ่มกลับเข้าสู่ระบบ ---------
    st.markdown("""
        <div class='form-footer'>
            <a href="#" onclick="window.location.reload();">
                <button style="background: none; border: none; color: #0084ff; font-size: 15px; cursor: pointer;">
                    🔙 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # ปิด box
import streamlit as st
import pandas as pd

def show_register():
    # --------- โหลดข้อมูล ---------
    df = pd.read_csv("credit_card.csv")

    # --------- CSS สไตล์ MODERN ---------
    st.markdown("""
    <style>
        .register-box {
            max-width: 500px;
            margin: 2rem auto;
            padding: 2rem;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }

        .register-title {
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }

        .input-label {
            font-size: 16px;
            margin-top: 1rem;
        }

        .icon {
            font-size: 20px;
            margin-right: 8px;
        }

        .form-footer {
            margin-top: 1.5rem;
            text-align: center;
        }

        .divider {
            text-align: center;
            margin: 1.5rem 0;
            color: #888;
        }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='register-box'>", unsafe_allow_html=True)
    st.markdown("<div class='register-title'>📝 สมัครสมาชิก</div>", unsafe_allow_html=True)

    # --------- ฟอร์ม (ชื่อผู้ใช้/รหัสผ่าน) ---------
    with st.form("user_register_form"):
        st.markdown("#### 👤 ข้อมูลบัญชีผู้ใช้")

        username = st.text_input("ชื่อผู้ใช้")
        password = st.text_input("รหัสผ่าน", type="password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")

        submitted = st.form_submit_button("สมัครสมาชิก")

        if submitted:
            if password != confirm_password:
                st.error("❌ รหัสผ่านไม่ตรงกัน")
            else:
                st.success("✅ สมัครสำเร็จแล้ว!")
                st.session_state.page = "login"
                st.rerun()

    # --------- Divider ---------
    st.markdown("<div class='divider'>หรือเลือกข้อมูลบัตร</div>", unsafe_allow_html=True)

    # --------- Dropdown เชื่อมกัน 3 ชั้น ---------
    st.markdown("#### 💳 ข้อมูลบัตรเครดิต")

    bank_options = sorted(df["ธนาคาร"].dropna().unique())
    selected_bank = st.selectbox("🏦 เลือกธนาคาร", bank_options)

    product_df = df[df["ธนาคาร"] == selected_bank]
    product_options = sorted(product_df["ผลิตภัณฑ์/ชื่อบัตร"].dropna().unique())
    selected_product = st.selectbox("💳 เลือกชื่อบัตร", product_options)

    issuer_df = product_df[product_df["ผลิตภัณฑ์/ชื่อบัตร"] == selected_product]
    issuer_options = sorted(issuer_df["ผู้ออกบัตร"].dropna().unique())
    selected_issuer = st.selectbox("🏢 เลือกผู้ออกบัตร", issuer_options)

    # --------- ปุ่มกลับเข้าสู่ระบบ ---------
    st.markdown("""
        <div class='form-footer'>
            <a href="#" onclick="window.location.reload();">
                <button style="background: none; border: none; color: #0084ff; font-size: 15px; cursor: pointer;">
                    🔙 มีบัญชีอยู่แล้ว? เข้าสู่ระบบ
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # ปิด box
