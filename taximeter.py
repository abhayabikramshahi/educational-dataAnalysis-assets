import tkinter as tk
from tkinter import messagebox

def calculate_fare():
    try:
        distance = float(entry_distance.get())
        waiting_time = float(entry_waiting.get())

        if distance <= 0 or waiting_time < 0:
            raise ValueError("Distance must be positive and waiting time cannot be negative.")
        
        # Initial flag-drop charge
        initial_charge = 60

        # Fare calculation for distance beyond 1 km
        if distance > 1:
            additional_distance = distance - 1
            additional_fare = (additional_distance * 1000 / 200) * 9.80
        else:
            additional_fare = 0

        # Waiting charge
        waiting_charge = waiting_time * 1.75

        # Total fare calculation
        total_fare = initial_charge + additional_fare + waiting_charge

        # Update GUI labels with calculated details
        label_initial.config(text=f"Initial Charge: Rs. {initial_charge:.2f}")
        label_distance_fare.config(text=f"Fare for Additional Distance: Rs. {additional_fare:.2f}")
        label_waiting_charge.config(text=f"Waiting Charge: Rs. {waiting_charge:.2f}")
        label_total_fare.config(text=f"Estimated Total Fare: Rs. {total_fare:.2f}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Set up the GUI
root = tk.Tk()
root.title("Kathmandu Taxi Fare Calculator")

# Labels and entry fields
tk.Label(root, text="Enter distance traveled (in kilometers):").grid(row=0, column=0, padx=10, pady=5)
entry_distance = tk.Entry(root)
entry_distance.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter waiting time (in minutes):").grid(row=1, column=0, padx=10, pady=5)
entry_waiting = tk.Entry(root)
entry_waiting.grid(row=1, column=1, padx=10, pady=5)

# Calculate button
button_calculate = tk.Button(root, text="Calculate Fare", command=calculate_fare)
button_calculate.grid(row=2, columnspan=2, pady=10)

# Result labels
label_initial = tk.Label(root, text="Initial Charge: Rs. 0.00")
label_initial.grid(row=3, columnspan=2, pady=5)

label_distance_fare = tk.Label(root, text="Fare for Additional Distance: Rs. 0.00")
label_distance_fare.grid(row=4, columnspan=2, pady=5)

label_waiting_charge = tk.Label(root, text="Waiting Charge: Rs. 0.00")
label_waiting_charge.grid(row=5, columnspan=2, pady=5)

label_total_fare = tk.Label(root, text="Estimated Total Fare: Rs. 0.00")
label_total_fare.grid(row=6, columnspan=2, pady=10)

# Start Tkinter main loop
root.mainloop()
