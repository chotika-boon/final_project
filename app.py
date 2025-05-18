import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# Mock data
def get_card_data():
    return [
        {
            "name": "Thong Grill Hide & Yakiniku",
            "category": "ชาบู/สุกี้ยากี้/หม้อไฟ",
            "rating": 4.8,
            "reviews": 5,
            "image_url": "https://img.wongnai.com/p/624x0/2025/03/28/7b4e368494c94cee80dfc99f0a7704dc.jpg"
        },
        {
            "name": "Burger King",
            "category": "เบอร์เกอร์",
            "rating": 4.4,
            "reviews": 10,
            "image_url": "https://img.wongnai.com/p/624x0/2020/05/08/0b4e2176d17c44d48d0ff22a2b5d167c.jpg"
        },
        {
            "name": "Starbucks River City",
            "category": "ร้านกาแฟ/ชา",
            "rating": 4.6,
            "reviews": 14,
            "image_url": "https://img.wongnai.com/p/624x0/2023/11/11/4d7eaa83a0dc4607b2e6edec001f33c4.jpg"
        },
        {
            "name": "MOS BURGER",
            "category": "เบอร์เกอร์",
            "rating": 4.5,
            "reviews": 13,
            "image_url": "https://img.wongnai.com/p/624x0/2019/12/17/a3a24300483f46298b728452dcdddb76.jpg"
        }
    ]

# CSS
st.markdown("""
    <style>
    .card-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin-top: 20px;
    }
    .card {
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        overflow: hidden;
        transition: transform 0.2s ease;
    }
    .card:hover { transform: translateY(-5px); }
    .card img {
        width: 100%;
        height: 160px;
        object-fit: cover;
    }
    .card-body { padding: 10px 16px; }
    .card-title { font-weight: bold; font-size: 16px; margin-bottom: 4px; }
    .card-category { font-size: 13px; color: #666; margin-bottom: 8px; }
    .card-rating {
        display: flex;
        align-items: center;
        font-size: 13px;
        color: #333;
        gap: 6px;
    }
    .rating-badge {
        background-color: #e53935;
        color: white;
        padding: 2px 6px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Logo
col1, col2, col3 = st.columns((1, 0.5, 1))
with col2:
    st.image("logo.png", width=90)

# Search
st.subheader("🔍 ค้นหาร้านอาหาร")
query = st.text_input("พิมพ์ชื่อร้าน").strip()
restaurants = get_card_data()
if query:
    restaurants = [r for r in restaurants if query.lower() in r["name"].lower()]

# Show cards
st.subheader("⭐ ร้านแนะนำ")
st.markdown('<div class="card-grid">', unsafe_allow_html=True)
for r in restaurants:
    link = f"/RestaurantDetail?name={r['name']}"
    st.markdown(f"""
    <a href="{link}" style="text-decoration: none; color: inherit;">
        <div class="card">
            <img src="{r['image_url']}" alt="{r['name']}">
            <div class="card-body">
                <div class="card-title">{r['name']}</div>
                <div class="card-category">{r['category']}</div>
                <div class="card-rating">
                    <span class="rating-badge">{r['rating']} ⭐</span>
                    <span>{r['reviews']} รีวิว</span>
                </div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
