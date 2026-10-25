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
    weight = weight_entry.get()
    height = height_entry.get()

    print("Your weight is: ",weight)
    print("Your height is: ",height)


calculate_button = tk.Button(window,text="Calculate",command=calculate)
calculate_button.pack()


window.mainloop()


