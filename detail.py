import streamlit as st
import pandas as pd
import os

CSV_FILE = "user_data.csv"
PROMO_FILE = "CoolKid_promotion_creditcard - Sheet2.csv"

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
    if st.session_state.get("username"):
        st.markdown(f"**ชื่อผู้ใช้:** {st.session_state.username}")
        st.markdown(f"**อีเมล:** {st.session_state.get('logged_in_email', '-')}")
    else:
        st.warning("คุณยังไม่ได้เข้าสู่ระบบ")

    try:
        df = pd.read_csv(CSV_FILE)
        current_user = df[df['email'] == st.session_state.get("logged_in_email")]
        if not current_user.empty:
            user_row = current_user.iloc[-1]
            st.markdown(f"**จำนวนบัตรเครดิตที่สมัคร:** {user_row['card_count']}")
        else:
            st.info("ไม่พบข้อมูลผู้ใช้นี้ในระบบ")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการโหลดข้อมูลผู้ใช้: {e}")

    # Divider
    st.divider()

    # Promotion Info
    st.subheader("🎁 โปรโมชั่นจากบัตรเครดิตที่ร่วมรายการ")
    try:
        promo_df = pd.read_csv(PROMO_FILE)
        filtered = promo_df[promo_df["ร้าน"] == r["name"]]
        if not filtered.empty:
            st.dataframe(filtered)
        else:
            st.info("ไม่มีโปรโมชั่นสำหรับร้านนี้ในขณะนี้")
    except Exception as e:
        st.error(f"ไม่สามารถโหลดไฟล์โปรโมชั่นได้: {e}")

    if st.button("🔙 กลับไปหน้าหลัก"):
        st.session_state.page = "home"
        st.rerun()
