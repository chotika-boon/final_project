
import streamlit as st
from PIL import Image
import importlib.util
import sys
import os
import uuid
import time
from google.cloud import bigquery

# Load engine.py dynamically
spec = importlib.util.spec_from_file_location("engine", os.path.join(os.path.dirname(__file__), "engine.py"))
engine = importlib.util.module_from_spec(spec)
sys.modules["engine"] = engine
spec.loader.exec_module(engine)

UserManager = engine.UserManager
BANKS = engine.BANKS
CARD_TYPES = engine.CARD_TYPES
LIFESTYLES = engine.LIFESTYLES
RestaurantSelector = engine.RestaurantSelector
CardRecommender = engine.CardRecommender

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
    html, body, input, button, select, div {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }
    .card-grid {
        display: flex;
        flex-wrap: nowrap;
        gap: 20px;
        margin-top: 20px;
        overflow-x: auto;
    }
    .card {
        flex: 0 0 23%;
        border-radius: 16px;
        overflow: hidden;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .card-img {
        width: 100%;
        height: 160px;
        object-fit: cover;
    }
    .card-body {
        padding: 12px 16px;
    }
    .card-title {
        font-weight: bold;
        font-size: 16px;
        margin-bottom: 4px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .card-category {
        font-size: 13px;
        color: #666;
        margin-bottom: 8px;
    }
    .card-rating {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 13px;
        color: #333;
    }
    .rating-badge {
        background-color: #d93025;
        color: white;
        font-weight: bold;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

user_manager = UserManager()
restaurant_selector = RestaurantSelector()
card_recommender = CardRecommender()

def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'show_register' not in st.session_state:
        st.session_state.show_register = False
    if "selected_restaurant" not in st.session_state:
        st.session_state["selected_restaurant"] = None
    if "search_query" not in st.session_state:
        st.session_state["search_query"] = ""

def modern_login_page():
    st.markdown("""
        <style>
            body {
                background: linear-gradient(to right, #00c6ff, #0072ff);
            }
            .login-container {
                max-width: 400px;
                margin: 0 auto;
                padding: 40px;
                background: white;
                border-radius: 16px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
                margin-top: 100px;
            }
            .login-title {
                font-size: 28px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
            .login-subtitle {
                font-size: 16px;
                color: #888;
                text-align: center;
                margin-bottom: 30px;
            }
            .login-button {
                width: 100%;
                padding: 10px;
                background: linear-gradient(to right, #00c6ff, #0072ff);
                color: white;
                border: none;
                border-radius: 8px;
                font-weight: bold;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("""<div class='login-container'>""", unsafe_allow_html=True)
        st.markdown("""<div class='login-title'>Sign Into<br>Your Account</div>""", unsafe_allow_html=True)
        username = st.text_input("Email / Company ID", placeholder="example@email.com")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        remember = st.checkbox("Remember Me")
        login = st.button("Sign In", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if login:
            if username == "admin" and password == "1234":
                st.success("Login Success! ✅")
            else:
                st.error("Login Failed ❌")


def register_page():
    st.markdown("<h2 style='text-align: center;'>ลงทะเบียน</h2>", unsafe_allow_html=True)

    with st.form("register_form"):
        st.markdown("<div class='login-box'>", unsafe_allow_html=True)
        username = st.text_input("ชื่อผู้ใช้", key="register_username", placeholder="เบอร์โทร/อีเมล")
        password = st.text_input("รหัสผ่าน", type="password", key="register_password", placeholder="รหัสผ่าน")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password", key="confirm_password", placeholder="ยืนยันรหัสผ่าน")
        bank = st.selectbox("ธนาคารที่ถือบัตรเครดิต", BANKS)
        card_type = st.selectbox("ประเภทบัตรเครดิตที่ถือ", CARD_TYPES)
        lifestyle = st.selectbox("ไลฟ์สไตล์ของคุณ", LIFESTYLES)
        submit_btn = st.form_submit_button("ลงทะเบียน", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center;'>หรือ</p>", unsafe_allow_html=True)

    col_facebook, col_line, col_google = st.columns(3)
    with col_facebook:
        st.button("เข้าสู่ระบบด้วย Facebook", use_container_width=True)
    with col_line:
        st.button("เข้าสู่ระบบด้วย LINE", use_container_width=True)
    with col_google:
        st.button("เข้าสู่ระบบด้วย Google", use_container_width=True)

    if submit_btn:
        if password != confirm_password:
            st.error("รหัสผ่านไม่ตรงกัน")
        else:
            success, msg = user_manager.register_user(username, password, bank, card_type, lifestyle)
            if success:
                try:
                    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "coolkid-460014-e7e1c656d653.json"
                    client = bigquery.Client()
                    table_id = "coolkid-460014.card_scoring.users"
                    row = [{
                        "customer_id": str(uuid.uuid4()),
                        "username": username,
                        "password": password,
                        "bank": bank,
                        "credit_name": "",
                        "card_type": card_type
                    }]
                    errors = client.insert_rows_json(table_id, row)
                    if errors:
                        st.warning(f"BigQuery insert error: {errors}")
                    else:
                        st.success("✅ บันทึกข้อมูลลง BigQuery สำเร็จ")
                except Exception as e:
                    st.warning(f"🔥 BigQuery error: {str(e)}")

                time.sleep(2)
                st.session_state.show_register = False
                st.rerun()
            else:
                st.error(msg)

def restaurant_app():
    col1, col2, col3 = st.columns((1, 0.5, 1))
    with col2:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=100)

    st.subheader("🔍 ค้นหาร้านอาหาร")
    search_query = st.text_input("พิมพ์ชื่อร้านอาหาร", st.session_state["search_query"]).strip()
    all_restaurants = restaurant_selector.all_restaurants
    filtered = all_restaurants if not search_query else [r for r in all_restaurants if search_query.lower() in r.lower()]
    selected = st.selectbox("เลือกร้านอาหาร", ["เลือกจากรายการ"] + filtered)

    if selected == "เลือกจากรายการ":
        st.subheader("⭐ ร้านแนะนำ")
        html = '<div class="card-grid">'
        for r in restaurant_selector.get_sample_data():
            html += f"""
            <div class="card">
                <img class="card-img" src="{r['image_url']}">
                <div class="card-body">
                    <div class="card-title">{r['name']}</div>
                    <div class="card-category">{r['category']}</div>
                    <div class="card-rating">
                        <span class="rating-badge">{r['rating']} ⭐</span>
                        <span>{r['reviews']} รีวิว</span>
                    </div>
                </div>
            </div>"""
        html += '</div>'
        st.markdown(html, unsafe_allow_html=True)

    if selected and selected != "เลือกจากรายการ":
        st.session_state["selected_restaurant"] = selected
        st.session_state["search_query"] = search_query
        st.success(f"✅ คุณเลือกร้าน {selected}")
        st.subheader(f"💳 บัตรเครดิตที่แนะนำสำหรับ {selected}")
        recommended = card_recommender.recommend_cards(selected)
        if recommended:
            st.markdown(f"""
            <div class="card">
                <div class="card-body">
                    <h4>🎉 {recommended.card_name} ({recommended.bank})</h4>
                    <ul>
                        <li>💰 <b>Cashback</b>: {recommended.cashback}%</li>
                        <li>🎁 <b>Rewards</b>: {recommended.rewards} คะแนน/100 บาท</li>
                        <li>🍽️ <b>Dining Discount</b>: {recommended.dining_discount}%</li>
                        <li>✈️ <b>Travel Benefits</b>: {recommended.travel_benefit}</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("❌ ไม่มีบัตรเครดิตแนะนำสำหรับร้านนี้")

    if st.button("🔄 เลือกร้านใหม่"):
        st.session_state["selected_restaurant"] = None
        st.session_state["search_query"] = ""
        st.rerun()

    st.markdown("---")
    user_data = user_manager.get_user_data(st.session_state.username)
    st.caption(f"คุณเข้าสู่ระบบในชื่อ: {st.session_state.username} ({user_data['bank']} - {user_data['card_type']}, ไลฟ์สไตล์: {user_data['lifestyle']})")
    if st.button("🚪 ออกจากระบบ"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

def main():
    init_session_state()
    if not st.session_state.logged_in:
        if st.session_state.show_register:
            register_page()
        else:
            login_page()
    else:
        restaurant_app()

if __name__ == "__main__":
    main()
