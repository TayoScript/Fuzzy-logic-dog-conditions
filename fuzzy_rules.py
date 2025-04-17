import skfuzzy.control as ctrl
from membership_functions import create_membership_functions



# Create Membership Functions
body_temperature, heart_rate, barking_volume, is_dog_ok = create_membership_functions()


# ____________________ 3 Define the Fuzzy Rules ____________________ #

rule1 = ctrl.Rule(body_temperature['normal'] & heart_rate['low'], is_dog_ok['normal'])
rule2 = ctrl.Rule(body_temperature['normal'] & heart_rate['normal'], is_dog_ok['perfect'])
rule3 = ctrl.Rule(body_temperature['normal'] & heart_rate['high'], is_dog_ok['need help'])

rule4 = ctrl.Rule(body_temperature['high'] & heart_rate['low'], is_dog_ok['urgent'])
rule5 = ctrl.Rule(body_temperature['high'] & heart_rate['high'], is_dog_ok['urgent'])
rule6 = ctrl.Rule(body_temperature['high'] & heart_rate['normal'], is_dog_ok['need help'])

rule7 = ctrl.Rule(body_temperature['low'] & heart_rate['low'], is_dog_ok['urgent'])
rule8 = ctrl.Rule(body_temperature['low'] & heart_rate['normal'], is_dog_ok['need help'])
rule9 = ctrl.Rule(body_temperature['low'] & heart_rate['high'], is_dog_ok['urgent'])
