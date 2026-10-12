# ฟังก์ชันสำหรับเปรียบเทียบและ return ผลลัพธ์
def get_most_sport(football, basketball, volleyball):
    # กรณีที่มีอย่างใดอย่างหนึ่งมากที่สุดตัวเดียว
    if football > basketball and football > volleyball:
        return f"Football มากที่สุด ({football} ลูก)"
    elif basketball > football and basketball > volleyball:
        return f"Basketball มากที่สุด ({basketball} ลูก)"
    elif volleyball > football and volleyball > basketball:
        return f"Volleyball มากที่สุด ({volleyball} ลูก)"
    
    # กรณีที่มีจำนวนสูงสุดเท่ากันมากกว่า 1 กีฬา
    else:
        highest = football
        if basketball > highest:
            highest = basketball
        if volleyball > highest:
            highest = volleyball
            
        result = f"มีจำนวนมากที่สุดเท่ากัน ({highest} ลูก) ได้แก่:"
        if football == highest:
            result += "\n- Football"
        if basketball == highest:
            result += "\n- Basketball"
        if volleyball == highest:
            result += "\n- Volleyball"
            
        return result


#1. รับค่าตัวแปร integer 3 ตัว
fb = int(input("ป้อนจำนวนลูก Football: "))
bb = int(input("ป้อนจำนวนลูก Basketball: "))
vb = int(input("ป้อนจำนวนลูก Volleyball: "))

print("----------------------------------------")

#2. เรียกใช้ฟังก์ชัน แล้วรับค่าที่ return กลับมาเก็บไว้ในตัวแปร
result_message = get_most_sport(fb, bb, vb)

# 3. แสดงผลลัพธ์
print(result_message)