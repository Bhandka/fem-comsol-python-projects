"""
Week 2, Part 2: Automating the COMSOL cantilever model with Python.
Now with: CSV export + plot of the results.

Prerequisite:
  pip install mph numpy pandas matplotlib
"""

import os
import mph
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Connect to COMSOL and load your saved model ---
client = mph.start()
model = client.load(r'D:\fem-comsol-python-projects\week02_cantilever_Python\Comsol\week02_cantilever_Python.mph')

# --- 2. Beam parameters (must match what you set in the GUI) ---
W = 100e-6   # length, m
H = 10e-6    # height, m
T = 10e-6     # thickness, m (out of plane, for 2D model)
E = 170e9    # Young's modulus, Pa (approx, silicon)
I = (T * H**3) / 12  # second moment of area

# --- 3. Sweep tip force values ---
forces_uN = [0.5, 1.0, 2.0, 5.0, 10.0]  # in micronewtons

print(f"{'F (uN)':>10} | {'FEA tip defl (nm)':>18} | {'Analytical (nm)':>16} | {'% diff':>7}")
print("-" * 60)

results = []  # <-- collect every row here so we can save/plot afterward

for F_uN in forces_uN:
    F = F_uN * 1e-6  # convert to newtons

    model.parameter('F', f'{F_uN}[uN]')
    model.solve()

    v_values = np.array(model.evaluate('v'))
    fea_defl_m = v_values[np.argmax(np.abs(v_values))]
    fea_defl_nm = fea_defl_m * 1e9

    analytical_m = F * W**3 / (3 * E * I)
    analytical_nm = analytical_m * 1e9

    pct_diff = 100 * abs(abs(fea_defl_nm) - analytical_nm) / analytical_nm

    print(f"{F_uN:>10.1f} | {fea_defl_nm:>18.3f} | {analytical_nm:>16.3f} | {pct_diff:>6.1f}%")

    # --- save this row's data into the results list ---
    results.append({
        'force_uN': F_uN,
        'fea_deflection_nm': fea_defl_nm,
        'analytical_deflection_nm': analytical_nm,
        'pct_diff': pct_diff
    })

client.remove(model)

# --- 4. Save results to CSV ---
os.makedirs('results', exist_ok=True)  # creates the folder if it doesn't exist yet
df = pd.DataFrame(results)
csv_path = 'results/force_sweep_results.csv'
df.to_csv(csv_path, index=False)
print(f"\nSaved: {csv_path}")

# --- 5. Plot: deflection vs force, FEA vs analytical ---
fig, ax = plt.subplots(figsize=(7, 5))

# Use abs() on FEA values for plotting, since sign just indicates direction
ax.plot(df['force_uN'], df['fea_deflection_nm'].abs(), 'o-', label='FEA (COMSOL)')
ax.plot(df['force_uN'], df['analytical_deflection_nm'], 's--', label='Analytical (beam theory)')

ax.set_xlabel('Tip force (µN)')
ax.set_ylabel('Tip deflection (nm)')
ax.set_title('Cantilever Tip Deflection vs. Applied Force')
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()

plot_path = 'results/force_sweep_plot.png'
fig.savefig(plot_path, dpi=150)
print(f"Saved: {plot_path}")

plt.show()  # opens the plot in a window - close it to end the script