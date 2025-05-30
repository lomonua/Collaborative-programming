-------------------
Restaurant Tycoon Simulator
Welcome to Restaurant Tycoon, a command-line game where you run a restaurant, set prices, manage staff wages, respond to random events, and try to maintain customer satisfaction and profitability.
Repository Contents
-------------------
- Final_Game.py - Contains all gameplay logic and supporting functions. This is the main script you run to play the game.
- README.md - This document. Contains instructions and documentation for understanding and running the game.
How to Run the Program ---------------------- Requirements:
- Python 3
- Standard libraries only: random, json
Running the Game:
From your terminal, navigate to the directory containing Final_Game.py and run:
python3 Final_Game.py if you are on a Mac or python main_game.py if you are on Windows device
You will be prompted each game day to input:
- Your menu price (float)
- Staff efficiency score (0-100)
- Cleanliness score (0-100)
- Average wait time in minutes (float)
- Proposed hourly wages for Chef, Waiter, and Dishwasher
To continue to the next day, type 'y'. Type 'n' to quit.
How to Play and Understand the Output -------------------------------------
Each game loop simulates one day at your restaurant.
You will:
1. Set your menu price - Impacts how many customers visit.
2. Enter cleanliness, staff efficiency, and wait time - Affects satisfaction.
3. Propose staff wages - Must meet or exceed minimum wage to be accepted. 4. Experience random events - Good or bad events affect reputation and sales. 5. Possibly trigger chain reactions - Certain events lead to follow-ups.
6. Review summary - See how your decisions impact profit and reputation.
Command-Line Interface Details ------------------------------
Required Inputs:
- price (float): Menu price, e.g., 12.99
- staff_efficiency (float): Between 0 and 100 - cleanliness (float): Between 0 and 100
- wait_time (float): Any positive number - wages (float): For each staff role

Optional Configuration (in code):
- base_cost: The food production cost per item (default is 5).
- min_wages: A dictionary setting legal minimum wages for staff.

|   Method/Function   |   Primary author  |   Techniques demonstrated  |
|---------------------|-------------------|----------------------------|
| trigger_random_event| Allie Kang        | Optional parameters/args   |
|---------------------|-------------------|----------------------------|
| chain_reaction      | Allie Kang        | Sequence unpacking         |
|---------------------|-------------------|----------------------------|
| validate_wages      | Jennifer Carrera  | f-strings containing       |
|                                         | expressions                |
|---------------------|-------------------|----------------------------|
|load_wage_rules      | Jennifer Carrera  | Use of json.load()         |
|---------------------|-------------------|----------------------------|
|get_unmatched_roles  | Jennifer Carrera  | Set operations             |
|---------------------|-------------------|----------------------------|
|evaluate_menu_price  | Lawrence Omonua   | Conditional expression     |
|---------------------|-------------------|----------------------------|
|manage_inventory     | Lawrence Omonua   | Comprehension              | 
|---------------------|-------------------|----------------------------|
|simulate_day         | Abel Degnet       |Use of json.dumps()         |
|---------------------|-------------------|----------------------------|
|calculate_satisfaction| Abel Degnet      |Generator expressions       |
|---------------------|-------------------|----------------------------|


Allie Kang (trigger_random_event, chain_reaction): Optional parameters and/or keyword arguments, Sequence unpacking
Jennifer Carrera(validate_wages, load_wage_rules, get_unmatched_roles): f-strings containing expressions, use of json.load()
Lawrence Omonua (evaluate_menu_price, manage_inventory): Conditional expression (tenary operator), comprehension 
Abel Degnet (simulate_day, calculate_satisfaction): Use of json.dumps(), generator expressions

End of Game
-----------
After each session, the game shows your total profit and ends.
Thanks for playing!

