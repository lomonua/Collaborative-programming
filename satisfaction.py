def calculate_satisfaction(staff_efficiency, cleanliness, wait_time):
    """
    Abel Degnet
    
    Calculates customer satisfaction score based on weighted input factors.
    This fuction is going to calulate the   
    customer satisfaction score based on the following factors: \
    staff efficiency, cleanliness, and wait time.

    Parameters:
        staff_efficiency (float): Rating from 0 to 100
        cleanliness (float): Rating from 0 to 100
        wait_time (float): Time in minutes (lower is better)

    Returns:
        float: Satisfaction score from 0 to 100
    """
    normalized_wait = max(0, 100 - (wait_time * (100 / 30)))  # max 30 mins wait
    score = (staff_efficiency * 0.4) + (cleanliness * 0.3) + (normalized_wait * 0.3)
    return round(score, 2)

# Test
if __name__ == "__main__":
    result = calculate_satisfaction(85, 90, 10)
    print("Customer Satisfaction Score:", result)