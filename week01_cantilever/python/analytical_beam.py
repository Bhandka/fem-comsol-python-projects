# Analytical solution for a cantilever beam under a point load at the free end

E = 170e9  # Pa
L, b, h = 100e-6, 10e-6, 10e-6
I = b*h**3/12
F = 1e-6  # N
delta = F*L**3/(3*E*I)
print(f"Deflection: {delta*1e6:.3f} µm")

import matplotlib.pyplot as plt

# Values (µm)
python_value = delta*1e6  # analytical result
comsol_value = 0.0021809   # COMSOL result

labels = ["Python Analytical", "COMSOL"]
values = [python_value, comsol_value]

plt.figure(figsize=(6,4))
plt.bar(labels, values, color=["steelblue", "orange"])
plt.ylabel("Tip displacement (µm)")
plt.title("Cantilever Beam: Python vs COMSOL (Week 01)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.savefig("comparison_plot.png", dpi=300)
plt.show()
