import tkinter as tk

window = tk.Tk()
window.minsize(300,300)
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

window.mainloop()


