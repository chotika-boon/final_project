# File: RestaurantDetail.py
import streamlit as st

st.set_page_config(layout="centered")

params = st.query_params
name = params.get("name", "")

# ข้อมูล mock
detail = {
    "Thong Grill Hide & Yakiniku": {
        "image": "https://img.wongnai.com/p/624x0/2025/03/28/7b4e368494c94cee80dfc99f0a7704dc.jpg",
        "desc": "ชาบู-ยากินิกุ ร้านดังย่านสุขุมวิท",
    },
    "Burger King": {
        "image": "https://img.wongnai.com/p/624x0/2020/05/08/0b4e2176d17c44d48d0ff22a2b5d167c.jpg",
        "desc": "เบอร์เกอร์สัญชาติอเมริกัน",
    },
    "Starbucks River City": {
        "image": "https://img.wongnai.com/p/624x0/2023/11/11/4d7eaa83a0dc4607b2e6edec001f33c4.jpg",
        "desc": "ร้านกาแฟวิวริมแม่น้ำเจ้าพระยา",
    },
    "MOS BURGER": {
        "image": "https://img.wongnai.com/p/624x0/2019/12/17/a3a24300483f46298b728452dcdddb76.jpg",
        "desc": "เบอร์เกอร์ญี่ปุ่นแท้ๆ",
    }
}

if name and name in detail:
    st.title(name)
    st.image(detail[name]["image"], width=400)
    st.write(f"📄 {detail[name]['desc']}")
else:
    st.error("ไม่พบข้อมูลร้าน")

# ปุ่มกลับหน้าแรก
st.page_link("Home.py", label="⬅️ กลับหน้าแรก", icon="🏠")
