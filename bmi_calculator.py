"""GUI Adaptation of BMI Calculator"""
import tkinter

# Constants
POUNDS = 1
KILOGRAMS = 2
INCHES = 1
METERS = 2

# Functions
def calculate_bmi(weight, height, weight_unit, height_unit):
    """Calculates BMI based on units selected."""
    if weight_unit == POUNDS and height_unit == INCHES:
        return round((weight / (height ** 2)) * 703, 2)
    elif weight_unit == KILOGRAMS and height_unit == METERS:
        return round(weight / (height ** 2), 2)
    return None

def convert_bmi():
    """Gets user input and updates the BMI display."""
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height, weight_metric.get(), height_metric.get())

        if bmi is not None:
            canvas.itemconfig(bmi_display, text=f"{bmi}")
        else:
            canvas.itemconfig(bmi_display, text="Invalid units")
    except ValueError as e:
        canvas.itemconfig(bmi_display, text=str(e))

# Window
window = tkinter.Tk()
window.config(padx=25, pady=25)

canvas = tkinter.Canvas(height=100, width=300)
canvas.grid(column=0, row=0, columnspan=4)
canvas.create_text(150, 20, text="Your BMI:", font=("Arial", 24, "bold"))
bmi_display = canvas.create_text(150, 70, text="00.0", font=("Arial", 24, "bold"))

# Labels
label_weight = tkinter.Label(text="Weight: ")
label_weight.grid(column=0, row=2)

label_height = tkinter.Label(text="Height: ")
label_height.grid(column=0, row=3)

# Entries
entry_weight = tkinter.Entry()
entry_weight.grid(column=1, row=2)

entry_height = tkinter.Entry()
entry_height.grid(column=1, row=3)

# Radios
weight_metric = tkinter.IntVar()
weight_metric.set(POUNDS)

radio_pounds = tkinter.Radiobutton(text="Pounds", value=POUNDS, variable=weight_metric)
radio_pounds.grid(column=2, row=2, sticky="EW")

radio_kilogram = tkinter.Radiobutton(text="Kilograms", value=KILOGRAMS, variable=weight_metric)
radio_kilogram.grid(column=3, row=2, sticky="EW")

height_metric = tkinter.IntVar()
height_metric.set(INCHES)

radio_inches = tkinter.Radiobutton(text="Inches", value=INCHES, variable=height_metric)
radio_inches.grid(column=2, row=3, sticky="EW")

radio_meters = tkinter.Radiobutton(text="Meters", value=METERS, variable=height_metric)
radio_meters.grid(column=3, row=3, sticky="EW", pady=5)

# Buttons
button_generate = tkinter.Button(text="Generate", command=convert_bmi)
button_generate.grid(column=0, row=4, columnspan=4, pady=5)

# Start main loop
window.mainloop()
