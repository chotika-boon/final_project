import streamlit as st
from PIL import Image
from engine import RestaurantSelector, CardRecommender

# ✅ Mock restaurant data (8 รายการ)
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
            "name": "The Saucy Kitchen",
            "category": "อาหารคลีน/สลัด",
            "rating": 4.4,
            "reviews": 13,
            "image_url": "https://img.wongnai.com/p/624x0/2021/06/15/4b8d4e88d3f2406fa5a0f0d83773104a.jpg"
        },
        {
            "name": "Burger King",
            "category": "ฟาสต์ฟู้ด/จานด่วน, เบอร์เกอร์",
            "rating": 4.4,
            "reviews": 10,
            "image_url": "https://img.wongnai.com/p/624x0/2020/05/08/0b4e2176d17c44d48d0ff22a2b5d167c.jpg"
        },
        {
            "name": "Starbucks River City",
            "category": "ร้านกาแฟ/ชา, เบเกอรี่/เค้ก, ร้านริมน้ำ",
            "rating": 4.4,
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

# ✅ CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

    html, body, input, button, select, div {
        font-family: 'Noto Sans Thai', sans-serif !important;
    }
    .card-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 24px;
        margin-top: 20px;
    }
    .card {
        border-radius: 16px;
        overflow: hidden;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
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
        padding: 14px 16px 16px;
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

# ✅ Display full-width layout
st.set_page_config(layout="wide")

# ✅ Logo
col1, col2, col3 = st.columns((1, 0.5, 1))
with col2:
    st.image(Image.open("logo.png"), width=100)

# ✅ Backend Setup
restaurant_selector = RestaurantSelector()
card_recommender = CardRecommender()

# ✅ Display Card Grid
st.subheader("⭐ ร้านแนะนำ")
html = '<div class="card-grid">'
for r in get_card_data():
    html += f'''
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
    '''
html += '</div>'
st.markdown(html, unsafe_allow_html=True)
