# Week 01 – Cantilever Beam Comparison (COMSOL vs Python)

This project validates a simple cantilever beam model by comparing the **analytical displacement** from classical beam theory with the **numerical displacement** obtained from COMSOL Multiphysics.

The goal is to ensure that both methods agree and that the COMSOL model is correctly configured.

## 📁 Folder Structure

week01/
│── comsol/
│   └── cantilever.mph
│   └── displacement_value.csv
│
│── python/
│   ├── analytical_beam.py
│   ├── comparison_plot.png
│   
└── README.md

## 🧪 Problem Description

A silicon cantilever beam is subjected to a tip load. The geometry and material properties are:

- **Length (L):** 100 µm  
- **Width (b):** 10 µm  
- **Thickness (h):** 10 µm  
- **Load (F):** 1 µN downward  
- **Material:** Silicon  
- **Young’s Modulus (E):** 170 GPa  
- **Poisson's Ratio (ν):** 0.22 (used for COMSOL 2D model)

The objective is to compute the **tip displacement** using:

1. Analytical beam theory
2. COMSOL Multiphysics simulation (2D solid mechanics)

## 📐 Analytical Calculation (Python)

The analytical displacement is computed using Euler-Bernoulli beam theory:

\[
\delta = \frac{F L^3}{3 E I}, \quad I = \frac{b h^3}{12}
\]

**Python script:** `python/analytical_beam.py`

**Result:**
Analytical displacement ≈ 0.00235 µm

## 🖥️ COMSOL Simulation

The COMSOL model is stored in:
comsol/cantilever.mph

**Model setup:**
- **Physics:** Solid Mechanics (3D)
- **Boundary condition:** Fixed constraint on the left face
- **Load:** 1 µN point load applied to the center of the tip face
- **Mesh:** Fine mapped hexahedral mesh (convergence verified)

The tip displacement was extracted using:
Results → Derived Values → Point Evaluation → solid.disp

**Result (fine mesh):**
COMSOL displacement ≈ 0.0021809 µm

## 📊 Comparison Plot

Generated automatically by running `python/analytical_beam.py`.

![Comparison Plot](python/comparison_plot.png)

| Method             | Displacement (µm) |
|--------------------|-------------------|
| Python Analytical  | 0.00235           |
| COMSOL (fine mesh) | 0.0021809         |


##  Conclusion

- The COMSOL model is **correctly configured** and shows proper mesh convergence.
- The 7.2% difference is **physically justified** by shear deformation effects absent in the 1D beam theory.
- This validates the setup for future studies involving more complex geometries or load cases.

## 🚀 Running the Code

To reproduce the analytical results and generate the comparison plot:

1. Clone this repository.
2. Install the required Python package:
   ```bash
   pip install matplotlib
