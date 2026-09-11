class Budget:

    def __init__(self, month, limit):

        self.month = month.strip()
        self.limit = float(limit)

        if self.limit <= 0:
            raise ValueError(
                "Budget limit must be greater than zero."
            )

    def remaining(self, spent):

        return self.limit - float(spent)

    def percentage_used(self, spent):

        return (float(spent) / self.limit) * 100

    def to_dict(self):

        return {
            "month": self.month,
            "limit": self.limit
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            data["month"],
            data["limit"]
        )


class BudgetManager:

    def __init__(self):

        self.budgets = {}

    # ---------------- SET BUDGET ----------------

    def set_budget(self, month, limit):

        self.budgets[month] = Budget(
            month,
            limit
        )

    # ---------------- GET BUDGET ----------------

    def get_budget(self, month):

        return self.budgets.get(month)

    # ---------------- VIEW BUDGETS ----------------

    def view_budgets(self):

        if not self.budgets:
            print("No budgets found.")
            return

        for budget in self.budgets.values():

            print(
                f"{budget.month:<12} | "
                f"₹{budget.limit:>10.2f}"
            )

    # ---------------- SAVE / LOAD ----------------

    def to_dict_list(self):

        return [
            budget.to_dict()
            for budget in self.budgets.values()
        ]

    def load_from_dict(self, data):

        self.budgets = {}

        for item in data:

            try:

                budget = Budget.from_dict(item)

                self.budgets[budget.month] = budget

            except (
                KeyError,
                TypeError,
                ValueError
            ):
                continue