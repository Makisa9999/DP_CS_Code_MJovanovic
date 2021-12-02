
import tkinter as tk

def onclick():
    make = entry1.get()
    dictionary['car'] = make
    model = entry2.get()
    dictionary['model'] = model
    color = entry3.get()
    dictionary['color'] = color
    wheelcolor = entry4.get()
    dictionary['wheelcolor'] = wheelcolor
    print(dictionary)
    print(printYourCar())

def printYourCar():
    return "You want " + dictionary["car"] + " " + dictionary["model"] + " in " + dictionary['color'] + " with " + dictionary['wheelcolor'] + " wheels!"

dictionary = {'car' : "", 'model': "", 'color': "", 'wheelcolor': ""}
#This creates new window
window = tk.Tk()
window.title("Car Cofigurator")
#First Line on the window
greeting = tk.Label(text="This is my car configurator!",)
greeting.pack()
#Second Line on the window
label1 = tk.Label(text="Write down what car you want. (Example: Audi, BMW, Mercedes)")
#Entry field
entry1 = tk.Entry()
#
label2 = tk.Label(text="Write down what model do you want. (Example: RS4, S350d, M5)")
entry2 = tk.Entry()
#
label3 = tk.Label(text="Write down what color of the car you want. (Example: red, blue, orange)")
entry3 = tk.Entry()
#
label4 = tk.Label(text="Write down what color of the wheels you want. (Example: red, black, grey, white)")
entry4 = tk.Entry()
#
btn1 = tk.Button(window, text="Next", command=onclick)

label1.pack()
entry1.pack()

label2.pack()
entry2.pack()

label3.pack()
entry3.pack()

label4.pack()
entry4.pack()

btn1.pack()


window.mainloop()
