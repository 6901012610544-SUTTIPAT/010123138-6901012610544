import tkinter as tk

#Global variable to store the counter number
counter_value = 0

#Function to increase the count by 1
def increase():
    global counter_value
    counter_value += 1
    label.config(text=str(counter_value))

#Function to decrease the count by 1
def decrease():
    global counter_value
    counter_value -= 1
    label.config(text=str(counter_value))

#Function to reset the count back to 0
def reset():
    global counter_value
    counter_value = 0
    label.config(text=str(counter_value))

#Create the main window
root = tk.Tk()
root.title("Counter App")
root.geometry("300x220")

#Label displaying the initial number starting at 0
label = tk.Label(root, text="0", font=("Arial", 32))
label.pack(pady=10)

#"Increase" button to add 1
btn_increase = tk.Button(root, text="Increase", command=increase, width=12)
btn_increase.pack(pady=3)

#"Decrease" button to subtract 1
btn_decrease = tk.Button(root, text="Decrease", command=decrease, width=12)
btn_decrease.pack(pady=3)

#"Reset" button to set value back to 0
btn_reset = tk.Button(root, text="Reset", command=reset, width=12)
btn_reset.pack(pady=3)

#Start the application loop
root.mainloop()