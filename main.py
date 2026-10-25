import tkinter as tk

window = tk.Tk()
window.minsize(200,200)
window.title("BMI Calculator")


# kilo alanı
weight_label = tk.Label(window,text="Enter your Weight : ")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window,text="Enter your Height : ")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()


def calculate():

    if weight_entry.get() == "" or height_entry.get() == "":
        result_label.config(text="Please enter your weight and height.")
        return


    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100

        if height <= 0 or weight <= 0:
            result_label.config(text="Please enter positive values.")
            return

        bmi = weight / (height**2)

        if bmi < 18.5:
            category = "Skinny"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Fat"
        else:
            category = "Obese"
        result_label.config(text=f"BMI Result: {bmi:.2f} - {category}")

    except ValueError:
        result_label.config(text="Enter numbers!!")

calculate_button = tk.Button(window,text="Calculate",command=calculate)
calculate_button.pack()


result_label = tk.Label(window,text="Result: ")
result_label.pack()


window.mainloop()


