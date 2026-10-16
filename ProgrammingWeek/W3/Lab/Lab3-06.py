def calculate_area(width, length):
    return width * length

def can_fit_court(land_width, land_length, court_width, court_length):
    fit_normal = (land_width >= court_width) and (land_length >= court_length)
    fit_rotated = (land_width >= court_length) and (land_length >= court_width)
    return fit_normal or fit_rotated

#รับข้อมูลความกว้างและความยาวจากผู้ใช้ (เมตร)
print("=== โปรแกรมคำนวณพื้นที่ดินและตรวจสอบสนามกีฬา ===")
width = float(input("ป้อนความกว้างของที่ดิน (เมตร): "))
length = float(input("ป้อนความยาวของที่ดิน (เมตร): "))

#คำนวณและแสดงผลพื้นที่
area = calculate_area(width, length)
print(f"\nพื้นที่ดินทั้งหมด: {area:,.2f} ตารางเมตร")
print("----------------------------------------------------")


#ขนาดสนามมาตรฐาน (กว้าง x ยาว):
#Volleyball (9x18 เมตร), Basketball (15x28 เมตร), Football (68x105 เมตร)

is_volleyball_ok = can_fit_court(width, length, 9, 18)
is_basketball_ok = can_fit_court(width, length, 15, 28)
is_football_ok = can_fit_court(width, length, 68, 105)

print("ผลการตรวจสอบพื้นที่สำหรับสนามกีฬา:")
print(f"- Volleyball (วอลเลย์บอล): {is_volleyball_ok}")
print(f"- Basketball (บาสเกตบอล): {is_basketball_ok}")
print(f"- Football (ฟุตบอล): {is_football_ok}")