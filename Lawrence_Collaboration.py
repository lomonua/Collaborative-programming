def evaluate_menu_price(price, base_cost, customer_sensitivity=1.5):
    """
    Evaluates if the given menu price is profitable and how it affects customer satisfaction.
    
    Parameters:
    - price (float): The price the player wants to charge for the menu item.
    - base_cost (float): The cost to produce one unit of the item.
    - customer_sensitivity (float): Higher means customers are more price-sensitive.
    
    Returns:
    - dict: Summary of profit/loss, customer satisfaction level, and status.
    """

    def estimate_customers(price):
        """
        example function to simulate customer turnout.
        The higher the price, the fewer the customers (in a non-linear way).
        """
        base_customers = 100  # Ideal number at base price
        # Simulate drop in customers with higher prices
        estimated = int(base_customers * (base_cost / price) ** customer_sensitivity)
        return max(0, estimated)  # makes sure its a non-negative number

    estimated_customers = estimate_customers(price)
    revenue = price * estimated_customers
    cost = base_cost * estimated_customers
    profit = revenue - cost

    # Determine business health
    if profit > 0:
        status = "Profiting"
    elif profit == 0:
        status = "Breaking Even"
    else:
        status = "Losing Money"

    # Determine customer satisfaction
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

result = evaluate_menu_price(price=9.50, base_cost=5)
print(result)
