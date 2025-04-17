import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def create_membership_functions():
    # 1. Create Antecedents and Consequents
    body_temperature = ctrl.Antecedent(np.arange(34.0, 44.0, 0.1), "body_temperature")
    heart_rate = ctrl.Antecedent(np.arange(0, 190, 1), "heart_rate")
    barking_volume = ctrl.Antecedent(np.arange(0, 113, 1), "barking_volume")
    is_dog_ok = ctrl.Consequent(np.arange(0, 100, 1), "is_dog_ok")

    # 2. Define Membership Functions

    # 2.1 Body Temperature (Triangular and Gaussian MF)
    body_temperature['low'] = fuzz.trimf(body_temperature.universe, [34, 34, 38.3])
    body_temperature['normal'] = fuzz.gaussmf(body_temperature.universe, mean=38.75, sigma=0.6)
    body_temperature['high'] = fuzz.trimf(body_temperature.universe, [37.75, 44, 44])  # 37.75

    # 2.2 Heart Rate (Gaussian MF)
    heart_rate['low'] = fuzz.gaussmf(heart_rate.universe, mean=50, sigma=20)
    heart_rate['normal'] = fuzz.gbellmf(heart_rate.universe, a=40, b=3, c=95)
    heart_rate['high'] = fuzz.gaussmf(heart_rate.universe, mean=140, sigma=20)  #140

    # 2.3 Barking Volume (Gaussian MF)
    barking_volume['quiet'] = fuzz.gaussmf(barking_volume.universe, mean=0, sigma=25)
    barking_volume['moderate'] = fuzz.gaussmf(barking_volume.universe, mean=56.5, sigma=20)
    barking_volume['loud'] = fuzz.gaussmf(barking_volume.universe, mean=113, sigma=25)

    # 2.4 Is Dog OK (MF)
    is_dog_ok["perfect"] = fuzz.gaussmf(is_dog_ok.universe, mean=10, sigma=10)
    is_dog_ok["normal"] = fuzz.gbellmf(is_dog_ok.universe, a=10, b=3, c=20)
    #is_dog_ok["normal"] = fuzz.trimf(is_dog_ok.universe, [20, 30, 50])
    is_dog_ok["need help"] = fuzz.gaussmf(is_dog_ok.universe, mean=50, sigma=10)
    is_dog_ok["urgent"] = fuzz.gaussmf(is_dog_ok.universe, mean=80, sigma=10)

    return body_temperature, heart_rate, barking_volume, is_dog_ok


def plot_membership_functions(fuzzy_variable):
    # Map variable labels to their corresponding names and units
    variable_info = {
        "body_temperature": {"name": "Body Temperature", "unit": "°C"},
        "heart_rate": {"name": "Heart Rate", "unit": "BPM"},
        "barking_volume": {"name": "Barking Volume", "unit": "dB"},
        "is_dog_ok": {"name": "Dog's Condition", "unit": "Score"}
    }

    # Determine the name and unit for the given variable
    variable_name = variable_info.get(fuzzy_variable.label, {}).get("name", "Variable")
    variable_unit = variable_info.get(fuzzy_variable.label, {}).get("unit", "units")

    # Plot Membership Functions for the given fuzzy variable
    plt.figure(figsize=(10, 6))
    for label, membership_function in fuzzy_variable.terms.items():
        plt.plot(fuzzy_variable.universe, membership_function.mf, label=label, linewidth=2)

    # Add titles and labels with increased font size
    plt.title(f"Fuzzification of {variable_name}", fontsize=18)  # Increased by 50%
    plt.xlabel(f"{variable_name} ({variable_unit})", fontsize=15)  # Increased by 50%
    plt.ylabel("Membership Degree", fontsize=15)  # Increased by 50%
    plt.legend(loc="upper right", fontsize=12)  # Increased by 50%
    plt.grid(True)
    plt.tight_layout()  # Remove unnecessary whitespace
    plt.show()
