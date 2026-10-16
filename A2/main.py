import os
import csv
import datetime


# ==============================================================================
# 1. ENCAPSULATION & INHERITANCE: คลาสแม่ (Base Class)
# ==============================================================================
class BaseTransaction:
    """
    คลาสแม่: แสดง Encapsulation โดยซ่อน Attribute สำคัญเป็น Private (__ตัวแปร)
    และเข้าถึงผ่าน Getter / Setter
    """

    def __init__(self, date_string, category, amount):
        # ข้อมูลถูกห่อหุ้มไว้ (Encapsulated) ภายนอกไม่สามารถเข้าถึงตรงๆ ได้
        self.__date_string = date_string
        self.__category = category
        self.__amount = 0.0

        # ใช้ Setter ในการกำหนดค่า เพื่อให้ผ่านการตรวจสอบข้อมูลเสมอ
        self.set_amount(amount)

    # --- Getter Methods ---
    def get_date(self):
        return self.__date_string

    def get_category(self):
        return self.__category

    def get_amount(self):
        return self.__amount

    # --- Setter Methods ---
    def set_amount(self, amount):
        numeric_amount = float(amount)
        if numeric_amount <= 0:
            print("ข้อผิดพลาด: จำนวนเงินต้องมากกว่า 0")
            self.__amount = 0.0
        else:
            self.__amount = numeric_amount

    # --- Methods สำหรับให้คลาสลูกทำ Polymorphism (Overriding) ---
    def get_type_name(self):
        """ส่งคืนชื่อประเภทของรายการ"""
        return "Generic Transaction"

    def get_balance_impact(self):
        """ส่งคืนผลกระทบต่อยอดเงินคงเหลือ (บวก หรือ ลบ)"""
        return 0.0

    def get_financial_role(self):
        """ส่งคืนบทบาททางการเงินเพื่อจัดกลุ่มสรุปผล"""
        return "generic"

    def to_csv_row(self):
        """แปลง Object เป็นแถวข้อมูลสำหรับบันทึกลงไฟล์ CSV"""
        formatted_amount = "{:.2f}".format(self.get_amount())
        row = [
            self.get_date(),
            self.get_type_name(),
            self.get_category(),
            formatted_amount
        ]
        return row


# ==============================================================================
# 2. INHERITANCE & POLYMORPHISM: คลาสลูก (Subclasses)
# ==============================================================================
class IncomeTransaction(BaseTransaction):
    """คลาสลูกสำหรับ รายรับ: สืบทอดคุณสมบัติจาก BaseTransaction"""

    def get_type_name(self):
        return "Income"

    def get_balance_impact(self):
        # รายรับทำให้ยอดเงินคงเหลือเป็นบวก
        return self.get_amount()

    def get_financial_role(self):
        return "income"


class FixedExpenseTransaction(BaseTransaction):
    """คลาสลูกสำหรับ รายจ่ายประจำ: สืบทอดคุณสมบัติจาก BaseTransaction"""

    def get_type_name(self):
        return "Fixed Expense"

    def get_balance_impact(self):
        # รายจ่ายทำให้ยอดเงินคงเหลือลดลง (ติดลบ)
        return 0.0 - self.get_amount()

    def get_financial_role(self):
        return "fixed_expense"


class VariableExpenseTransaction(BaseTransaction):
    """คลาสลูกสำหรับ รายจ่ายผันแปร: สืบทอดคุณสมบัติจาก BaseTransaction"""

    def get_type_name(self):
        return "Variable Expense"

    def get_balance_impact(self):
        # รายจ่ายผันแปรทำให้ยอดเงินคงเหลือลดลง (ติดลบ)
        return 0.0 - self.get_amount()

    def get_financial_role(self):
        return "variable_expense"


class SavingsTransaction(BaseTransaction):
    """คลาสลูกสำหรับ เงินออมและการลงทุน: สืบทอดคุณสมบัติจาก BaseTransaction"""

    def get_type_name(self):
        return "Savings or Investment"

    def get_balance_impact(self):
        # เงินออมถูกกันออกจากเงินคงเหลือใช้จ่ายจริง (ติดลบจากยอดใช้จ่าย)
        return 0.0 - self.get_amount()

    def get_financial_role(self):
        return "savings"


# ==============================================================================
# 3. คลาสสร้างวัตถุ (Factory) และจัดการข้อมูลไฟล์
# ==============================================================================
class TransactionFactory:
    """ช่วยแปลงข้อมูลข้อความจากไฟล์หรือหน้าจอ ให้เป็น Instance ของคลาสลูกที่ถูกต้อง"""

    def create_transaction(self, type_name, date_string, category, amount):
        if type_name == "Income":
            return IncomeTransaction(date_string, category, amount)
        elif type_name == "Fixed Expense":
            return FixedExpenseTransaction(date_string, category, amount)
        elif type_name == "Variable Expense":
            return VariableExpenseTransaction(date_string, category, amount)
        elif type_name == "Savings or Investment":
            return SavingsTransaction(date_string, category, amount)
        else:
            return None


class FinanceManager:
    """จัดการไฟล์ CSV และคำนวณสถิติด้วยหลักการ Polymorphism"""

    def __init__(self):
        # กำหนดพาธไปยัง User System Drive (เช่น C:\Users\<user>\ หรือ /home/<user>/)
        home_directory = os.path.expanduser("~")
        self.__folder_path = os.path.join(home_directory, "FinanceTrackerData")
        self.__file_path = os.path.join(self.__folder_path, "transactions.csv")
        self.__headers = ["Date", "Type", "Item_Details", "Amount"]
        self.__factory = TransactionFactory()

        # สร้างโฟลเดอร์และไฟล์ทันทีเมื่อเปิดใช้งาน
        self.initialize_storage()

    def initialize_storage(self):
        """ตรวจสอบและสร้างโฟลเดอร์รวมถึงไฟล์เริ่มต้นถ้ายังไม่มี"""
        if not os.path.exists(self.__folder_path):
            os.makedirs(self.__folder_path)
            print("สร้างโฟลเดอร์สำหรับเก็บข้อมูลที่:", self.__folder_path)

        if not os.path.exists(self.__file_path):
            file = open(self.__file_path, mode="w", newline="", encoding="utf-8")
            writer = csv.writer(file)
            writer.writerow(self.__headers)
            file.close()
            print("สร้างไฟล์บันทึกเริ่มต้นที่:", self.__file_path)

    def add_transaction(self, transaction):
        """บันทึก Object ลงไฟล์ CSV"""
        file = open(self.__file_path, mode="a", newline="", encoding="utf-8")
        writer = csv.writer(file)
        row_data = transaction.to_csv_row()
        writer.writerow(row_data)
        file.close()

    def get_all_transactions(self):
        """อ่านไฟล์ CSV และแปลงกลับมาเป็น List ของ Object คลาสลูกแต่ละตัว"""
        transaction_list = []

        if not os.path.exists(self.__file_path):
            return transaction_list

        file = open(self.__file_path, mode="r", newline="", encoding="utf-8")
        reader = csv.reader(file)

        is_header = True
        for row in reader:
            if is_header:
                is_header = False
                continue

            if len(row) == 4:
                date_val = row[0]
                type_val = row[1]
                category_val = row[2]
                amount_val = row[3]

                # สร้าง Object ที่แท้จริงผ่าน Factory
                obj = self.__factory.create_transaction(
                    type_val,
                    date_val,
                    category_val,
                    amount_val
                )
                if obj is not None:
                    transaction_list.append(obj)

        file.close()
        return transaction_list

    def calculate_summary(self, transaction_list):
        """
        คำนวณผลสรุปทางการเงิน:
        แสดง Polymorphism เต็มรูปแบบ โดยเรียก `item.get_balance_impact()` ได้ทันที
        """
        total_income = 0.0
        income_count = 0

        total_fixed_expense = 0.0
        total_variable_expense = 0.0
        expense_count = 0

        total_savings = 0.0
        remaining_balance = 0.0

        for item in transaction_list:
            role = item.get_financial_role()
            amount = item.get_amount()

            # คำนวณยอดเงินคงเหลือด้วย Polymorphic Method โดยตรง
            remaining_balance = remaining_balance + item.get_balance_impact()

            # แยกเก็บข้อมูลตามบทบาทเพื่อนำไปแสดงผล
            if role == "income":
                total_income = total_income + amount
                income_count = income_count + 1

            elif role == "fixed_expense":
                total_fixed_expense = total_fixed_expense + amount
                expense_count = expense_count + 1

            elif role == "variable_expense":
                total_variable_expense = total_variable_expense + amount
                expense_count = expense_count + 1

            elif role == "savings":
                total_savings = total_savings + amount

        total_expense = total_fixed_expense + total_variable_expense

        # คำนวณค่าเฉลี่ย
        if income_count > 0:
            avg_income = total_income / income_count
        else:
            avg_income = 0.0

        if expense_count > 0:
            avg_expense = total_expense / expense_count
        else:
            avg_expense = 0.0

        summary = {
            "total_income": total_income,
            "avg_income": avg_income,
            "total_fixed_expense": total_fixed_expense,
            "total_variable_expense": total_variable_expense,
            "total_expense": total_expense,
            "avg_expense": avg_expense,
            "total_savings": total_savings,
            "remaining_balance": remaining_balance,
            "total_records": len(transaction_list)
        }
        return summary


# ==============================================================================
# 4. ส่วนหน้าจอ CLI (User Interface)
# ==============================================================================
class FinanceCLI:
    """จัดการส่วนแสดงผล การรับค่าผ่าน Terminal"""

    def __init__(self):
        self.manager = FinanceManager()
        self.factory = TransactionFactory()

    def input_date(self):
        today_string = datetime.date.today().strftime("%Y-%m-%d")
        prompt = "กรอกวันที่ (YYYY-MM-DD) [กด Enter เพื่อใช้วันนี้ " + today_string + "]: "
        user_input = input(prompt).strip()

        if user_input == "":
            return today_string

        try:
            datetime.datetime.strptime(user_input, "%Y-%m-%d")
            return user_input
        except ValueError:
            print("รูปแบบวันที่ไม่ถูกต้อง ระบบจะใช้วันนี้แทน")
            return today_string

    def input_amount(self):
        while True:
            amount_string = input("กรอกจำนวนเงิน (บาท): ").strip()
            try:
                val = float(amount_string)
                if val <= 0:
                    print("จำนวนเงินต้องมากกว่า 0")
                    continue
                return val
            except ValueError:
                print("กรุณากรอกตัวเลขที่ถูกต้อง")

    def add_transaction_screen(self):
        print("\n--- เลือกประเภทรายการ ---")
        print("1. Income (รายรับ: เงินเดือน, รายได้เสริม)")
        print("2. Fixed Expense (รายจ่ายประจำ: ค่าเช่า, ค่างวด)")
        print("3. Variable Expense (รายจ่ายผันแปร: ค่าอาหาร, ช้อปปิ้ง)")
        print("4. Savings or Investment (เงินออม หรือ เงินลงทุน)")

        selected_type = ""
        while True:
            choice = input("เลือกหมายเลขประเภท (1-4): ").strip()
            if choice == "1":
                selected_type = "Income"
                break
            elif choice == "2":
                selected_type = "Fixed Expense"
                break
            elif choice == "3":
                selected_type = "Variable Expense"
                break
            elif choice == "4":
                selected_type = "Savings or Investment"
                break
            else:
                print("ตัวเลือกไม่ถูกต้อง กรุณากรอก 1-4")

        category = input("กรอกชื่อรายการ/รายละเอียด: ").strip()
        if category == "":
            category = "ไม่ระบุ"

        tx_date = self.input_date()
        tx_amount = self.input_amount()

        # สร้าง Object โดยเรียกผ่าน Factory
        new_transaction = self.factory.create_transaction(
            selected_type,
            tx_date,
            category,
            tx_amount
        )

        self.manager.add_transaction(new_transaction)
        print("\n[สำเร็จ] บันทึกข้อมูลเรียบร้อยแล้ว")

    def display_table(self, records):
        if len(records) == 0:
            print("\nไม่มีข้อมูลรายการบันทึก")
            return

        print("\n" + "=" * 70)
        header_text = "{:<12} | {:<22} | {:<20} | {:>10}".format(
            "วันที่", "ประเภท", "รายละเอียด", "จำนวนเงิน"
        )
        print(header_text)
        print("-" * 70)

        for item in records:
            # ดึงข้อมูลผ่าน Getter Methods (Encapsulation)
            display_row = "{:<12} | {:<22} | {:<20} | {:>10.2f}".format(
                item.get_date(),
                item.get_type_name(),
                item.get_category()[:20],
                item.get_amount()
            )
            print(display_row)

        print("=" * 70)

    def display_summary_card(self, title, summary):
        print("\n" + "#" * 50)
        print(" " + title)
        print("#" * 50)
        print("จำนวนรายการทั้งหมด           : " + str(summary["total_records"]) + " รายการ")
        print("รายรับรวมทั้งหมด              : " + "{:.2f}".format(summary["total_income"]) + " บาท")
        print("  - รายรับเฉลี่ยต่อรายการ       : " + "{:.2f}".format(summary["avg_income"]) + " บาท")
        print("รายจ่ายประจำ (Fixed)          : " + "{:.2f}".format(summary["total_fixed_expense"]) + " บาท")
        print("รายจ่ายผันแปร (Variable)      : " + "{:.2f}".format(summary["total_variable_expense"]) + " บาท")
        print("รายจ่ายรวมทั้งหมด             : " + "{:.2f}".format(summary["total_expense"]) + " บาท")
        print("  - รายจ่ายเฉลี่ยต่อรายการ      : " + "{:.2f}".format(summary["avg_expense"]) + " บาท")
        print("เงินออมและการลงทุน            : " + "{:.2f}".format(summary["total_savings"]) + " บาท")
        print("-" * 50)
        print("ยอดเงินคงเหลือสุทธิ (Balance)  : " + "{:.2f}".format(summary["remaining_balance"]) + " บาท")
        print("#" * 50)

    def show_all_logs(self):
        records = self.manager.get_all_transactions()
        self.display_table(records)

    def show_weekly_summary(self):
        records = self.manager.get_all_transactions()
        if len(records) == 0:
            print("\nยังไม่มีข้อมูลในระบบ")
            return

        today = datetime.date.today()
        current_year, current_week, _ = today.isocalendar()
        default_week = "{}-W{:02d}".format(current_year, current_week)

        prompt = "กรอกสัปดาห์ (เช่น 2026-W39) [กด Enter เพื่อเลือกสัปดาห์นี้ " + default_week + "]: "
        target_week = input(prompt).strip()
        if target_week == "":
            target_week = default_week

        filtered = []
        for item in records:
            try:
                date_obj = datetime.datetime.strptime(item.get_date(), "%Y-%m-%d").date()
                year_num, week_num, _ = date_obj.isocalendar()
                week_format = "{}-W{:02d}".format(year_num, week_num)
                if week_format == target_week:
                    filtered.append(item)
            except ValueError:
                continue

        self.display_table(filtered)
        summary = self.manager.calculate_summary(filtered)
        title = "สรุปผลรายสัปดาห์ (Weekly Summary: " + target_week + ")"
        self.display_summary_card(title, summary)

    def show_monthly_summary(self):
        records = self.manager.get_all_transactions()
        if len(records) == 0:
            print("\nยังไม่มีข้อมูลในระบบ")
            return

        default_month = datetime.date.today().strftime("%Y-%m")
        prompt = "กรอกเดือน (YYYY-MM) [กด Enter เพื่อเลือกเดือนนี้ " + default_month + "]: "
        target_month = input(prompt).strip()
        if target_month == "":
            target_month = default_month

        filtered = []
        for item in records:
            if item.get_date().startswith(target_month):
                filtered.append(item)

        self.display_table(filtered)
        summary = self.manager.calculate_summary(filtered)
        title = "สรุปผลสิ้นเดือน / รายเดือน (Month-End Summary: " + target_month + ")"
        self.display_summary_card(title, summary)

    def run(self):
        while True:
            print("\n========== ระบบบันทึกรายรับ-รายจ่าย (CLI OOP) ==========")
            print("1. เพิ่มรายการ (Income / Expense / Savings)")
            print("2. แสดงรายการบันทึกทั้งหมด (Transaction Logs)")
            print("3. ดูรายงานสรุปประจำสัปดาห์ (Weekly Summary)")
            print("4. ดูรายงานสรุปประจำเดือน / สิ้นเดือน (Month-End Summary)")
            print("5. ออกจากโปรแกรม")

            menu_choice = input("เลือกเมนู (1-5): ").strip()

            if menu_choice == "1":
                self.add_transaction_screen()
            elif menu_choice == "2":
                self.show_all_logs()
            elif menu_choice == "3":
                self.show_weekly_summary()
            elif menu_choice == "4":
                self.show_monthly_summary()
            elif menu_choice == "5":
                print("\nปิดโปรแกรมเรียบร้อยแล้ว")
                break
            else:
                print("กรุณาเลือกหมายเลขระหว่าง 1 ถึง 5 เท่านั้น")


if __name__ == "__main__":
    app = FinanceCLI()
    app.run()