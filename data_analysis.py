
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#  ____________________ 4 Define a Dog class ____________________ #

class Dog:
    def __init__(self, time, heart_rate, body_temperature,barking_volume ):
        self.time = time
        self.heart_rate = heart_rate
        self.body_temperature = body_temperature
        self.barking_volume = barking_volume


#  ____________________ 5 Process Dog Data from CSV File ____________________ #


def data_process(file):
    dog_data_list = []

    datafile = pd.read_csv(file)

    # Loop through each row to create Dog objects
    for i in range(len(datafile)):
        # Extract each column directly
        time_str = datafile.loc[i, 'Time']
        heart_rate = datafile.loc[i, 'Heart Rate (bpm)']
        body_temp = datafile.loc[i, 'Body Temperature (°C)']
        barking = datafile.loc[i, 'Barking Volume (dB)']

        # Parse time as a datetime object in HH:MM format
        time = datetime.strptime(time_str, '%H:%M').time()

        # Create a Dog object and add it to the list
        dog = Dog(time, int(heart_rate), int(body_temp), int(barking))
        dog_data_list.append(dog)

    return dog_data_list


def evaluate_dog_conditions(dog_data_list, system, is_dog_ok, output_var="is_dog_ok"):
    """
    Evaluate the condition of each dog based on fuzzy logic and print the results.

    Parameters:
    - dog_data_list: list of Dog objects containing the dog's data.
    - system: the fuzzy control system.
    - output_var: the name of the output variable (default: "is_dog_ok").

    Returns:
    - results: A list of dictionaries with evaluation results for each dog.
    """

    # Initiation
    results = []

    for i in dog_data_list:
        # Create a new simulation for each dog
        sim = ctrl.ControlSystemSimulation(system)

        # Assign all inputs
        sim.input['body_temperature'] = i.body_temperature
        sim.input['heart_rate'] = i.heart_rate
        # sim.input['barking_volume'] = i.barking_volume  # Uncomment if needed

        try:
            # Compute the result
            sim.compute()
            output_value = sim.output[output_var]

            # Calculate membership degrees for all terms in `is_dog_ok`
            membership_levels = {
                label: fuzz.interp_membership(
                    is_dog_ok.universe, is_dog_ok[label].mf, output_value
                )
                for label in is_dog_ok.terms
            }

            # Sort by membership degree (highest first)
            sorted_memberships = sorted(
                membership_levels.items(), key=lambda x: x[1], reverse=True
            )

            # Extracting the top two memberships
            top_two = sorted_memberships[:2]
            top_two_conditions = [
                f"{label} {degree * 100:.0f}%" for label, degree in top_two
            ]

            # Combine the conditions for output
            condition = ", ".join(top_two_conditions)

            # Store the result
            results.append({
                "time": i.time,
                "output_value": output_value,
                "condition": condition
            })

            # Print the result
            print(f"Time: {i.time} | Fuzzification value for {output_var}: {output_value:.2f} -> Condition: {condition}")

        except ValueError as e:
            print(f"Error for dog at time {i.time}: {e}")

    return results





def plot_dog_condition(results):
    """
    Plot a bar chart for the primary dog condition over a 24-hour schedule.

    Parameters:
    - results: List of dictionaries containing 'time' and 'condition' for each hour.
    """
    # Mapping conditions to numeric values and colours
    condition_mapping = {
        "perfect": {"value": 4, "colour": "#a8c9ca"},  # Opal
        "normal": {"value": 3, "colour": "#a6d301"},   # Pistachio
        "need help": {"value": 2, "colour": "#d37401"}, # Orange
        "urgent": {"value": 1, "colour": "#a90120"},    # Dark Red
        "unknown": {"value": 0, "colour": "gray"}      # Default for missing hours
    }

    # Extract reported times and conditions
    reported_times = [result['time'].strftime('%H:%M') for result in results]
    reported_conditions = [
        " ".join(result['condition'].split(",")[0].split()[:-1]).lower()
        for result in results
    ]

    # Create a mapping of time to condition for 24-hour tracking
    time_to_condition = {
        reported_times[i]: reported_conditions[i] if reported_conditions[i] in condition_mapping else "unknown"
        for i in range(len(reported_times))
    }

    # Generate a full 24-hour time schedule
    full_day_times = [f"{hour:02}:00" for hour in range(24)]

    # Fill missing hours with the default condition ("unknown")
    full_day_conditions = [
        time_to_condition[hour] if hour in time_to_condition else "unknown"
        for hour in full_day_times
    ]

    # Convert conditions to numeric values and colours
    numeric_conditions = [condition_mapping[cond]["value"] for cond in full_day_conditions]
    bar_colors = [condition_mapping[cond]["colour"] for cond in full_day_conditions]

    # Plot the bar chart
    plt.figure(figsize=(12, 6))
    bars = plt.bar(full_day_times, numeric_conditions, color=bar_colors, alpha=0.7)

    # Adding labels for clarity
    plt.yticks(
        [val["value"] for val in condition_mapping.values()],
        [key.capitalize() for key in condition_mapping.keys()],
        fontsize=18  # Increased by 50%
    )
    plt.xlabel("Time (Hour)", fontsize=18)  # Increased by 50%
    # plt.ylabel("Condition", fontsize=18)  # Increased by 50% if needed
    plt.title("Dog Condition Over 24 Hours", fontsize=21)  # Increased by 50%
    plt.xticks(rotation=45, fontsize=18)  # Increased by 50%
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the chart
    plt.tight_layout()
    plt.show()



