def validate_wages (proposed_wages, min_wages):
    """
    Checks whether each proposed wage meets the minimum wage requirements.

    Parameters:
        proposed_wages(dict): maps role(str) to proposed hourly wage (float)
        min_wages (dict): maps role (str) to legal minimum wage (float)
    
    Returns:
        dict: the keys are roles that each match to a dict that contains:
            'proposed_wage' (float)
            'status' ('Approved' or 'Rejected')
            'reason' (str, only if rejected) 
    """
    results = {}
    
    for role, wage in proposed_wages.items():
        if role in min_wages:
            if wage < min_wages[role]:
                results[role] = {
                    'proposed_wage': wage, 
                    'status': 'Rejected',
                    'reason': f"Below required min wage of ${min_wages[role]:.2f}/hour"}
            else:
                results[role] = {'proposed_wage': wage, 'status': 'Approved'}
                
        else:
            results[role] = {'proposed_wage': wage, 'status': 'Approved'}
            
    return results