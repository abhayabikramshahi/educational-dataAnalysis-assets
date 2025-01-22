import tkinter as tk
from tkinter import messagebox

def calculate_fare():
    try:
        distance = float(entry_distance.get())
        if distance <= 0:
            raise ValueError("Distance must be positive.")
        
        # Initial flag-drop charge
        fare = 60
        
        # Calculate fare based on distance
        if distance > 1:
            additional_distance = distance - 1
            additional_fare = (additional_distance * 1000 / 200) * 9.80
            fare += additional_fare
        
        label_result.config(text=f"Estimated Fare: Rs. {fare:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Set up the GUI
root = tk.Tk()
root.title("Kathmandu Taxi Fare Calculator")

label_instruction = tk.Label(root, text="Enter distance traveled (in kilometers):")
label_instruction.pack(pady=10)

entry_distance = tk.Entry(root)
entry_distance.pack(pady=5)

button_calculate = tk.Button(root, text="Calculate Fare", command=calculate_fare)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="Estimated Fare: Rs. 0.00")
label_result.pack(pady=10)

root.mainloop()
