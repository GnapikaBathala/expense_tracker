from Expense import Expense, ExpenseManager
from Income import Income, IncomeManager
from Budget import BudgetManager

from JSONstorage import save_data, load_data

from data_to_CSV_export import export_budgets_to_csv,export_expenses_to_csv,export_incomes_to_csv

from datetime import datetime
# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_positive_float(prompt):

    while True:

        try:

            value = float(input(prompt))

            if value <= 0:
                print("Value must be greater than zero.")
                continue
            return value

        except ValueError:
            print("Please enter a valid number.")
                
def get_valid_date(prompt):

    while True:

        date = input(prompt).strip()

        try:

            datetime.strptime( date,"%d-%m-%Y")
            return date
        except ValueError:
            print("Invalid date. "
                "Please use DD-MM-YYYY.")

def get_valid_month(prompt):

    while True:

        month = input(prompt).strip()

        try:
            datetime.strptime(month,"%m-%Y")
            return month

        except ValueError:
            print("Invalid month. "
                "Please use MM-YYYY."
            )
# ============================================================
# DISPLAY MENU
# ============================================================
def display_menu():

    print("""
========================================
       PERSONAL EXPENSE TRACKER
========================================
1.  Add Expense
2.  View All Expenses
3.  Search Expenses
4.  Edit Expense
5.  Delete Expense
6.  Add Income
7.  View Income
8.  Edit Income
9.  Delete Income
10. Set Monthly Budget
11. View All Budgets
12. View Budget Status
13. Expense Analysis
14. Financial Summary
15. Export Data to CSV
16. Save Data
17. Exit
========================================
""")
# ============================================================
# MAIN
# ============================================================

def main():

    manager = ExpenseManager()
    income_manager = IncomeManager()
    budget_manager = BudgetManager()

    # Load previously saved data
    load_data(manager,income_manager,budget_manager)
    print("\nData loaded successfully.")

    while True:

        display_menu()
        choice = input("Enter your choice: ").strip()
        try:

            # ==================================================
            # 1. ADD EXPENSE
            # ==================================================

            if choice == "1":

                print()
                print("****** Add New Expense ******")

                amount = get_positive_float(
                    "Enter Expense Amount: "
                )

                category = input(
                    "Enter category: "
                ).strip()

                description = input(
                    "Enter description: "
                ).strip()

                date = get_valid_date(
                    "Enter date (DD-MM-YYYY): "
                )

                expense = Expense(
                    amount,
                    category,
                    description,
                    date
                )

                manager.add_expense(expense)

                print()

            # ==================================================
            # 2. VIEW EXPENSES
            # ==================================================

            elif choice == "2":

                print()
                print("****** Expenses Details ******")

                print(
                    f"{'ID':<8} | "
                    f"{'Amount':>10} | "
                    f"{'Category':<15} | "
                    f"{'Description':<25} | "
                    f"{'Date':<12} |"
                )

                print("-" * 85)

                manager.view_expenses()

                print()

            # ==================================================
            # 3. SEARCH EXPENSE
            # ==================================================

            elif choice == "3":

                print()
                print(
                    "****** Search Expenses ******"
                )

                print(
                    "Search by ID, category, "
                    "description or date."
                )

                expense_key = input(
                    "Enter search value: "
                ).strip()

                if expense_key.isdigit():

                    expense_key = int(
                        expense_key
                    )

                expenses = manager.get_expenses(
                    expense_key
                )

                if expenses:

                    print("\nExpenses found:")

                    print(
                        f"{'ID':<8} | "
                        f"{'Amount':>10} | "
                        f"{'Category':<15} | "
                        f"{'Description':<25} | "
                        f"{'Date':<12} |"
                    )

                    print("-" * 85)

                    for expense in expenses:

                        print(
                            expense.get_details()
                        )

                else:

                    print(
                        "No matching expense found."
                    )

                print()

            # ==================================================
            # 4. EDIT EXPENSE
            # ==================================================

            elif choice == "4":

                print()
                print(
                    "****** Edit Expense ******"
                )

                expense_id = int(
                    input(
                        "Enter expense ID: "
                    )
                )

                if manager.edit_expense(
                    expense_id
                ):

                    print(
                        "Expense edited successfully!"
                    )

                else:

                    print(
                        "Expense not found."
                    )

                print()

            # ==================================================
            # 5. DELETE EXPENSE
            # ==================================================

            elif choice == "5":

                print()
                print(
                    "****** Delete Expense ******"
                )

                expense_id = int(
                    input(
                        "Enter expense ID: "
                    )
                )

                if manager.delete_expense(
                    expense_id
                ):

                    print(
                        "Expense deleted successfully!"
                    )

                else:

                    print(
                        "Expense not found."
                    )

                print()

            # ==================================================
            # 6. ADD INCOME
            # ==================================================

            elif choice == "6":

                print()
                print(
                    "****** Add Income ******"
                )

                amount = get_positive_float(
                    "Enter income amount: "
                )

                source = input(
                    "Enter source of income: "
                ).strip()

                date = get_valid_date(
                    "Enter date (DD-MM-YYYY): "
                )

                income = Income(
                    amount,
                    source,
                    date
                )

                income_manager.add_income(
                    income
                )

                print()

            # ==================================================
            # 7. VIEW INCOME
            # ==================================================

            elif choice == "7":

                print()
                print(
                    "****** Income Details ******"
                )

                print(
                    f"{'ID':<8} | "
                    f"{'Amount':>10} | "
                    f"{'Source':<15} | "
                    f"{'Date':<12} |"
                )

                print("-" * 70)

                income_manager.view_incomes()

                print()

            # ==================================================
            # 8. EDIT INCOME
            # ==================================================

            elif choice == "8":

                print()
                print(
                    "****** Edit Income ******"
                )

                income_id = int(
                    input(
                        "Enter income ID: "
                    )
                )

                if income_manager.edit_income(
                    income_id
                ):

                    print(
                        "Income edited successfully!"
                    )

                else:

                    print(
                        "Income not found."
                    )

                print()

            # ==================================================
            # 9. DELETE INCOME
            # ==================================================

            elif choice == "9":

                print()
                print(
                    "****** Delete Income ******"
                )

                income_id = int(
                    input(
                        "Enter income ID: "
                    )
                )

                if income_manager.delete_income(
                    income_id
                ):

                    print(
                        "Income deleted successfully!"
                    )

                else:

                    print(
                        "Income not found."
                    )

                print()

            # ==================================================
            # 10. SET MONTHLY BUDGET
            # ==================================================

            elif choice == "10":

                print()
                print(
                    "****** Set Monthly Budget ******"
                )

                month = get_valid_month(
                    "Enter month (MM-YYYY): "
                )

                limit = get_positive_float(
                    "Enter monthly budget limit: "
                )

                budget_manager.set_budget(
                    month,
                    limit
                )

                print(
                    f"Budget of ₹{limit:.2f} "
                    f"set for {month}."
                )

                print()

            # ==================================================
            # 11. VIEW ALL BUDGETS
            # ==================================================

            elif choice == "11":

                print()
                print(
                    "****** All Budgets ******"
                )

                print(
                    f"{'Month':<12} | "
                    f"{'Budget':>12}"
                )

                print("-" * 30)

                budget_manager.view_budgets()

                print()

            # ==================================================
            # 12. BUDGET STATUS
            # ==================================================

            elif choice == "12":

                print()
                print(
                    "****** Budget Status ******"
                )

                month = get_valid_month(
                    "Enter month (MM-YYYY): "
                )

                budget = budget_manager.get_budget(
                    month
                )

                if budget is None:

                    print(
                        f"No budget found for {month}."
                    )

                else:

                    spent = (
                        manager.total_expenses_by_month(
                            month
                        )
                    )

                    remaining = (
                        budget.remaining(spent)
                    )

                    percentage = (
                        budget.percentage_used(
                            spent
                        )
                    )

                    print(
                        f"Month           : "
                        f"{budget.month}"
                    )

                    print(
                        f"Budget Limit    : "
                        f"₹{budget.limit:.2f}"
                    )

                    print(
                        f"Total Spent     : "
                        f"₹{spent:.2f}"
                    )

                    print(
                        f"Remaining       : "
                        f"₹{remaining:.2f}"
                    )

                    print(
                        f"Used            : "
                        f"{percentage:.2f}%"
                    )

                    if percentage >= 100:

                        print(
                            "WARNING: "
                            "Budget exceeded!"
                        )

                    elif percentage >= 80:

                        print(
                            "WARNING: "
                            "More than 80% "
                            "of budget used."
                        )

                print()

            # ==================================================
            # 13. EXPENSE ANALYSIS
            # ==================================================

            elif choice == "13":

                print()
                print(
                    "****** Expense Analysis ******"
                )

                if not manager.expenses:

                    print(
                        "No expenses available "
                        "for analysis."
                    )

                    print()

                    continue

                # Total
                total = manager.total_expenses()

                # Count
                count = len(
                    manager.expenses
                )

                # Average
                average = (
                    manager.average_expense()
                )

                print(
                    f"Total Expenses         : "
                    f"₹{total:.2f}"
                )

                print(
                    f"Number of Transactions : "
                    f"{count}"
                )

                print(
                    f"Average Expense        : "
                    f"₹{average:.2f}"
                )

                # ------------------------------
                # MONTHLY
                # ------------------------------

                monthly_totals = (
                    manager.monthly_expenses()
                )

                print()
                print(
                    "Monthly Spending"
                )

                print("-" * 35)

                for month, amount in (
                    monthly_totals.items()
                ):

                    print(
                        f"{month:<20} : "
                        f"₹{amount:.2f}"
                    )

                # ------------------------------
                # CATEGORY
                # ------------------------------

                print()
                print(
                    "Category-wise Spending"
                )

                print("-" * 35)

                category_totals = (
                    manager.category_wise_expenses()
                )

                for category, amount in (
                    category_totals.items()
                ):

                    print(
                        f"{category:<20} : "
                        f"₹{amount:.2f}"
                    )

                # ------------------------------
                # HIGHEST
                # ------------------------------

                highest_categories, highest_amount = (
                    manager.highest_spending_categories()
                )

                print()
                print(
                    "Highest Spending Categories"
                )

                print("-" * 35)

                for category in (
                    highest_categories
                ):

                    print(
                        f"{category:<20} : "
                        f"₹{highest_amount:.2f}"
                    )

                print()

            # ==================================================
            # 14. FINANCIAL SUMMARY
            # ==================================================

            elif choice == "14":

                print()
                print(
                    "****** Financial Summary ******"
                )

                total_income = (
                    income_manager.total_income()
                )

                total_expenses = (
                    manager.total_expenses()
                )

                balance = (
                    total_income
                    - total_expenses
                )

                print(
                    f"Total Income     : "
                    f"₹{total_income:.2f}"
                )

                print(
                    f"Total Expenses   : "
                    f"₹{total_expenses:.2f}"
                )

                print(
                    f"Balance          : "
                    f"₹{balance:.2f}"
                )

                if balance > 0:

                    print(
                        "Status           : "
                        "Positive balance"
                    )

                elif balance < 0:

                    print(
                        "Status           : "
                        "Expenses exceed income"
                    )

                else:

                    print(
                        "Status           : "
                        "No remaining balance"
                    )

                print()

            # ==================================================
            # 15. EXPORT CSV
            # ==================================================

            elif choice == "15":

                print()
                print(
                    "****** Export Data to CSV ******"
                )

                export_expenses_to_csv(
                    manager.expenses
                )

                export_incomes_to_csv(
                    income_manager.incomes
                )

                export_budgets_to_csv(
                    budget_manager.budgets.values()
                )

                print(
                    "Data exported successfully."
                )

                print(
                    "Created files:"
                )

                print(
                    "1. expenses.csv"
                )

                print(
                    "2. incomes.csv"
                )

                print(
                    "3. budgets.csv"
                )

                print()

            # ==================================================
            # 16. SAVE DATA
            # ==================================================

            elif choice == "16":

                save_data(
                    manager,
                    income_manager,
                    budget_manager
                )

                print(
                    "Data saved successfully."
                )

                print()

            # ==================================================
            # 17. EXIT
            # ==================================================

            elif choice == "17":

                # Automatically save before exit
                save_data(
                    manager,
                    income_manager,
                    budget_manager
                )

                print(
                    "Data saved successfully."
                )

                print(
                    "Exiting Personal Expense Tracker..."
                )

                break

            # ==================================================
            # INVALID
            # ==================================================

            else:

                print(
                    "Invalid choice. "
                    "Please select 1-17."
                )

        except ValueError as error:

            print(
                f"Input error: {error}"
            )

        except Exception as error:

            print(
                f"An unexpected error occurred: "
                f"{error}"
            )


if __name__ == "__main__":
    main()