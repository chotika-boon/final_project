import streamlit as st
from PIL import Image
from engine import RestaurantSelector, CardRecommender

def get_card_data():
    return [
        {
            "name": "Thong Grill Hide & Yakiniku",
            "category": "ชาบู/สุกี้ยากี้/หม้อไฟ",
            "rating": 4.8,
            "reviews": 5,
            "image_url": "https://img.wongnai.com/p/624x0/2025/03/28/7b4e368494c94cee80dfc99f0a7704dc.jpg",
            "description": "เปิดถึง 23:30 | ที่จอดรถ | เดลิเวอรี"
        },
        {
            "name": "Burger King",
            "category": "เบอร์เกอร์",
            "rating": 4.4,
            "reviews": 10,
            "image_url": "https://img.wongnai.com/p/624x0/2025/04/11/e6b18c24a9914034b14666aba59ecdfd.jpg",
            "description": "ฟาสต์ฟู้ดในตำนาน พร้อมโปรตลอดปี"
        },
        {
            "name": "Starbucks River City",
            "category": "ร้านกาแฟ/ชา",
            "rating": 4.6,
            "reviews": 14,
            "image_url": "https://img.wongnai.com/p/624x0/2024/04/17/1e4ec5eae8ad4e2cbcb79fd2753e16f9.jpg",
            "description": "ร้านกาแฟวิวแม่น้ำเจ้าพระยา"
        },
        {
            "name": "MOS BURGER",
            "category": "เบอร์เกอร์",
            "rating": 4.5,
            "reviews": 13,
            "image_url": "https://img.wongnai.com/p/624x0/2024/09/10/44f2586e3bd84950b34fd074b82e7a85.jpg",
            "description": "เบอร์เกอร์ญี่ปุ่นแท้ ๆ จากโตเกียว"
        }
    ]

def show_home():
    st.markdown("""
        <style>
        .card-title { font-weight: bold; font-size: 16px; margin-top: 10px; }
        .card-category { font-size: 13px; color: #666; margin-bottom: 4px; }
        .card-rating { font-size: 13px; color: #333; margin: 4px 0; }
        .rating-badge { background-color: #d93025; color: white; font-weight: bold; padding: 2px 6px; border-radius: 12px; font-size: 12px; }
        .card-box { background: white; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); padding: 12px; height: 100%; display: flex; flex-direction: column; justify-content: space-between; }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns((1, 0.5, 1))
    with col2:
        st.image(Image.open("logo.png"), width=100)

    restaurant_selector = RestaurantSelector()
    card_recommender = CardRecommender()

    if "selected_restaurant" not in st.session_state:
        st.session_state["selected_restaurant"] = None
    if "search_query" not in st.session_state:
        st.session_state["search_query"] = ""

    st.subheader("🔍 ค้นหาร้านอาหาร")
    search_query = st.text_input("พิมพ์ชื่อร้านค่ะ", st.session_state["search_query"]).strip()
    all_restaurants = restaurant_selector.all_restaurants
    filtered_restaurants = all_restaurants if not search_query else [
        r for r in all_restaurants if search_query.lower() in r.lower()
    ]
    selected_restaurant = st.selectbox("เลือกร้านอาหาร", ["เลือกจากรายการ"] + filtered_restaurants)

    if selected_restaurant == "เลือกจากรายการ":
        st.subheader("⭐ ร้านแนะนำ")
        cards = get_card_data()

        for i in range(0, len(cards), 4):
            cols = st.columns(4)
            for j, r in enumerate(cards[i:i+4]):
                with cols[j]:
                    with st.container():
                        st.image(r['image_url'], use_container_width=True)
                        st.markdown(f"<div class='card-box'>", unsafe_allow_html=True)
                        st.markdown(f"<div class='card-title'>{r['name']}</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='card-category'>{r['category']}</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='card-rating'><span class='rating-badge'>{r['rating']} ⭐</span> {r['reviews']} รีวิว</div>", unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                        if st.button("ดูรายละเอียด", key=f"card_{i+j}"):
                            st.session_state.page = "detail"
                            st.session_state.restaurant_detail = r
                            st.rerun()

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
            st.warning("❌ ไม่มีบัตรเครดิตแนะนำสำหรับร้านนี้")

    if st.button("🔄 เลือกร้านใหม่"):
        st.session_state["selected_restaurant"] = None
        st.session_state["search_query"] = ""
        st.rerun()
