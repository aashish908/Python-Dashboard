
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def select_excel_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    return file_path

# ---- File selection when imported ----
file_path = select_excel_file()

if not file_path:
    raise Exception("❌ No Excel file selected.")

df = pd.read_excel(file_path)

if df.empty:
    raise Exception("❌ Excel file is empty.")

column_options = [{"label": col, "value": col} for col in df.columns]

__all__ = ["df", "column_options"]

