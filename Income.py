from datetime import datetime


class Income:

    def __init__(self, amount, source, date, income_id=None):

        self.amount = float(amount)
        self.source = source.strip()
        self.date = date.strip()
        self.id = income_id

        if self.amount <= 0:
            raise ValueError(
                "Income amount must be greater than zero."
            )

        datetime.strptime(
            self.date,
            "%d-%m-%Y"
        )

    def get_details(self):

        return (
            f"{self.id:<8} | "
            f"₹{self.amount:>10.2f} | "
            f"{self.source:<15} | "
            f"{self.date:<12} |"
        )

    def to_dict(self):

        return {
            "id": self.id,
            "amount": self.amount,
            "source": self.source,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["amount"],
            data["source"],
            data["date"],
            data.get("id")
        )


class IncomeManager:

    def __init__(self):

        self.incomes = []

    # ---------------- ADD ----------------

    def add_income(self, income):

        if income.id is None:
            income.id = self._next_id()

        self.incomes.append(income)

        print(
            f"Income #{income.id} added successfully."
        )

    def _next_id(self):

        if not self.incomes:
            return 1

        return max(
            income.id
            for income in self.incomes
        ) + 1

    # ---------------- VIEW ----------------

    def view_incomes(self):

        if not self.incomes:
            print("No incomes found.")
            return

        for income in self.incomes:
            print(income.get_details())

    # ---------------- EDIT ----------------

    def edit_income(self, income_id):

        for income in self.incomes:

            if income.id == income_id:

                print("\nCurrent income:")
                print(income.get_details())

                amount = float(
                    input("Enter new amount: ")
                )

                if amount <= 0:
                    raise ValueError(
                        "Income amount must be greater than zero."
                    )

                source = input(
                    "Enter new source: "
                ).strip()

                date = input(
                    "Enter new date (DD-MM-YYYY): "
                ).strip()

                datetime.strptime(
                    date,
                    "%d-%m-%Y"
                )

                income.amount = amount
                income.source = source
                income.date = date

                return True

        return False

    # ---------------- DELETE ----------------

    def delete_income(self, income_id):

        for income in self.incomes:

            if income.id == income_id:

                self.incomes.remove(income)

                return True

        return False

    # ---------------- TOTAL ----------------

    def total_income(self):

        return sum(
            income.amount
            for income in self.incomes
        )

    # ---------------- SAVE / LOAD ----------------

    def to_dict_list(self):

        return [
            income.to_dict()
            for income in self.incomes
        ]

    def load_from_dict(self, data):

        self.incomes = []

        for item in data:

            try:
                self.incomes.append(
                    Income.from_dict(item)
                )

            except (
                KeyError,
                TypeError,
                ValueError
            ):
                continue