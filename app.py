from PIL import Image
import streamlit as st
from engine import RestaurantSelector, CardRecommender

# Custom modern style
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, input, button, select, div {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }

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

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #00af87;
        margin-bottom: 10px;
    }

    .menu-container {
        display: flex;
        justify-content: center;
        gap: 25px;
        margin: 20px 0;
        flex-wrap: wrap;
    }

    .menu-item {
        font-size: 20px;
        font-weight: 500;
        color: #555;
        padding: 8px 12px;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .menu-item:hover {
        background-color: #f0f0f0;
    }

    .menu-item.active {
        font-weight: 700;
        color: white;
        background-color: #00af87;
        border-radius: 20px;
        padding: 8px 16px;
    }

    .card {
        padding: 20px;
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }

    .card:hover {
        transform: translateY(-4px);
    }

    .search-container {
        display: flex;
        align-items: center;
        justify-content: center;
        background: white;
        padding: 12px;
        border-radius: 50px;
        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        max-width: 600px;
        margin: 20px auto;
        border: 1px solid #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo and title
col1, col2, col3 = st.columns((1, 0.5, 1))
with col2:
    st.image(Image.open("logo.png"))
st.markdown("<div class='main-title'>ไปไหนดี?</div>", unsafe_allow_html=True)

# Menu
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

# Create instance
restaurant_selector = RestaurantSelector()
card_recommender = CardRecommender()

# Use session state
if "selected_restaurant" not in st.session_state:
    st.session_state["selected_restaurant"] = None
if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""

# Load data
all_restaurants = restaurant_selector.all_restaurants
recommended_restaurants = restaurant_selector.recommend_restaurants()

# Search UI
st.subheader("🔍 ค้นหาร้านอาหาร")
search_query = st.text_input("พิมพ์ชื่อร้านอาหารที่ต้องการค้นหา", st.session_state["search_query"]).strip()

# Filtered list
filtered_restaurants = all_restaurants if not search_query else [
    r for r in all_restaurants if search_query.lower() in r.lower()
]

# Restaurant selector
selected_restaurant = st.selectbox("เลือกร้านอาหาร", ["เลือกจากรายการ"] + filtered_restaurants)

# If no selection, show recommended
if selected_restaurant == "เลือกจากรายการ":
    st.markdown("## ⭐ ร้านแนะนำ")
    cols = st.columns(2)
    for idx, restaurant in enumerate(recommended_restaurants):
        with cols[idx % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <h4>🍽️ {restaurant}</h4>
                    <p>รีวิวดี / สิทธิประโยชน์มากมาย</p>
                </div>
                """, unsafe_allow_html=True
            )

# If selected, show card
if selected_restaurant and selected_restaurant != "เลือกจากรายการ":
    st.session_state["selected_restaurant"] = selected_restaurant
    st.session_state["search_query"] = search_query
    st.success(f"✅ คุณเลือกร้าน {selected_restaurant}")

    st.subheader(f"💳 บัตรเครดิตที่แนะนำสำหรับ {selected_restaurant}")
    recommended_card = card_recommender.recommend_cards(selected_restaurant)

    if recommended_card:
        st.markdown(f"""
        <div class="card">
        <h4>🎉 {recommended_card.card_name} ({recommended_card.bank})</h4>
        <ul>
            <li>💰 <b>Cashback</b>: {recommended_card.cashback}%</li>
            <li>🎁 <b>Rewards</b>: {recommended_card.rewards} points / 100 THB</li>
            <li>🍽️ <b>Dining Discount</b>: {recommended_card.dining_discount}%</li>
            <li>✈️ <b>Travel Benefits</b>: {recommended_card.travel_benefit}</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"❌ ไม่มีบัตรเครดิตแนะนำสำหรับร้าน {selected_restaurant}")

# Reset
if st.button("🔄 เลือกร้านใหม่"):
    st.session_state["selected_restaurant"] = None
    st.session_state["search_query"] = ""
    st.rerun()
