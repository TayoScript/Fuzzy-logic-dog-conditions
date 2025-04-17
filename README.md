# Fuzzy-logic on dog conditions

This project implements a fuzzy logic system to monitor and evaluate the condition of dogs based on physiological and environmental data. The system processes input data, applies fuzzy inference, and visualises the results in a 24-hour schedule.


### Algorithms Included (Features)
The project implements the following optimisation techniques:

1. **Fuzzy Logic-Based Inference**:
   - Uses fuzzy membership functions and inference rules to evaluate the condition of dogs.
   - Inputs are fuzzified, processed through a rule-based control system, and defuzzified to produce meaningful output.

2. **Custom Membership Function Design**:
   - Employs a combination of triangular, Gaussian, and generalised bell-shaped membership functions for flexibility and accuracy.
   - Ensures that input data is mapped effectively into linguistic terms for evaluation.

3. **Data Visualisation Optimisation**:
   - Implements a customised 24-hour condition tracking system.
   - Translates fuzzy output into a visual representation for better interpretability.

These techniques work together to form an end-to-end system that processes data, evaluates conditions, and presents insights efficiently.



## Repository Structure


### Python Scripts
- `main.py`
- `membership_functions.py`
- `data_analysis.py`

### Additional files
- `\data` directory holding the raw input data (raw CSV files)
- `\experiemnt_data` directory holds records of previous run results (outputs) 

### Notebook file
- `project_rundown.ipynb` is a Jupyter notebook file which gives a detailed explanations of the projects codes with example outputs in a notebook format.

### Preferred Python interpreter:
- This project was produced and run via the following IDE: PyCharm.
- Any other IDE which are compatible with python scrips and notebook (.py and .ipynb files) should be able to run the projects source code.

## Running the Project

### Prerequisites
For a fully functioning fuzzy logic system with `skfuzzy`, ensure the following Python packages are installed to be able to run this project (for Python 3.8 or later) :

1. `scikit-fuzzy`: For implementing fuzzy logic systems.
2. `scipy`: For mathematical operations like membership function calculations.
3. `networkx`: For fuzzy rule graph management.
4. `numpy`: For numerical operations.
5. `pandas`: For data table operations.
6. `matplotlib`: For visualisation (optional, for plotting membership functions).

```bash
pip install pandas matplotlib numpy scikit-fuzzy scipy networkx
```

### Required Imports
The required imports of each library modules and scripts are all included in each script. The following imports are for demonstration purposes.
```bash
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import scikit-fuzzy
from typing import List
```

### Method 1: How to run the project algorithm: `main.py`
1. Set Up the Environment:
    - Make sure to download all of the python scripts (.py files) in the repository.
    - Ensure all provided Python scripts are in the same directory and environment.
    - Ensure the `\data` directory is downloaded 
2. Make sure all of the libraries are installed in the same environment.
   - Ensure that the scripts imports are not changed within the source code.
3. Data dictionary appears in the same environment as the scripts.
    - Ensure all input CSV files (e.g., fine_dog_data.csv, sick_dog_data.csv) are placed in the Data directory.
4. Run the `main.py` script 

### Method 2: How to run the notebook: `project_rundown.ipynb`
1. Follows the steps of the methods above to make sure the necessary libraries are installed.
2. Download the Jupyter file, `project_rundown.ipynb`, from the GitHub repository.
3. Set Up the Environment:
    - Make sure that the file is run via an IDE/environment compatible with jupyter notebook files (.ipynb).
    - Make sure the libraries are installed in the same environment as the notebook file.
4. Feel free to read trhough the notebook and run the individual code blocks!

### Method 3: Running the notebook directly here in the project's repository!
1. Just navigate to the repository's file overview on the right.
2. click on the `project_rundown.ipynb` to view its content!

