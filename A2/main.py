#=====================================================
#|         A2: Income and expense tracker            |
#|       6901012610544 นายสุทธิภัทร เอื้อพัฒนากิจ         |
#=====================================================

#Last update: 29.09.2026 08.19PM

import os
import csv
from datetime import datetime


#=====================================================
#|                     BASE CLASS                    |
#=====================================================
class BaseTransaction:
    """
    Superclass for storing incomes and expenses data.
    Used techniques: Encapsulation, and Polymorphism.
    """
    def __init__(self, date_string, category, amount):
        #Encapsulated attributes
        self.__date_string = date_string
        self.__category = category
        self.__amount = 0.0

        #Use setter for cofiguring value
        self.set_amount(amount)

    #Getter methods
    def get_date(self):
        return self.__date_string

    def get_category(self):
        return self.__category

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        numeric_amount = float(amount)
        if numeric_amount <= 0:
            print("Error: Amount must greater than 0.")
        else:
            self.__amount = numeric_amount
    

    #Method for polymorphism in subclasses
    def get_type_name(self):
        #Return transaction type
        return "Generic Transaction"

    def get_balance_impact(self):
        #Return positive or negative impact in balance
        return 0.0
    
    def get_financial_role(self):
        #Return role in bugetting for summary
        return "generic"
    
    def to_csv_row(self):
        #Convert object to row for saving in CSV
        formatted_amount = "{:.2f}".format(self.get_amount())
        row = [
            self.get_date(),
            self.get_type_name(),
            self.get_category(),
            formatted_amount
        ]
        return row

#=====================================================
#|                     SUB CLASS                     |
#=====================================================
class IncomeTransaction(BaseTransaction):
    """
    Subclass for income.
    Inherit from BaseTransaction
    """
    def get_type_name(self):
        return "Income"

    def get_balance_impact(self):
        #Income makes balance become positive
        return self.get_amount()

    def get_financial_role(self):
        return "income"

class FixedExpenseTransaction(BaseTransaction):
    """
    Subclass for fixed expense
    Inherit from BaseTransaction
    """
    def get_type_name(self):
        return "Fixed Expense"

    def get_balance_impact(self):
        #Expense makes balance become negative
        return 0.0 - self.get_amount()

    def get_financial_role(self):
        return "fixed_expense"

class VariableExpenseTransaction(BaseTransaction):
    """
    Subclass for variable expense
    inherit from BaseTransaction
    """
    def get_type_name(self):
        return "Variable Expense"

    def get_balance_impact(self):
        #Same as fixed expense
        return 0.0 - self.get_amount()

    def get_financial_role(self):
        return "variable_expense"

class SavingsTransaction(BaseTransaction):
    """
    Subclass for savings and investment
    inherit from BaseTransaction
    """
    def get_type_name(self):
        return "Savings or Investment"

    def get_balance_impact(self):
        #Savings sets aside
        return 0.0 - self.get_amount()

    def get_financial_role(self):
        return "savings"


#=====================================================
#|                FILE OPERATION CLASS               |
#=====================================================
class TransactionFactory:
    """
    This class help converts .csv to class instance for every subclasses.
    """
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
    """
    Manage CSV and calculate statics by using polymorphism
    """
    def __init__(self):
        #Set path
        home_directory = os.path.expanduser("~")
        self.__folder_path = os.path.join(home_directory, "FinanceTrackerData")
        self.__file_path = os.path.join(self.__folder_path, "transactions.csv")
        self.__headers = ["Date",
                          "Type",
                          "Item_Details",
                          "Amount"]
        self.__factory = TransactionFactory()

        #Creates folder when initialize
        self.initialize_storage()

    def initialize_storage(self):
        if not os.path.exists(self.__folder_path):
            os.makedirs(self.__folder_path)
            print("Create folder for saving data at: ", self.__folder_path)
        if not os.path.exists(self.__file_path):
            file = open(self.__file_path, mode="w", newline="", encoding="utf-8")
            writer = csv.writer(file)
            writer.writerow(self.__headers)
            file.close()
            print("Create save file at: ", self.__file_path)

    def add_transaction(self, transaction):
        #save object to csv
        file = open(self.__file_path, mode="a", newline="", encoding="utf-8")
        writer = csv.writer(file)
        row_data = transaction.to_csv_row()
        writer.writerow(row_data)
        file.close()

    def get_all_transactions(self):
        #Read CSV and converts back to list of objects of each subclasses
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

                #Create real object through Factory
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
        Compute bugetting summary
        This method use polymorphism
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

            #Calculate balance by using polymorphic method directly
            remaining_balance = remaining_balance + item.get_balance_impact()

            #Save transaction role separately for displaying
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

        #Calculate average
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
#=====================================================
#|                  USER INTERFACE                   |
#=====================================================
class FinanceCLI:
    """
    Manage I/O through Terminal
    """
    def __init__(self):
        self.manager = FinanceManager()
        self.factory = TransactionFactory()

    def input_date(self):
        pass

    def input_amount(self):
        pass

    def add_transaction_screen(self):
        print("\n--- Select Category ---")
        print("1. Income (รายรับ)")
        print("2. Fixed Expense (รายจ่ายประจำ)")
        print("3. Variable Expense (รายจ่ายผันแปร)")
        print("4. Savings or Investment (เงินออม หรือ เงินลงทุน)")

    def display_table(self):
        pass

    def display_summary_card(self):
        pass

    def show_all_logs(self):
        pass

    def show_weekly_summary(self):
        pass

    def show_monthly_summary(self):
        pass

    def run(self):
        pass


def main():
    app = FinanceCLI()
    app.run()

if __name__ == "__main__":
    main()