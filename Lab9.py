import pandas as pd
import matplotlib.pyplot as plt

# 1. อ่านไฟล์ข้อมูล (ใช้ path ที่คุณทำผ่านแล้ว)
# ถ้ามีปัญหาเรื่อง path ให้แก้เป็น r'C:\Users\User\Downloads\...' เหมือนเดิมนะครับ
try:
    df_d1 = pd.read_csv('Waveform_2026-02-11.csv', sep='\t', encoding='utf-16')
    df_led = pd.read_csv('Waveform_2026-02-11 (1).csv', sep='\t', encoding='utf-16')
except:
    # เผื่อกรณีไฟล์ไม่ได้เป็น utf-16
    df_d1 = pd.read_csv('Waveform_2026-02-11.csv', sep='\t')
    df_led = pd.read_csv('Waveform_2026-02-11 (1).csv', sep='\t')

# 2. ล้างชื่อคอลัมน์ให้สะอาด (ลบช่องว่าง)
df_d1.columns = df_d1.columns.str.strip()
df_led.columns = df_led.columns.str.strip()

# 3. ตั้งค่าการสร้างกราฟ
plt.figure(figsize=(12, 5)) # กำหนดขนาดรูป (กว้าง x สูง)

# --- กราฟที่ 1: Standard Diode (D1) ---
plt.subplot(1, 2, 1)
# แกน X: แรงดันตกคร่อม D1 = V(vs_1)
# แกน Y: กระแส D1 = I(D1) (คูณ 1000 เพื่อแปลงเป็น mA)
plt.plot(df_d1['V(vs_1)'], df_d1['I(D1)'] * 1000, label='D1 Current', color='blue', linewidth=2)

# เส้นประแสดงจุดทำงาน (ประมาณ 0.6-0.7V)
plt.axvline(x=0.65, color='gray', linestyle='--', alpha=0.7, label='Turn-on ~0.65V')

plt.title('IV Characteristic: Standard Diode (D1)')
plt.xlabel('Voltage Across Diode (V)')
plt.ylabel('Current (mA)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# --- กราฟที่ 2: LED (D2) ---
plt.subplot(1, 2, 2)
# แกน X: แรงดันตกคร่อม LED = V(d2_1)
# แกน Y: กระแส LED = I(D2)
plt.plot(df_led['V(d2_1)'], df_led['I(D2)'] * 1000, label='LED Current', color='red', linewidth=2)

plt.title('IV Characteristic: LED (D2)')
plt.xlabel('Voltage Across LED (V)')
plt.ylabel('Current (mA)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# จัดระยะห่างให้สวยงาม
plt.tight_layout()

# 4. บันทึกเป็นไฟล์รูปภาพ (จะถูกเซฟในโฟลเดอร์เดียวกับที่คุณรันโค้ด)
plt.savefig('Lab_Report_Graphs.png', dpi=300) 
print("บันทึกกราฟเสร็จเรียบร้อย! ชื่อไฟล์: Lab_Report_Graphs.png")

# 5. แสดงผลบนหน้าจอ
plt.show()
