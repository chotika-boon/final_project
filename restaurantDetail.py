import streamlit as st

st.set_page_config(layout="centered")

# Query param
params = st.query_params
name = params.get("name", "")

# Mock detail
detail_map = {
    "Thong Grill Hide & Yakiniku": {
        "image": "https://img.wongnai.com/p/624x0/2025/03/28/7b4e368494c94cee80dfc99f0a7704dc.jpg",
        "category": "ชาบู/สุกี้ยากี้/หม้อไฟ",
        "location": "สุขุมวิท 53, กรุงเทพ",
        "open": "17:00 - 23:30"
    },
    "Burger King": {
        "image": "https://img.wongnai.com/p/624x0/2020/05/08/0b4e2176d17c44d48d0ff22a2b5d167c.jpg",
        "category": "เบอร์เกอร์",
        "location": "Terminal 21, อโศก",
        "open": "10:00 - 21:00"
    },
    "Starbucks River City": {
        "image": "https://img.wongnai.com/p/624x0/2023/11/11/4d7eaa83a0dc4607b2e6edec001f33c4.jpg",
        "category": "ร้านกาแฟ/ชา",
        "location": "River City Bangkok",
        "open": "07:00 - 20:00"
    },
    "MOS BURGER": {
        "image": "https://img.wongnai.com/p/624x0/2019/12/17/a3a24300483f46298b728452dcdddb76.jpg",
        "category": "เบอร์เกอร์",
        "location": "Siam Paragon",
        "open": "10:30 - 22:00"
    }
}

# Render page
if name and name in detail_map:
    info = detail_map[name]
    st.image(info["image"], width=400)
    st.title(name)
    st.markdown(f"""
- ประเภท: **{info['category']}**
- ที่ตั้ง: 📍 {info['location']}
- เวลาเปิด: 🕒 {info['open']}
""")
else:
    st.error("ไม่พบข้อมูลร้าน")

# Back link
st.page_link("Home.py", label="⬅️ กลับหน้าแรก", icon="🏠")
