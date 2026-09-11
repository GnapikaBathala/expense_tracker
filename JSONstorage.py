import json


FILE_NAME = "data.json"


def save_data(
    expense_manager,
    income_manager,
    budget_manager
):

    data = {

        "expenses":
            expense_manager.to_dict_list(),

        "incomes":
            income_manager.to_dict_list(),

        "budgets":
            budget_manager.to_dict_list()
    }

    with open(
        FILE_NAME,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_data(
    expense_manager,
    income_manager,
    budget_manager
):

    try:

        with open(
            FILE_NAME,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        expense_manager.load_from_dict(
            data.get("expenses", [])
        )

        income_manager.load_from_dict(
            data.get("incomes", [])
        )

        budget_manager.load_from_dict(
            data.get("budgets", [])
        )

    except FileNotFoundError:

        # First time running the application.
        pass

    except json.JSONDecodeError:

        print(
            "Warning: data.json is corrupted."
        )