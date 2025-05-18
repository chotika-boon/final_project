import streamlit as st

# st.set_page_config must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Sign In")

# Custom CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
        html, body, [class*="css"] {
            font-family: 'Noto Sans Thai', sans-serif;
        }
        .container {
            display: flex;
            flex-direction: row;
            height: 100vh;
        }
        .left {
            flex: 0 0 40%;
            background-color: #f2f6f5;
            padding: 4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .right {
            flex: 0 0 60%;
            background-color: #0e3c2e;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }
        .logo {
            width: 60px;
            margin-bottom: 10px;
        }
        .title {
            font-size: 32px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 14px;
            margin-bottom: 20px;
        }
        .subtitle a {
            color: #0e3c2e;
            font-weight: bold;
        }
        .input-label {
            margin-top: 10px;
            font-size: 14px;
            font-weight: 600;
        }
        .input {
            padding: 10px;
            width: 100%;
            border-radius: 8px;
            border: 1px solid #ddd;
            margin-bottom: 10px;
        }
        .actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            font-size: 13px;
        }
        .btn-main {
            width: 100%;
            padding: 12px;
            background-color: #0e3c2e;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            border: none;
            margin-bottom: 12px;
        }
        .social {
            background-color: white;
            color: #444;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 10px;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 10px;
            justify-content: center;
        }
        .highlight-box {
            background-color: white;
            color: #0e3c2e;
            border-radius: 12px;
            padding: 24px;
            text-align: left;
            max-width: 360px;
        }
        .highlight-title {
            font-weight: 700;
            font-size: 16px;
            margin-bottom: 8px;
        }
        .highlight-description {
            font-size: 13px;
            margin-bottom: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Layout section
top, content = st.columns([1, 1])  # just dummy to avoid margin from top
st.markdown("<div class='container'>", unsafe_allow_html=True)

# Left Panel
st.markdown("""
    <div class='left'>
        <img class='logo' src='https://i.ibb.co/yPz4Bf4/logo.png'>
        <div class='title'>Sign in</div>
        <div class='subtitle'>ยังไม่มีบัญชี? <a href='#'>สร้างบัญชี</a></div>

        <div class='input-label'>E-mail</div>
        <input type='text' class='input' placeholder='example@gmail.com'/>

        <div class='input-label'>Password</div>
        <input type='password' class='input' placeholder='รหัสผ่าน'/>

        <div class='actions'>
            <div><input type='checkbox'/> จำฉันไว้</div>
            <a href='#'>ลืมรหัสผ่าน?</a>
        </div>

        <button class='btn-main'>เข้าสู่ระบบ</button>
        <div class='social'>🔵 เข้าสู่ระบบด้วย Google</div>
        <div class='social'>🔵 เข้าสู่ระบบด้วย Facebook</div>
    </div>
""", unsafe_allow_html=True)

# Right Panel
st.markdown("""
    <div class='right'>
        <div class='highlight-box'>
            <div class='highlight-title'>📌 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</div>
            <div class='highlight-description'>ใช้บัตร Venus ของคุณทั่วโลก โดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้จ่ายได้ทันที</div>
            <button class='btn-main' style='background:white; color:#0e3c2e;'>ดูเพิ่มเติม</button>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
