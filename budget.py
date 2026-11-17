



def calculate_months_to_reach_goal(
    goal_amount: float,
    monthly_savings_50_30_20: float,
    monthly_savings_without_rule: float,
) -> list[int | None]:
    """
    Calculate the number of months needed to achieve a financial goal
    using the 50/30/20 rule or without following it.
    """
    # Raises error if the goal amount less or equal to zero, this should be checked before
    if goal_amount <= 0:
        raise ValueError("The savings goal must be greater than zero.")

    # checks how many months it'll take to achieve this, if module is not 0
    # add 1 since it'll take another month to achieve the goal
    if monthly_savings_50_30_20 > 0:
        months_with_rule = int(
            goal_amount / monthly_savings_50_30_20
        )

        if goal_amount % monthly_savings_50_30_20 != 0:
            months_with_rule += 1
    else:
        months_with_rule = None

    if monthly_savings_without_rule > 0:
        months_without_rule = int(
            goal_amount / monthly_savings_without_rule
        )

        if goal_amount % monthly_savings_without_rule != 0:
            months_without_rule += 1
    else:
        months_without_rule = None

    return [months_with_rule, months_without_rule]


def calculate_remaining_balance_50_30_20(
    income: float,
    needs_expenses: float,
    wants_expenses: float,
    period: int
) -> float:
    """
    Calculate the money remaining after actual expenses
    and the 20% savings allocation over a selected period.
    """

    # Under the 50/30/20 rules, 20% of income is set aside for savings
    monthly_savings = income * 0.2

    # Calculate the money remaining after expenses and savings
    monthly_remaining = income - needs_expenses - wants_expenses - monthly_savings

    # Calculate the remaining balance over the selected period
    period_balance = monthly_remaining * period

    return period_balance


def calculate_monthly_savings_without_rule(
    income: float,
    needs_expenses: float,
    wants_expenses: float,
) -> float:
    """
    Calculate the total amount saved each month without using the 50/30/20 rule.

    Savings are whatever remains after paying needs and wants.
    """
    # Start with the total monthly income available for the budget.
    monthly_savings = income

    # Subtract essential expenses such as rent, bills, and groceries.
    monthly_savings -= needs_expenses

    # Subtract discretionary expenses such as hobbies and entertainment.
    monthly_savings -= wants_expenses

    return monthly_savings


def main():

    print("BUDGET AND SAVINGS CALCULATOR")
    print("Enter your monthly amounts.")

    income = float(input("Monthly income: "))
    needs_expenses = float(input(
        "Monthly needs expenses (rent, bills, groceries): "
    ))
    wants_expenses = float(input(
        "Monthly wants expenses (hobbies, cinema, etc.): "
    ))
    goal = float(input("Your savings goal: "))
    period = int(input(
        "In how many months do you want to track your savings? "
    ))

    # Function 1: 50/30/20 savings recommendation
    recommended_budget = calculate_monthly_savings_50_30_20(income)

    # Function 2: Calculate actual monthly savings
    actual_monthly_savings = calculate_monthly_savings_without_rule(
        income, needs_expenses, wants_expenses
    )

    # Function 3: Compare the time needed to reach the savings goal
    
    goal_comparison = calculate_months_to_reach_goal(
        goal,
        recommended_budget[2],
        actual_monthly_savings,
    )

    # Function 4: Calculate the balance over the selected period
    period_balance = calculate_remaining_balance_50_30_20(
        income, needs_expenses, wants_expenses, period
    )

    print("\nRESULTS")
    print("Results are in!")

    print("Recommended 50/30/20 budget:", recommended_budget)
    print("Actual monthly savings:", actual_monthly_savings)
    print("Time to reach savings goal:", goal_comparison)
    print("Balance over selected period:", period_balance)


if __name__ == "__main__":
    print(calculate_months_to_reach_goal(500,100,200))
    #main()


def calculate_monthly_savings_50_30_20(income: float) -> list[float]:
    """
    Calculate the recommended monthly budget following the 50/30/20 rule.

    The 50/30/20 rule divides monthly income into three categories:
    - 50% for needs (rent, etc.).
    - 30% for wants (hobbies, entertainment, shopping, etc.).
    - 20% for savings and financial goals.

    Args:
        income: The total monthly income.

    Returns:
        A list containing:
        [needs_budget, wants_budget, savings_budget]

    Raises:
        ValueError: If the monthly income is less than or equal to zero.
    """

    # Check that the monthly income is valid
    if income <= 0:
        raise ValueError("Monthly income must be greater than zero.")

    # Calculate 50% of income for essential expenses
    needs_budget = income * 0.50

    # Calculate 30% of income for personal expenses
    wants_budget = income * 0.30

    # Calculate 20% of income for monthly savings
    savings_budget = income * 0.20

    # Store all budget allocations in a list
    recommended_budget = [
        needs_budget,
        wants_budget,
        savings_budget
    ]

    # Return the recommended monthly budget
    return recommended_budget
