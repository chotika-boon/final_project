import streamlit as st
import pandas as pd

CSV_FILE = "user_data.csv"

def show_detail():
    r = st.session_state.get("restaurant_detail")
    if not r:
        st.warning("ไม่พบข้อมูลร้านที่เลือก")
        return

    st.markdown("""
        <style>
        .detail-header {
            display: flex;
            gap: 20px;
            align-items: flex-start;
        }
        .detail-image {
            flex: 1;
        }
        .detail-info {
            flex: 2;
        }
        .badge {
            background-color: #e3e3e3;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 13px;
            margin-right: 6px;
            display: inline-block;
        }
        </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<div class='detail-header'>", unsafe_allow_html=True)
    st.image(r["image_url"], width=300)
    st.markdown("<div class='detail-info'>", unsafe_allow_html=True)
    st.title(r["name"])
    st.markdown(f"<div class='badge'>{r['category']}</div>", unsafe_allow_html=True)
    st.markdown(f"<p>⭐ <b>{r['rating']}</b> ({r['reviews']} รีวิว)</p>", unsafe_allow_html=True)
    st.markdown(f"<p>{r.get('description', 'ไม่มีรายละเอียดเพิ่มเติม')}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Divider
    st.divider()

    # Show current logged-in user info
    st.subheader("👤 ข้อมูลผู้ใช้ที่เข้าสู่ระบบ")
    try:
        df = pd.read_csv(CSV_FILE)
        current_user = df[df['email'] == st.session_state.get("logged_in_email")]
        if not current_user.empty:
            user_row = current_user.iloc[-1]  # show last match (latest)
            st.markdown(f"**ชื่อผู้ใช้:** {user_row['name']}")
            st.markdown(f"**อีเมล:** {user_row['email']}")
            st.markdown(f"**จำนวนบัตรเครดิตที่สมัคร:** {user_row['card_count']}")
        else:
            st.info("ไม่พบข้อมูลผู้ใช้นี้ในระบบ")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการโหลดข้อมูลผู้ใช้: {e}")

    if st.button("🔙 กลับไปหน้าหลัก"):
        st.session_state.page = "home"
        st.rerun()
