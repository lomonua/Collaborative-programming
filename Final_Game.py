import random

# === Existing Functions (Unchanged) ===

def evaluate_menu_price(price, base_cost, customer_sensitivity=1.5):
    def estimate_customers(price):
        base_customers = 100
        estimated = int(base_customers * (base_cost / price) ** customer_sensitivity)
        return max(0, estimated)

    estimated_customers = estimate_customers(price)
    revenue = price * estimated_customers
    cost = base_cost * estimated_customers
    profit = revenue - cost

    if profit > 0:
        status = "Profiting"
    elif profit == 0:
        status = "Breaking Even"
    else:
        status = "Losing Money"

    if estimated_customers >= 75:
        satisfaction = "High"
    elif estimated_customers >= 40:
        satisfaction = "Moderate"
    else:
        satisfaction = "Low"

    return {
        "price_charged": round(price, 2),
        "estimated_customers": estimated_customers,
        "total_profit": round(profit, 2),
        "status": status,
        "customer_satisfaction": satisfaction
    }

def calculate_satisfaction(staff_efficiency, cleanliness, wait_time):
    normalized_wait = max(0, 100 - (wait_time * (100 / 30)))
    score = (staff_efficiency * 0.4) + (cleanliness * 0.3) + (normalized_wait * 0.3)
    return round(score, 2)

def trigger_random_event(probability_positive, event_list, restaurant_state):
    if not (0 <= probability_positive <= 1):
        raise ValueError("probability_positive must be between 0 and 1.")
    
    event_type = 'pos.' if random.random() <= probability_positive else 'neg.'

    if not event_list[event_type]:
        return {'event_name': "No Event", 'applied_changes': {}}

    event = random.choice(event_list[event_type])
    applied_changes = {}
    for key, change in event['effect'].items():
        if key in restaurant_state:
            restaurant_state[key] += change
            applied_changes[key] = change

    return {
        'event_name': event['name'],
        'applied_changes': applied_changes
    }

def validate_wages(proposed_wages, min_wages):
    results = {}
    for role, wage in proposed_wages.items():
        if role in min_wages:
            if wage < min_wages[role]:
                results[role] = {
                    'proposed_wage': wage,
                    'status': 'Rejected',
                    'reason': f"Below required min wage of ${min_wages[role]:.2f}/hour"
                }
            else:
                results[role] = {
                    'proposed_wage': wage,
                    'status': 'Approved'
                }
        else:
            results[role] = {
                'proposed_wage': wage,
                'status': 'Approved'
            }
    return results

# === Game Setup ===

restaurant_state = {
    'reputation': 50,
    'sales': 10000
}

event_list = {
    'pos.': [{'name': 'Great Online Review', 'effect': {'reputation': 10}}],
    'neg.': [{'name': 'Customer Illness Report', 'effect': {'reputation': -15}}]
}

min_wages = {
    'Chef': 13.5,
    'Waiter': 12.0,
    'Dishwasher': 9.0
}

# === Game Loop ===

def main_game():
    base_cost = 5
    day = 1
    total_profit = 0

    print("Welcome to Restaurant Tycoon!\n")

    while True:
        print(f"\n--- Day {day} ---")

        try:
            price = float(input("Set your menu price: $"))
            staff_eff = float(input("Staff efficiency (0-100): "))
            cleanliness = float(input("Cleanliness (0-100): "))
            wait_time = float(input("Average wait time (minutes): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        # Menu Evaluation
        menu_result = evaluate_menu_price(price, base_cost)
        print("-> Menu Profit:", menu_result["total_profit"])
        print("-> Customer Satisfaction (from price):", menu_result["customer_satisfaction"])
        total_profit += menu_result["total_profit"]

        # Satisfaction Score
        satisfaction_score = calculate_satisfaction(staff_eff, cleanliness, wait_time)
        print("-> Customer Satisfaction (overall):", satisfaction_score)

        # Wages
        print("\nEnter proposed wages:")
        proposed = {}
        for role in min_wages:
            try:
                wage = float(input(f"  {role} wage: $"))
                proposed[role] = wage
            except ValueError:
                print("Invalid wage. Setting to $0.")
                proposed[role] = 0.0
        wage_results = validate_wages(proposed, min_wages)
        for role, result in wage_results.items():
            print(f"  {role} - {result['status']}", f"({result.get('reason','')})")

        # Random Event
        event_result = trigger_random_event(0.5, event_list, restaurant_state)
        print(f"\nRandom Event: {event_result['event_name']}")
        for k, v in event_result['applied_changes'].items():
            print(f"  {k} changed by {v}")

        print("Current Reputation:", restaurant_state['reputation'])
        print("Current Sales: $", restaurant_state['sales'])

        # Continue?
        cont = input("\nNext day? (y/n): ").strip().lower()
        if cont != 'y':
            break
        day += 1

    print(f"\nThanks for playing! Total Profit: ${total_profit:.2f}")

if __name__ == "__main__":
    main_game()
