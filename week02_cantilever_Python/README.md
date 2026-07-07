# Cantilever Beam FEA Automation with COMSOL and Python

This project automates a COMSOL Multiphysics cantilever beam study using Python. It sweeps several tip-force values, solves the model, compares the finite-element results against analytical beam theory, and exports the results to CSV and a plot image.

## Overview

The workflow includes:

- Loading a saved COMSOL model from the Comsol folder
- Running a force-sweep analysis for multiple tip loads
- Extracting tip deflection values from the COMSOL solution
- Comparing FEA results with the analytical cantilever beam formula
- Saving results to a CSV file and generating a plot

This is a useful example for learning how to combine COMSOL with Python for parametric studies and automated post-processing.

## Project Structure

```text
week02_cantilever_Python/
├── Comsol/
│   └── week02_cantilever_Python.mph
├── Python/
│   └── week02_cantilever_Python.py
├── results/
│   ├── force_sweep_results.csv
│   └── force_sweep_plot.png
└── README.md
```

## What the Script Does

The Python script:

1. Starts a COMSOL client
2. Loads the saved .mph model
3. Defines the beam geometry and material properties
4. Sweeps tip force values in micronewtons
5. Solves the model for each force
6. Computes both FEA and analytical tip deflection
7. Saves the comparison results to CSV
8. Generates a plot for visualization

## Requirements

Before running the script, make sure you have:

- COMSOL Multiphysics installed and licensed
- Python 3.x
- The following Python packages:

```bash
pip install mph numpy pandas matplotlib
```

## Setup

1. Open the project folder.
2. Ensure the COMSOL model file exists at:
   - Comsol/week02_cantilever_Python.mph
3. Make sure the script points to the correct COMSOL model path.
4. Run the Python script from the project root.

## Usage

Run the script with:

```bash
python Python/week02_cantilever_Python.py
```

The script will:

- print a table of FEA vs. analytical deflection results in the terminal
- save the numerical results to results/force_sweep_results.csv
- create a plot image at results/force_sweep_plot.png

## Output Files

- results/force_sweep_results.csv: tabular comparison of force, FEA deflection, analytical deflection, and percent difference
- results/force_sweep_plot.png: visualization of deflection versus applied force

## Notes

- The beam dimensions and material properties are defined in the script and should match the COMSOL model settings.
- The script uses a hard-coded path to the COMSOL model, so you may need to adjust it if you move the project or use a different machine.
- This example is intended for educational and research use.

## License

This project is provided for educational purposes. Feel free to adapt and extend it for your own simulations.
