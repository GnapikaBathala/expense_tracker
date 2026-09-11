import csv


def export_expenses_to_csv(expenses, filename="expenses.csv"):

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["id", "amount", "category", "description", "date"]
        )

        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense.to_dict())


def export_incomes_to_csv(incomes, filename="incomes.csv"):

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["id", "amount", "source", "date"]
        )

        writer.writeheader()

        for income in incomes:
            writer.writerow(income.to_dict())


def export_budgets_to_csv(budgets, filename="budgets.csv"):

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=["month", "limit"]
        )

        writer.writeheader()

        for budget in budgets:
            writer.writerow(budget.to_dict())