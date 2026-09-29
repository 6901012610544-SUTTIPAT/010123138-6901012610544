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
    def __init__(self):
        pass

    def get_date(self):
        pass

    def get_category(self):
        pass

    def get_amount(self):
        pass

    def set_amount(self):
        pass

    def get_type_name(self):
        pass

    def get_balance_impact(self):
        pass

    def get_financial_role(self):
        pass

    def to_csv_row(self):
        pass

#=====================================================
#|                     SUB CLASS                     |
#=====================================================
class IncomeTransaction(BaseTransaction):
    """
    Subclass for income.
    Inherit from BaseTransaction
    """
    def get_type_name(self):
        pass

    def get_balance_impact(self):
        pass

    def get_financial_role(self):
        pass

class FixedExpenseTransaction(BaseTransaction):
    """
    Subclass for fixed expense
    Inherit from BaseTransaction
    """
    def get_type_name(self):
        pass

    def get_balance_impact(self):
        pass

    def get_financial_role(self):
        pass

class VariableExpenseTransaction(BaseTransaction):
    """
    Subclass for variable expense
    inherit from BaseTransaction
    """
    def get_type_name(self):
        pass

    def get_balance_impact(self):
        pass

    def get_financial_role(self):
        pass

class SavingsTransaction(BaseTransaction):
    """
    Subclass for savings and investment
    inherit from BaseTransaction
    """
    def get_type_name(self):
        pass

    def get_balance_impact(self):
        pass

    def get_financial_role(self):
        pass


#=====================================================
#|                FILE OPERATION CLASS               |
#=====================================================
class TransactionFactory:
    """
    This class help converts .csv to class instance for every subclasses.
    """
    def create_transaction(self):
        pass

class FinanceManager:
    """
    Manage CSV and calculate statics by using polymorphism
    """
    def __init__(self):
        pass

    def initialize_storage(self):
        pass

    def add_transaction(self):
        pass

    def get_all_transactions(self):
        pass

    def calculate_summary(self):
        pass

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
        print("\n--- เลือกประเภทรายการ ---")
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