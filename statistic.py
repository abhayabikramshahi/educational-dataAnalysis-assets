import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
from textblob import TextBlob

# Function to calculate statistics
def calculate_statistics():
    try:
        values = list(map(int, value_entry.get().split(',')))
        frequencies = list(map(int, freq_entry.get().split(',')))

        if len(values) != len(frequencies):
            messagebox.showerror("Input Error", "Values and Frequencies must have the same length.")
            return

        data = pd.DataFrame({'Value': values, 'Frequency': frequencies})
        data['FX'] = data['Value'] * data['Frequency']
        data['CF'] = data['Frequency'].cumsum()

        for row in table.get_children():
            table.delete(row)
        for _, row in data.iterrows():
            table.insert("", "end", values=(row['Value'], row['Frequency'], row['FX'], row['CF']))

        total_fx = data['FX'].sum()
        total_f = data['Frequency'].sum()
        mean = total_fx / total_f if total_f > 0 else 0

        result_label.config(text=f"Total F: {total_f}, Total FX: {total_fx}, Mean: {mean:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values separated by commas.")

# Function for essay correction
def correct_essay():
    essay_text = essay_entry.get("1.0", tk.END).strip()

    if not essay_text:
        messagebox.showerror("Input Error", "Please enter an essay to check.")
        return

    corrected_essay = TextBlob(essay_text).correct()
    corrected_text.delete("1.0", tk.END)
    corrected_text.insert(tk.END, corrected_essay)

# Set up the main window
root = tk.Tk()
root.title("Multi-Feature Application")
root.geometry("600x500")
root.resizable(False, False)

# Create a tabbed interface
tab_control = ttk.Notebook(root)

# Tab 1: Statistics Calculator
stat_tab = ttk.Frame(tab_control)
tab_control.add(stat_tab, text="Statistics Calculator")

# Input section for statistics
input_frame = ttk.LabelFrame(stat_tab, text="Input Data", padding=(10, 5))
input_frame.grid(row=0, column=0, padx=20, pady=10, columnspan=2, sticky="ew")

tk.Label(input_frame, text="Enter Values (comma-separated):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
value_entry = ttk.Entry(input_frame, width=35)
value_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter Frequencies (comma-separated):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
freq_entry = ttk.Entry(input_frame, width=35)
freq_entry.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
calc_button = ttk.Button(stat_tab, text="Calculate", command=calculate_statistics)
calc_button.grid(row=1, columnspan=2, pady=10)

# Table to display results
result_frame = ttk.LabelFrame(stat_tab, text="Results", padding=(10, 5))
result_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="ew")

columns = ('Value', 'Frequency', 'FX', 'CF')
table = ttk.Treeview(result_frame, columns=columns, show="headings", height=6)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120, anchor="center")

table.pack(padx=10, pady=5)

# Result label
result_label = tk.Label(stat_tab, text="Total F: 0, Total FX: 0, Mean: 0.00", font=("Arial", 12, "bold"))
result_label.grid(row=3, columnspan=2, pady=10)

# Tab 2: Essay Writing Helper
essay_tab = ttk.Frame(tab_control)
tab_control.add(essay_tab, text="Essay Writing Helper")

# Essay input section
essay_frame = ttk.LabelFrame(essay_tab, text="Write your Essay", padding=(10, 5))
essay_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

essay_entry = tk.Text(essay_frame, height=8, width=60)
essay_entry.pack(padx=10, pady=5)

# Correct essay button
correct_button = ttk.Button(essay_tab, text="Correct Essay", command=correct_essay)
correct_button.grid(row=1, pady=10)

# Corrected essay section
corrected_frame = ttk.LabelFrame(essay_tab, text="Corrected Essay", padding=(10, 5))
corrected_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

corrected_text = tk.Text(corrected_frame, height=8, width=60, bg="#e8e8e8", state="normal")
corrected_text.pack(padx=10, pady=5)

# Pack the tab control
tab_control.pack(expand=1, fill="both")

# Start Tkinter main loop
root.mainloop()
