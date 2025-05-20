import streamlit as st
import openai
import pandas as pd
import json

# ---------------------------
# CONFIG
# ---------------------------
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@300;400;600&display=swap');
html, body, div, p, h1, h2, h3, h4 {
    font-family: 'Noto Sans Thai', sans-serif !important;
}
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 20px;
    margin-top: 20px;
}
.card {
    background: white;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    height: 100%;
}
.tag {
    background-color: #eee;
    color: #333;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 13px;
    display: inline-block;
    margin-right: 6px;
    margin-bottom: 4px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# INPUT DATA (คุณต้องเปลี่ยนตามจริง)
# ---------------------------
r = {"name": "รวมร้านบุฟเฟ่ต์ปิ้งย่างและชาบู"}

# ตัวอย่าง DataFrame (filtered เฉพาะร้านที่เลือก)
filtered = pd.DataFrame([
    {"Card_name": "KTC Platinum", "Benefit_detail": "แลกคะแนนรับส่วนลดบุฟเฟ่ต์ 80 บาท/ท่าน เมื่อใช้ 699 คะแนน KTC"},
    {"Card_name": "KTC Signature", "Benefit_detail": "แลกคะแนนรับส่วนลดบุฟเฟ่ต์ 150 บาท/ท่าน เมื่อใช้ 699 คะแนน KTC"},
])

user_cards = ["KTC Platinum"]

# ---------------------------
# PROMPT ส่งให้ OpenAI
# ---------------------------
prompt = f"""
คุณคือผู้ช่วยด้านการเงินและโปรโมชั่นบัตรเครดิต

ร้าน: {r['name']}

ข้อมูลโปรโมชั่นทั้งหมด:
{filtered[['Card_name', 'Benefit_detail']].to_csv(index=False)}

ผู้ใช้มีบัตรดังต่อไปนี้:
{', '.join(user_cards)}

กรุณาช่วย:
1. เรียงลำดับบัตรจากแต่ละกลุ่ม โดยพิจารณาจาก:
   - จำนวนเงินที่ต้องจ่ายน้อยที่สุด (amount)
   - ความง่ายในการใช้ (เงื่อนไขไม่ซับซ้อน)
   - มูลค่า benefit ที่ได้รับจริง
   จัดกลุ่มบัตรเป็น:
   - ✅ บัตรที่ผู้ใช้มี
   - 💳 บัตรที่ผู้ใช้ไม่มี

2. สำหรับแต่ละบัตร ช่วยจัดประเภทการใช้งาน:
   - กินคนเดียว / กินเป็นกลุ่ม
   - ต้องจ่ายเกินเท่าไหร่
   - คุ้มยังไง
   - คำแนะนำ: เช่น “ปิ้งย่าง”, “เหมาะกับกลุ่ม”, “คุ้มเมื่อใช้คะแนน”

3. ตอบกลับเฉพาะในรูปแบบ JSON เท่านั้น:
[
  {{
    "ร้าน": "ชื่อร้าน",
    "ประเภท": "ปิ้งย่าง / ชาบู",
    "benefit": "ลด ...",
    "amount_min": 699,
    "กลุ่ม": "✅ หรือ 💳",
    "เหมาะกับ": "กินคนเดียว / กินเป็นกลุ่ม",
    "คำแนะนำ": "ข้อความสั้น ๆ เช่น ปิ้งย่าง"
  }}
]
"""

# ---------------------------
# CALL OpenAI API
# ---------------------------
with st.spinner("กำลังวิเคราะห์ข้อมูล..."):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

# ---------------------------
# PARSE JSON RESPONSE
# ---------------------------
try:
    content = response['choices'][0]['message']['content']
    json_data = json.loads(content)
except Exception as e:
    st.error("❌ ไม่สามารถแปลงผลลัพธ์จาก OpenAI เป็น JSON ได้")
    st.code(content)
    st.stop()

# ---------------------------
# DISPLAY UI
# ---------------------------
st.markdown("### 📋 ผลลัพธ์แนะนำบัตรที่คุ้มค่าที่สุด")
st.markdown('<div class="card-grid">', unsafe_allow_html=True)

for item in json_data:
    st.markdown(f"""
    <div class="card">
        <h4>{item['ร้าน']}</h4>
        <p><strong>ประเภท:</strong> {item.get('ประเภท', '-')}</p>
        <p><strong>สิทธิประโยชน์:</strong> {item['benefit']}</p>
        <p><strong>ขั้นต่ำ:</strong> {item.get('amount_min', '-'):,} บาท</p>
        <div>
            <span class="tag">{item['กลุ่ม']}</span>
            <span class="tag">{item['เหมาะกับ']}</span>
            <span class="tag">{item['คำแนะนำ']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
