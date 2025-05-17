import streamlit as st
from PIL import Image
from engine import RestaurantSelector, CardRecommender

# 🧪 Mock function: Replace this with actual logic if using real data/images
def get_card_data():
    return [
        {
            "name": "Thong Grill Hide & Yakiniku",
            "category": "ชาบู/สุกี้ยากี้/หม้อไฟ",
            "rating": 4.8,
            "reviews": 5,
            "image_url": "https://via.placeholder.com/400x250.png?text=Thong+Grill"
        },
        {
            "name": "Burger King",
            "category": "ฟาสต์ฟู้ด/เบอร์เกอร์",
            "rating": 4.4,
            "reviews": 10,
            "image_url": "https://via.placeholder.com/400x250.png?text=Burger+King"
        },
        {
            "name": "Starbucks River City",
            "category": "ร้านกาแฟ/ชา",
            "rating": 4.6,
            "reviews": 14,
            "image_url": "https://via.placeholder.com/400x250.png?text=Starbucks"
        }
    ]

# 💅 Modern CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

html, body, input, button, select, div {
    font-family: 'Noto Sans Thai', sans-serif !important;
}
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    padding-top: 20px;
}
.card {
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    background: white;
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
    font-weight: 600;
    font-size: 18px;
    margin-bottom: 4px;
}
.card-category {
    font-size: 14px;
    color: #666;
    margin-bottom: 8px;
}
.card-rating {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 14px;
    color: #333;
}
.rating-badge {
    background-color: #d93025;
    color: white;
    font-weight: bold;
    padding: 2px 8px;
    border-radius: 12px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ✅ Logo only
col1, col2, col3 = st.columns((1, 0.5, 1))
with col2:
    st.image(Image.open("logo.png"))

# 🧠 Initialize backend
restaurant_selector = RestaurantSelector()
card_recommender = CardRecommender()

if "selected_restaurant" not in st.session_state:
    st.session_state["selected_restaurant"] = None
if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""

# 📥 Load restaurants
all_restaurants = restaurant_selector.all_restaurants
recommended_restaurants = restaurant_selector.recommend_restaurants()

# 🔍 Search and selection
st.subheader("🔍 ค้นหาร้านอาหาร")
search_query = st.text_input("พิมพ์ชื่อร้านอาหารที่ต้องการค้นหา", st.session_state["search_query"]).strip()

filtered_restaurants = all_restaurants if not search_query else [
    r for r in all_restaurants if search_query.lower() in r.lower()
]

selected_restaurant = st.selectbox("เลือกร้านอาหาร", ["เลือกจากรายการ"] + filtered_restaurants)

# ⭐ Show recommendation cards
if selected_restaurant == "เลือกจากรายการ":
    st.subheader("⭐ ร้านแนะนำ")
    html = '<div class="card-grid">'
    for r in get_card_data():
        html += f"""
        <div class="card">
            <img class="card-img" src="{r['image_url']}" alt="{r['name']}">
            <div class="card-body">
                <div class="card-title">{r['name']}</div>
                <div class="card-category">{r['category']}</div>
                <div class="card-rating">
                    <span class="rating-badge">{r['rating']} ⭐</span>
                    <span>{r['reviews']} รีวิว</span>
                </div>
            </div>
        </div>
        """
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# ✅ Show card recommendation
if selected_restaurant and selected_restaurant != "เลือกจากรายการ":
    st.session_state["selected_restaurant"] = selected_restaurant
    st.session_state["search_query"] = search_query
    st.success(f"✅ คุณเลือกร้าน {selected_restaurant}")

    st.subheader(f"💳 บัตรเครดิตที่แนะนำสำหรับ {selected_restaurant}")
    recommended_card = card_recommender.recommend_cards(selected_restaurant)

    if recommended_card:
        st.markdown(f"""
        <div class="card">
        <div class="card-body">
            <h4>🎉 {recommended_card.card_name} ({recommended_card.bank})</h4>
            <ul>
                <li>💰 <b>Cashback</b>: {recommended_card.cashback}%</li>
                <li>🎁 <b>Rewards</b>: {recommended_card.rewards} คะแนน/100 บาท</li>
                <li>🍽️ <b>Dining Discount</b>: {recommended_card.dining_discount}%</li>
                <li>✈️ <b>Travel Benefits</b>: {recommended_card.travel_benefit}</li>
            </ul>
        </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"❌ ไม่มีบัตรเครดิตแนะนำสำหรับร้าน {selected_restaurant}")

# 🔄 Reset button
if st.button("🔄 เลือกร้านใหม่"):
    st.session_state["selected_restaurant"] = None
    st.session_state["search_query"] = ""
    st.rerun()
