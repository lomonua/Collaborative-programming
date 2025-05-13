import json

def load_wage_rules(file_path):
    """
    Author: Jennifer Carrera
    Techniques: use of json.load()

    Reads a JSON file of role-to-minimum wage mappings and returns a dict.

    Args:
        file_path (str): Path to a JSON file containing a mapping of roles to minimum wages.

    Returns:
        dict: A mapping of role names (str) to minimum wages (float).

    Raises:
        FileNotFoundError: If the file at file_path does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.

    Side effects:
        Opens and reads the specified file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def validate_wages(proposed_wages, min_wages):
    """
    Author: Jennifer Carrera
    Techniques: f-strings containing expressions

    Validates proposed wages against legally required minimum wages.

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

    Identifies roles with missing definitions in either mapping.

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
