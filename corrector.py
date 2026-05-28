import pandas as pd
import numpy as np
import os
from tkinter import Tk, filedialog

SanCarlos_d18O_true = 5.226
SanCarlos_D17O_true = -52
Lambda = 0.528

# --- Open file explorer to choose Excel file ---
root = Tk()
root.withdraw()  # hide main tkinter window

file_path = filedialog.askopenfilename(
    title="Select the Excel file",
    filetypes=[("Excel files", "*.xlsx *.xls")]
)

if not file_path:
    raise SystemExit("No file selected.")

# --- Read Excel ---
primitive_data = pd.read_excel(file_path)

# --- Filter San Carlos rows ---
SanCarlos_filter = primitive_data.loc[
    primitive_data["SampleType"] == "San Carlos Olivine (olivine): 0820M"
]

# --- Calculate means ---
d18O_mean = SanCarlos_filter["d18O"].mean()
CapD17O_mean = SanCarlos_filter["CapD17O"].mean()

# --- Apply corrections ---
cd_d18O = primitive_data["d18O"] - (d18O_mean - SanCarlos_d18O_true)
cd_D17O = primitive_data["CapD17O"] - (CapD17O_mean - SanCarlos_D17O_true)

dp18O = 1000 * np.log(cd_d18O / 1000 + 1)
dp17O = dp18O * Lambda + cd_D17O / 1000
cd_d17O = 1000 * (np.exp(dp17O / 1000) - 1)

# --- Add new columns to dataframe ---
primitive_data["cd_d18O"] = cd_d18O
primitive_data["cd_D17O"] = cd_D17O
primitive_data["dp18O"] = dp18O
primitive_data["dp17O"] = dp17O
primitive_data["cd_d17O"] = cd_d17O

# --- Create new filename with "_corrected" ---
directory = os.path.dirname(file_path)
filename = os.path.basename(file_path)
name, ext = os.path.splitext(filename)

new_file = os.path.join(directory, f"{name}_corrected{ext}")

# --- Save new Excel file ---
primitive_data.to_excel(new_file, index=False)

print(f"Corrected file saved as:\n{new_file}")