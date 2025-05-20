import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from engine import RestaurantSelector, CardRecommender
import json

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
        .card-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .card {
            width: 23%;
            border-radius: 16px;
            overflow: hidden;
            background: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
            cursor: pointer;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card img {
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
            font-size: 13px;
            color: #666;
            margin-bottom: 8px;
        }
        .card-rating {
            display: flex;
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

    st.subheader("⭐ ร้านแนะนำ")
    cards = get_card_data()
    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    for i, r in enumerate(cards):
        with st.container():
            btn_key = f"card_btn_{i}"
            if st.button(
                f'''
                <div class="card">
                    <img src="{r['image_url']}" />
                    <div class="card-body">
                        <div class="card-title">{r['name']}</div>
                        <div class="card-category">{r['category']}</div>
                        <div class="card-rating">
                            <span class="rating-badge">{r['rating']} ⭐</span>
                            <span>{r['reviews']} รีวิว</span>
                        </div>
                    </div>
                </div>
                ''',
                key=btn_key,
                use_container_width=True,
                help=r['name'],
            ):
                st.session_state.page = "detail"
                st.session_state.restaurant_detail = r
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# Hook into request body manually (simulate API-style read)
if st.runtime.exists():
    try:
        import streamlit.web.server.websocket_headers as wh
        import streamlit.web.server.server_util as su
        body = su.get_request_body()
        if body:
            payload = json.loads(body)
            if "selected_card" in payload:
                st.session_state["_selected_card_json"] = payload["selected_card"]
    except:
        pass
