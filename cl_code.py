import pandas as pd
import numpy as np

# อ่านไฟล์ Excel
df = pd.read_excel("_____________", parse_dates=["timestamp"])

# กรองช่วงเวลาที่กำหนด
df = df[(df['timestamp'] >= '2023-01-01 01:00:00') & (df['timestamp'] <= '2024-12-31 23:59:59')]

# ลบแถวที่มีค่า pm_2_5 มากกว่า 500 หรือน้อยกว่าหรือเท่ากับ 0
df = df[(df['pm_2_5'] > 0) & (df['pm_2_5'] <= 500)]

# ลบแถวที่มีค่า pm_10 มากกว่า 300 หรือน้อยกว่าหรือเท่ากับ 0
df = df[(df['pm_10'] > 0) & (df['pm_10'] <= 500)]

# 🎯 เพิ่มฟีเจอร์เกี่ยวกับเวลา
df['month'] = df['timestamp'].dt.month              # เดือน
df['hour'] = df['timestamp'].dt.hour                # ชั่วโมง

# 🎯 เพิ่มฟีเจอร์ sin และ cos สำหรับเดือนและชั่วโมง
df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)  # ค่า sin ของเดือน
df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)  # ค่า cos ของเดือน

df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)    # ค่า sin ของชั่วโมง
df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)    # ค่า cos ของชั่วโมง

#เอาปี/เดือนออก
df = df.drop(columns=['year', 'day'])

# บันทึกไฟล์ใหม่
new_file_name = 'time_feature.xlsx'
df.to_excel(new_file_name, index=False)

print("File saved successfully!")
print("""
                 \ (•◡•) /
                  \     /
                    -o-
                   |   |
                   |_  |_""")
