import streamlit as st
from PIL import Image
import streamlit as st

import streamlit as st
from engine import RestaurantSelector, CardRecommender

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, input, button, select, div {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }

    /* โลโก้ตรงกลาง */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: -10px;
    }

    .logo {
        width: 100px;
        max-width: 100%;
    }

    /* ข้อความหลัก "ไปไหนดี" */
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-top: -5px;
    }

    /* เมนูตัวเลือก */
    .menu-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 10px;
    }

    .menu-item {
        display: flex;
        align-items: center;
        font-size: 18px;
        font-weight: 500;
        cursor: pointer;
        color: #333;
        padding-bottom: 5px;
    }

    .menu-item.active {
        font-weight: bold;
        border-bottom: 3px solid black;
    }

    /* ช่องค้นหา */
    .search-container {
        display: flex;
        align-items: center;
        background: white;
        padding: 12px;
        border-radius: 50px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        max-width: 600px;
        width: 100%;
        margin: 20px auto;
        border: 1px solid #ddd;
    }

    .search-icon {
        margin-left: 10px;
        font-size: 20px;
        color: #777;
    }

    .search-input {
        flex: 1;
        background: transparent;
        border: none;
        outline: none;
        font-size: 18px;
        padding: 10px;
    }

    .search-button {
        background: #00af87;
        color: white;
        padding: 10px 24px;
        border-radius: 25px;
        border: none;
        cursor: pointer;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
    }

    .search-button:hover {
        background: #008a6e;
    }

    </style>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns((1, 0.5, 1))
with col2:
    st.image(Image.open("logo.png"))

# 📌 เมนูตัวเลือก
st.markdown(
    """
    <div class="menu-container">
        <div class="menu-item active">🏠 ค้นหาทั้งหมด</div>
        <div class="menu-item">🛏️ โรงแรม</div>
        <div class="menu-item">📷 กิจกรรมน่าสนใจ</div>
        <div class="menu-item">🍽️ ร้านอาหาร</div>
        <div class="menu-item">✈️ เที่ยวบิน</div>
    </div>
    """,
    unsafe_allow_html=True
)

# สร้าง instance ของ Backend
restaurant_selector = RestaurantSelector()
card_recommender = CardRecommender()

# ใช้ Session State เก็บสถานะ
if "selected_restaurant" not in st.session_state:
    st.session_state["selected_restaurant"] = None
if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""

# ✅ ดึงร้านอาหารทั้งหมด
all_restaurants = restaurant_selector.all_restaurants
recommended_restaurants = restaurant_selector.recommend_restaurants()  # ✅ 5 ร้านแรก

# ✅ UI ค้นหาร้านค้า
st.subheader("🔍 ค้นหาร้านอาหาร")
search_query = st.text_input("พิมพ์ชื่อร้านอาหารที่ต้องการค้นหา", st.session_state["search_query"]).strip()

# ✅ ถ้ายังไม่มีการค้นหา ให้แสดงทุกตัวเลือกใน `selectbox`
filtered_restaurants = all_restaurants if not search_query else [
    r for r in all_restaurants if search_query.lower() in r.lower()
]

# ✅ แสดง `selectbox` ที่มีทุกร้าน
selected_restaurant = st.selectbox("เลือกร้านอาหาร", ["เลือกจากรายการ"] + filtered_restaurants)

if selected_restaurant and selected_restaurant == "เลือกจากรายการ":
# ✅ แสดงผลเฉพาะ 5 ร้านแรกที่แนะนำ
    st.subheader("⭐ ร้านแนะนำ")
    for idx, restaurant in enumerate(recommended_restaurants, start=1):
        st.write(f"**{idx}. {restaurant}**")  # ✅ แสดงเฉพาะ 5 ร้านแรก

# ✅ บันทึกค่าร้านที่เลือก
if selected_restaurant and selected_restaurant != "เลือกจากรายการ":
    st.session_state["selected_restaurant"] = selected_restaurant
    st.session_state["search_query"] = search_query  # ✅ บันทึกค่าค้นหา
    st.success(f"✅ คุณเลือกร้าน {selected_restaurant}")

    # ✅ **แสดงบัตรเครดิต สำหรับร้านที่เลือก**
    st.subheader(f"💳 บัตรเครดิตที่แนะนำสำหรับ {selected_restaurant}")
    recommended_card = card_recommender.recommend_cards(selected_restaurant)

    if recommended_card:
        st.markdown(f"""
        **🎉 บัตรเครดิตที่แนะนำสำหรับร้าน {selected_restaurant}**  
        - 💳 **{recommended_card.card_name}** ({recommended_card.bank})  
        - 💰 **Cashback**: {recommended_card.cashback}%  
        - 🎁 **Rewards**: {recommended_card.rewards} points per 100 THB  
        - 🍽️ **Dining Discount**: {recommended_card.dining_discount}%  
        - ✈️ **Travel Benefits**: {recommended_card.travel_benefit}  
        """)
    else:
        st.warning(f"❌ ไม่มีบัตรเครดิตแนะนำสำหรับร้าน {selected_restaurant}")

# ✅ ปุ่ม Reset ค้นหาและเลือกใหม่
if st.button("🔄 เลือกร้านใหม่"):
    st.session_state["selected_restaurant"] = None
    st.session_state["search_query"] = ""  # ✅ รีเซ็ตช่องค้นหา
    st.rerun()  # รีเฟรชหน้าใหม่
