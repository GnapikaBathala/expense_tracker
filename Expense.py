from datetime import datetime


class Expense:

    def __init__(self, amount, category, description, date, expense_id=None):
        self.amount = float(amount)
        self.category = category.strip()
        self.description = description.strip()
        self.date = date.strip()
        self.id = expense_id

        if self.amount <= 0:
            raise ValueError("Expense amount must be greater than zero.")

        # Validate date
        datetime.strptime(self.date, "%d-%m-%Y")

    def get_details(self):
        return (
            f"{self.id:<8} | "
            f"₹{self.amount:>10.2f} | "
            f"{self.category:<15} | "
            f"{self.description:<25} | "
            f"{self.date:<12} |"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["amount"],
            data["category"],
            data["description"],
            data["date"],
            data.get("id")
        )


class ExpenseManager:

    def __init__(self):
        self.expenses = []

    # ---------------- ADD ----------------

    def add_expense(self, expense):
        if expense.id is None:
            expense.id = self._next_id()

        self.expenses.append(expense)

        print(f"Expense #{expense.id} added successfully.")

    def _next_id(self):
        if not self.expenses:
            return 1

        return max(expense.id for expense in self.expenses) + 1

    # ---------------- VIEW ----------------

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:
            print(expense.get_details())

    # ---------------- SEARCH ----------------

    def get_expenses(self, expense_key):

        matches = []

        for expense in self.expenses:

            # Search by ID
            if isinstance(expense_key, int):

                if expense.id == expense_key:
                    matches.append(expense)

            # Search by category
            else:

                key = expense_key.strip().lower()

                if (
                    key in expense.category.lower()
                    or key in expense.description.lower()
                    or key in expense.date.lower()
                ):
                    matches.append(expense)

        return matches if matches else None

    # ---------------- EDIT ----------------

    def edit_expense(self, expense_id):

        for expense in self.expenses:

            if expense.id == expense_id:

                print("\nCurrent expense:")
                print(expense.get_details())

                amount = float(input("Enter new amount: "))

                if amount <= 0:
                    raise ValueError(
                        "Expense amount must be greater than zero."
                    )

                category = input("Enter new category: ").strip()

                description = input(
                    "Enter new description: "
                ).strip()

                date = input(
                    "Enter new date (DD-MM-YYYY): "
                ).strip()

                datetime.strptime(date, "%d-%m-%Y")

                expense.amount = amount
                expense.category = category
                expense.description = description
                expense.date = date

                return True

        return False

    # ---------------- DELETE ----------------

    def delete_expense(self, expense_id):

        for expense in self.expenses:

            if expense.id == expense_id:

                self.expenses.remove(expense)

                return True

        return False

    # ---------------- TOTAL ----------------

    def total_expenses(self):

        return sum(
            expense.amount
            for expense in self.expenses
        )

    # ---------------- MONTHLY EXPENSES ----------------

    def total_expenses_by_month(self, month):

        total = 0

        for expense in self.expenses:

            date = datetime.strptime(
                expense.date,
                "%d-%m-%Y"
            )

            expense_month = date.strftime("%m-%Y")

            if expense_month == month:
                total += expense.amount

        return total

    def monthly_expenses(self):

        monthly_totals = {}

        for expense in self.expenses:

            date = datetime.strptime(
                expense.date,
                "%d-%m-%Y"
            )

            month = date.strftime("%m-%Y")

            if month not in monthly_totals:
                monthly_totals[month] = 0

            monthly_totals[month] += expense.amount

        return monthly_totals

    # ---------------- CATEGORY ANALYSIS ----------------

    def category_wise_expenses(self):

        category_totals = {}

        for expense in self.expenses:

            category = expense.category.strip().lower()

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += expense.amount

        return category_totals

    # ---------------- AVERAGE ----------------

    def average_expense(self):

        if not self.expenses:
            return 0

        return self.total_expenses() / len(self.expenses)

    # ---------------- HIGHEST CATEGORY ----------------

    def highest_spending_categories(self):

        category_totals = self.category_wise_expenses()

        if not category_totals:
            return [], 0

        highest_amount = max(category_totals.values())

        highest_categories = [
            category
            for category, amount in category_totals.items()
            if amount == highest_amount
        ]

        return highest_categories, highest_amount

    # ---------------- SAVE / LOAD ----------------

    def to_dict_list(self):

        return [
            expense.to_dict()
            for expense in self.expenses
        ]

    def load_from_dict(self, data):

        self.expenses = []

        for item in data:

            try:
                self.expenses.append(
                    Expense.from_dict(item)
                )

            except (
                KeyError,
                TypeError,
                ValueError
            ):
                continue