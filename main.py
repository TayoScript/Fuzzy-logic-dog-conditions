import skfuzzy.control as ctrl
from membership_functions import create_membership_functions, plot_membership_functions
from data_analysis import data_process, evaluate_dog_conditions, plot_dog_condition
from fuzzy_rules import (rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,)

# Create Membership Functions
body_temperature, heart_rate, barking_volume, is_dog_ok = create_membership_functions()

# Plot Membership Functions
plot_membership_functions(body_temperature)
plot_membership_functions(heart_rate)
plot_membership_functions(barking_volume)
plot_membership_functions(is_dog_ok)


#_______ create a control system and simulation _______ #
system = ctrl.ControlSystem([rule1,rule2,rule3, rule4, rule5, rule6, rule7, rule8, rule9])



#  ____________________  Running the Project ____________________ #
dog_1='Data/fine_dog_data.csv'
dog_2='Data/sick_dog_data.csv'
dog_3='Data/critical_dog_data.csv'

# change the number of the dog_ variable to change the data
dog_1_data_list = data_process(dog_3)

results = evaluate_dog_conditions(dog_1_data_list, system, is_dog_ok)
plot_dog_condition(results)



