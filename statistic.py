import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk

def calculate_statistics():
    try:
        # Get user input and convert to list of integers
        values = list(map(int, value_entry.get().split(',')))
        frequencies = list(map(int, freq_entry.get().split(',')))

        if len(values) != len(frequencies):
            messagebox.showerror("Input Error", "Values and Frequencies must have the same length.")
            return

        # Create DataFrame
        data = pd.DataFrame({'Value': values, 'Frequency': frequencies})

        # Calculate FX (Value * Frequency)
        data['FX'] = data['Value'] * data['Frequency']

        # Calculate Cumulative Frequency (CF)
        data['CF'] = data['Frequency'].cumsum()

        # Display results in the table
        for row in table.get_children():
            table.delete(row)
        for i, row in data.iterrows():
            table.insert("", "end", values=(row['Value'], row['Frequency'], row['FX'], row['CF']))

        # Display total values
        total_fx = data['FX'].sum()
        total_f = data['Frequency'].sum()
        mean = total_fx / total_f if total_f > 0 else 0

        result_label.config(text=f"Total F: {total_f}, Total FX: {total_fx}, Mean: {mean:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values separated by commas.")

# GUI Setup
root = tk.Tk()
root.title("Statistics Calculator")

# Input fields
tk.Label(root, text="Enter Values (comma-separated):").grid(row=0, column=0, padx=10, pady=5)
value_entry = tk.Entry(root, width=40)
value_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Frequencies (comma-separated):").grid(row=1, column=0, padx=10, pady=5)
freq_entry = tk.Entry(root, width=40)
freq_entry.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate_statistics)
calc_button.grid(row=2, columnspan=2, pady=10)

# Table to display results
columns = ('Value', 'Frequency', 'FX', 'CF')
table = ttk.Treeview(root, columns=columns, show="headings", height=8)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

table.grid(row=3, columnspan=2, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="Total F: 0, Total FX: 0, Mean: 0.00")
result_label.grid(row=4, columnspan=2, pady=10)

# Start Tkinter main loop
root.mainloop()
