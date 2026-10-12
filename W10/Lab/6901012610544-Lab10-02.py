import tkinter as tk
from tkinter import messagebox

#Function to convert Celsius to Fahrenheit
def convert_temperature():
    try:
        #Get the input value from Entry widget and convert to float
        celsius = float(entry_celsius.get())
        
        #Formula to convert Celsius to Fahrenheit: (C * 9/5) + 32
        fahrenheit = (celsius * 9 / 5) + 32
        
        #Display the calculated result on the Label
        label_result.config(text=f"Result: {fahrenheit:.2f} °F", fg="black")
    except ValueError:
        #Show an error pop-up window if input is not a valid number
        messagebox.showerror("Input Error", "Please enter a valid numeric value!")
        #Update label text to indicate invalid input
        label_result.config(text="Invalid input!", fg="red")

#Create the main window
root = tk.Tk()
root.title("Celsius to Fahrenheit Converter")
root.geometry("350x200")

#Label instruction for user input
label_instruction = tk.Label(root, text="Enter temperature in Celsius (°C):")
label_instruction.pack(pady=5)

#Entry widget for inputting Celsius value
entry_celsius = tk.Entry(root, width=20)
entry_celsius.pack(pady=5)

#"Convert" button to trigger calculation
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack(pady=10)

#Label widget for displaying Fahrenheit result
label_result = tk.Label(root, text="Result: -", font=("Arial", 12, "bold"))
label_result.pack(pady=5)

#Start application event loop
root.mainloop()