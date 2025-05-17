import streamlit as st
from PIL import Image
from engine import RestaurantSelector, CardRecommender

# ✅ ข้อมูลร้านอาหาร (ใช้จาก HTML ที่ให้มา)
restaurant_cards = [
    {
        "name": "The Saucy Kitchen",
        "category": "อาหารคลีน/สลัด",
        "rating": 4.4,
        "reviews": 13,
        "image_url": "https://img.wongnai.com/p/624x0/2021/06/15/4b8d4e88d3f2406fa5a0f0d83773104a.jpg"
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
        "reviews": 17,
        "image_url": "https://img.wongnai.com/p/624x0/2023/11/11/4d7eaa83a0dc4607b2e6edec001f33c4.jpg"
    },
    {
        "name": "Starbucks Lotus's North",
        "category": "ร้านกาแฟ/ชา",
        "rating": 4.6,
        "reviews": 14,
        "image_url": "https://img.wongnai.com/p/624x0/2022/04/12/bdb04fdd1e18410f8d90ed73eaa5c3e2.jpg"
    },
    {
        "name": "MOS BURGER",
        "category": "เบอร์เกอร์",
        "rating": 4.5,
        "reviews": 13,
        "image_url": "https://img.wongnai.com/p/624x0/2019/12/17/a3a24300483f46298b728452dcdddb76.jpg"
    },
    {
        "name": "Starbucks Vichaiyut",
        "category": "ร้านกาแฟ/ชา",
        "rating": 5.0,
        "reviews": 6,
        "image_url": "https://img.wongnai.com/p/624x0/2021/07/21/0d2a92dbb1dc438cba02a334c0d50355.jpg"
    },
    {
        "name": "Starbucks Index Living",
        "category": "ร้านกาแฟ/ชา",
        "rating": 4.6,
        "reviews": 5,
        "image_url": "https://img.wongnai.com/p/624x0/2023/02/22/fcc32f22c4cf4c6489c7933df7e0dd88.jpg"
    }
]

# ✅ CSS สำหรับ card layout
st.markdown("""
    <style>
    .card-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        padding-top: 20px;
    }
    .card {
        border-radius: 16px;
        overflow: hidden;
        background: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
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

# ✅ โลโก้
col1, col2, col3 = st.columns((1, 0.5, 1))
with col2:
    st.image(Image.open("logo.png"))

# ✅ Header
st.subheader("⭐ ร้านแนะนำ")

# ✅ แสดง card layout
html = '<div class="card-grid">'
for r in restaurant_cards:
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
html += "</div>"

# ✅ เรนเดอร์ HTML
st.markdown(html, unsafe_allow_html=True)

