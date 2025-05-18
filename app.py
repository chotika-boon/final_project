st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');

body, html, * {
    font-family: 'Noto Sans Thai', sans-serif;
}

.container {
    display: flex;
    flex-direction: row;
    height: 100vh;
    margin: 0;
    padding: 0;
    overflow: hidden;
}

.left-panel {
    width: 40%;
    padding: 4rem;
    background: #f7f9f8;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.right-panel {
    width: 60%;
    background-color: #0e3c2e;
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

input, button {
    font-family: 'Noto Sans Thai', sans-serif;
    font-size: 16px;
    margin-top: 10px;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid #ccc;
    width: 100%;
}

.login-btn {
    background: #0e3c2e;
    color: white;
    font-weight: bold;
}

.social-btn {
    background: white;
    color: #333;
    border: 1px solid #ccc;
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>

<div class="container">
  <div class="left-panel">
    <img src="https://your-path-to/คู่คิด-removebg-preview.png" width="80" />
    <h2>Sign in</h2>
    <p>ยังไม่มีบัญชี? <a href="#">สร้างบัญชี</a></p>

    <input type="text" placeholder="example@gmail.com" />
    <input type="password" placeholder="รหัสผ่าน" />

    <div style="display: flex; justify-content: space-between;">
        <label><input type="checkbox" /> จำฉันไว้</label>
        <a href="#">ลืมรหัสผ่าน?</a>
    </div>

    <button class="login-btn">เข้าสู่ระบบ</button>
    <div class="social-btn">🔵 เข้าสู่ระบบด้วย Google</div>
    <div class="social-btn">🔵 เข้าสู่ระบบด้วย Facebook</div>
  </div>

  <div class="right-panel">
    <div style="max-width: 350px; text-align: center;">
        <h3>📌 บรรลุเป้าหมายทางการเงินได้ไวขึ้น</h3>
        <p>ใช้บัตร Venus ของคุณทั่วโลก โดยไม่มีค่าธรรมเนียมแอบแฝง พร้อมโอนและใช้งานได้ทันที</p>
        <button style="background: white; color: #0e3c2e;">ดูเพิ่มเติม</button>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
