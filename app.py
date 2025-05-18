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

def login_page():
    st.title("เข้าสู่ระบบ")
    with st.form("login_form"):
        username = st.text_input("ชื่อผู้ใช้", key="login_username")
        password = st.text_input("รหัสผ่าน", type="password", key="login_password")
        col1, col2 = st.columns(2)
        login_btn = col1.form_submit_button("เข้าสู่ระบบ")
        register_btn = col2.form_submit_button("ลงทะเบียน")

    if login_btn:
        if user_manager.authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("เข้าสู่ระบบสำเร็จ!")
            st.rerun()
        else:
            st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    if register_btn:
        st.session_state.show_register = True
        st.rerun()

def register_page():
    st.title("ลงทะเบียน")
    with st.form("register_form"):
        username = st.text_input("ชื่อผู้ใช้", key="register_username")
        password = st.text_input("รหัสผ่าน", type="password", key="register_password")
        confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password", key="confirm_password")
        bank = st.selectbox("ธนาคาร", BANKS)
        card_type = st.selectbox("ประเภทบัตร", CARD_TYPES)
        lifestyle = st.selectbox("ไลฟ์สไตล์", LIFESTYLES)
        col1, col2 = st.columns(2)
        submit_btn = col1.form_submit_button("ลงทะเบียน")
        back_btn = col2.form_submit_button("กลับ")

    if submit_btn:
        st.write("🟢 Form Submitted")
        if password != confirm_password:
            st.error("รหัสผ่านไม่ตรงกัน")
        else:
            success, msg = user_manager.register_user(username, password, bank, card_type, lifestyle)
            st.write("✅ Register Function:", success)
            if success:
                try:
                    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
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
                    st.write("🚀 Data to insert:", row)
                    errors = client.insert_rows_json(table_id, row)
                    st.write("📥 Insert result:", errors)
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
    if back_btn:
        st.session_state.show_register = False
        st.rerun()

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
