import random
import json

def load_wage_rules(file_path):
    """
    Author: Jennifer Carrera
    Techniques: use of json.load()

    This function loads a JSON file containing wage rule definitions for each role,
    enabling dynamic swapping of minimum-wage policies without modifying code.
    This supports scenarios like regional adjustments or cuisine-specific wage sets.
    
    Args:
        file_path (str): Path to a JSON file containing a mapping of roles to minimum wages.

    Returns:
        dict: A mapping of role names (str) to minimum wages (float).

    Raises:
        FileNotFoundError: If the file at file_path does not exist.

    Side effects:
        Opens and reads the specified file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)
def validate_wages(proposed_wages, min_wages):
    """
    Author: Jennifer Carrera
    Techniques: f-strings containing expressions

    This method performs a in depth check of each proposed wage against its legal minimum,
    returning a structured mapping of roles to their proposed wage, approval status,
    and explanatory messages for any rejections. This function centralizes compliance
    logic and creates human-readable feedback ideal for display or logging.
    
    Args:
        proposed_wages (dict): Mapping of role names (str) to proposed hourly wages (float).
        min_wages (dict): Mapping of role names (str) to legally required minimum wages (float).

    Returns:
        dict: A mapping where each role maps to a dict with keys:
            'proposed_wage' (float): the proposed wage.
            'status' (str): 'Approved' or 'Rejected'.
            'reason' (str, optional): Human-readable reason if rejected.

    Side effects:
        None
    """
    results = {}
    for role, wage in proposed_wages.items():
        if role in min_wages and wage < min_wages[role]:
            reason = f"Below required min wage of ${min_wages[role]:.2f}/hour"
            results[role] = {
                'proposed_wage': wage,
                'status': 'Rejected',
                'reason': reason
            }
        else:
            results[role] = {
                'proposed_wage': wage,
                'status': 'Approved'
            }
    return results

def get_unmatched_roles(proposed_wages, min_wages):
    """
    Author: Jennifer Carrera
    Techniques: set operations (difference)

    Compares the sets of roles between the player's proposed wages and the official
    minimum-wage definitions, identifying any discrepancies. Helps ensure that every
    role has an associated legal minimum and highlights unused definitions.

    Args:
        proposed_wages (dict): Mapping of role names (str) to proposed hourly wages (float).
        min_wages (dict): Mapping of role names (str) to legally required minimum wages (float).

    Returns:
        dict: Contains two sets:
            'undefined_min_wages' (set[str]): Roles in proposed_wages missing in min_wages.
            'unused_min_wages' (set[str]): Roles in min_wages not present in proposed_wages.

    Side effects:
        None
    """
    proposed_set = set(proposed_wages.keys())
    min_set = set(min_wages.keys())
    undefined = proposed_set - min_set
    unused = min_set - proposed_set
    return {
        'undefined_min_wages': undefined,
        'unused_min_wages': unused
    }
    
def evaluate_menu_price(price, base_cost, customer_sensitivity=1.5):
    """
    Made by Lawrence
    Evaluates if the given menu price is profitable and how it affects customer satisfaction.
    Technique demonstrated: Conditional expressions (tenary operator)
    Parameters:
    - price (float): The price the player wants to charge for the menu item.
    - base_cost (float): The cost to produce one unit of the item.
    - customer_sensitivity (float): Higher means customers are more price-sensitive.
    
    Returns:
    - dict: A summary containing:
        - 'price_charged': Rounded menu price.
        - 'estimated_customers': Number of customers expected.
        - 'total_profit': Profit after costs.
        - 'status': Business outcome ("Profiting", "Breaking Even", or "Losing Money").
        - 'customer_satisfaction': Satisfaction level ("High", "Moderate", or "Low").
    """
    def estimate_customers(price):
        """
        example function to simulate customer turnout.
        The higher the price, the fewer the customers (in a non-linear way).
        """
        base_customers = 100
        estimated = int(base_customers * (base_cost / price) ** customer_sensitivity)
        return max(0, estimated)

    estimated_customers = estimate_customers(price)
    revenue = price * estimated_customers
    cost = base_cost * estimated_customers
    profit = revenue - cost

    status =( "Profiting" if profit > 0 else "Breaking Even" if  profit == 0
             else "Losing Money")

    satisfaction = ("High" if estimated_customers >= 75 else "Moderate" if
    estimated_customers >= 40 else "Low")


    return {
        "price_charged": round(price, 2),
        "estimated_customers": estimated_customers,
        "total_profit": round(profit, 2),
        "status": status,
        "customer_satisfaction": satisfaction
    }

"""
Abel Degnet  
Technique Demonstrated – Generator expression used within a weighted scoring system

This function calculates an overall customer satisfaction score based on
staff efficiency, cleanliness, and average wait time. It normalizes the wait
time to a 0–100 scale (lower wait = better) and uses a generator expression
to apply dynamic weights to each metric.
"""

def calculate_satisfaction(staff_efficiency, cleanliness, wait_time):
    # Define weights for each factor
    metric_weights = {
        'staff_efficiency': 0.4,
        'cleanliness': 0.3,
        'wait_time': 0.3
    }

    # Normalize wait time: lower wait increases satisfaction
    metrics = {
        'staff_efficiency': staff_efficiency,
        'cleanliness': cleanliness,
        'wait_time': max(0, 100 - (wait_time * (100 / 30)))
    }

    # Use generator expression to apply weights
    score = sum(metric_weights[key] * metrics[key] for key in metrics)

    return round(score, 2)



def trigger_random_event(probability_positive, event_list, restaurant_state):
    """
    Allie Kang
    Technique Demonstrated - Optional parameters and/or keyword arguments
    
    Triggers a random event (positive or negative) based on provided probability
    and applies its effect to the restaurant "state". It will also return the 
    name and effect of the triggered event.
    
    Parameters:
    - probability_positive (float): value between 0 and 1; chance of a 
    positive event.
    - event_list (dict): contains 'positive' and 'negative' keys correlating 
    to lists of possible events.
                        Each event is a dict with keys: 'name', 'effect'.
    - restaurant_state (dict): current state of the restaurant with keys 
    like 'reputation', 'sales', etc.
    
    Returns:
    - dict with keys: 'event_name' and 'applied_changes'
    """
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
    

def chain_reaction(event_name, event_list, restaurant_state):
    """
    Allie Kang
    Technique Demonstrated - Sequence unpacking
    
    Triggers a follow-up event based on the name of the initial random event
    that was triggered. Only certain events can lead to chain reactions.
    
    Parameters:
    - event_name (str): the name of the original event.
    - event_list (dict): contains all events.
    - restaurant_state (dict): current state of the restaurant.
    
    Returns:
    - dict with keys: 'event_name' and 'applied_changes' (or empty if no chain
    reaction)
    """
    chain_events = {
        "Viral Social Media Post": "Increased Crowds",
        "Food Critic Review": "Blog Feature",
        "Customer Illness Report": "Health Inspection"
    }

    if event_name in chain_events:
        next_event_name = chain_events[event_name]
        for event_type in ['pos.', 'neg.']:
            for event in event_list[event_type]:
                if event['name'] == next_event_name:
                    applied_changes = {}
                    for key, change in event['effect'].items():
                        if key in restaurant_state:
                            restaurant_state[key] += change
                            applied_changes[key] = change
                    return {
                        'event_name': event['name'],
                        'applied_changes': applied_changes
                    }
    
    return {
        'event_name': "No Chain Reaction",
        'applied_changes': {}
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
def manage_inventory(inventory, estimated_customers, portion_size=1):
    """
    Made by Lawrence
    Updates inventory based on customer demand and spoilage.
    Technique demonstrated: Comprehension

    Parameters:
    - inventory (dict): Ingredients and their quantities.
    - estimated_customers (int): Number of customers that day.
    - portion_size (int): Amount of each ingredient used per customer.

    Returns:
    - dict: Updated inventory after usage and spoilage.
    """
    spoilage_rate = 0.05

    updated_inventory = {
        item: max(0, quantity - (estimated_customers * portion_size) - int(quantity * spoilage_rate))
        for item, quantity in inventory.items()
    }

    return updated_inventory
"""
Abel Degnet
Revenue Algorithm Simulation
Technique Demonstrated – Use of json.dumps() to format structured output

This code will help in understanding the impact of different factors on the 
restaurant's revenue and can be used to make informed decisions about pricing, 
marketing, and operations.

Functions:
    simulate_day(): Simulates one day of operations, including random events 
    and profit calculation.

Execution:
    When run as a script, it will simulate 5 days and print the results.
"""



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


# === Game Setup ===

restaurant_state = {
    'reputation': 50,
    'sales': 10000
}

event_list = {
    'pos.': [
        {'name': 'Great Online Review', 'effect': {'reputation': 10}},
        {'name': 'Viral Social Media Post', 'effect': {'reputation': 15}},
        {'name': 'Blog Feature', 'effect': {'sales': 3000}}
    ],
    'neg.': [
        {'name': 'Customer Illness', 'effect': {'reputation': -15}},
        {'name': 'Health Inspection', 
            'effect': {'reputation': -10, 'sales': -2000}},
        {'name': 'Increased Crowds', 'effect': {'reputation': -5, 'sales': 1000}}
    ]
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

    # Inventory initialization
    inventory = {
        'meat': 300,
        'vegetables': 200,
        'rice': 150
    }

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

        # Inventory Update
        inventory = manage_inventory(inventory, menu_result["estimated_customers"])
        print("-> Inventory after service:", inventory)

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

        # Chain Reaction
        chain_result = chain_reaction(event_result['event_name'], event_list, restaurant_state)
        if chain_result['event_name'] != "No Chain Reaction":
            print(f"Chain Reaction Event: {chain_result['event_name']}")
            for k, v in chain_result['applied_changes'].items():
                print(f"  {k} changed by {v}")
            print("Updated Reputation:", restaurant_state['reputation'])
            print("Updated Sales: $", restaurant_state['sales'])

        # Revenue Simulation
        print("\n--- Revenue Simulation ---")
        daily_report = simulate_day()
        print(f"  Event: {daily_report['event']}")
        print(f"  Total Income: ${daily_report['total_income']}")
        print(f"  Total Expenses: ${daily_report['total_expenses']}")
        print(f"  Daily Profit: ${daily_report['daily_profit']}")

        # Continue?
        cont = input("\nNext day? (y/n): ").strip().lower()
        if cont != 'y':
            break
        day += 1

    print(f"\nThanks for playing! Total Profit: ${total_profit:.2f}")

if __name__ == "__main__":
    main_game()
