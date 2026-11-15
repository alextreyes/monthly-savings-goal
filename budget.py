



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
