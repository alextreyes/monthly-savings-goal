
def main() -> None:

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
        recommended_budget["savings"],
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
    main()
