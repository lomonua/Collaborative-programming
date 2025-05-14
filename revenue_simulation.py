"""
Abel Degnet
Revenue Algorithm Simulation

This code will help in understanding the impact of different factors on the 
restaurant's revenue and can be used to make informed decisions about pricing, 
marketing, and operations.

Functions:
    simulate_day(): Simulates one day of operations, including random events 
    and profit calculation.

Execution:
    When run as a script, it will simulate 5 days and print the results.
"""

import random

# Income and expense history
profit_history = []

def simulate_day():
    """
    Simulates a single day of restaurant operations.
    Calculates income and expenses, applies a random event,
    and returns the daily profit with event context.

    Returns:
        dict: Contains event, total income, total expenses, and daily profit.
    """
    # Income breakdown
    income = {
        'food_sales': 1200,
        'drink_sales': 450,
        'promotions': 200,
        'delivery': 350
    }

    # Expense breakdown
    expenses = {
        'wages': 800,
        'food_costs': 300,
        'maintenance': 100,
        'utilities': 150,
        'marketing': 75
    }

    # Simulate random event
    event = random.choice(['none', 'bad_review', 'promo_success', 
                           'utility_surge'])

    if event == 'bad_review':
        income['food_sales'] *= 0.9  
    elif event == 'promo_success':
        income['promotions'] += 150
    elif event == 'utility_surge':
        expenses['utilities'] += 50

    total_income = sum(income.values())
    total_expenses = sum(expenses.values())
    daily_profit = total_income - total_expenses

    # Store the result
    profit_history.append({
        'event': event,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'daily_profit': daily_profit
    })

    return profit_history[-1]

# Simulate a few days to test
if __name__ == '__main__':
    for _ in range(5):
        result = simulate_day()
        print(result)
