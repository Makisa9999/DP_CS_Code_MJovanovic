# Here I want to make an application for the Pascal's triangle.
# In this application I want it to ask for the integer which is the number "n" (x + y) ** n
# The output of the program is going to be printed out on the screen what are the numbers 
# of that degree.

def pascalsTriangle():
    degree = int(input())
    pascal = []
    for i in range(degree + 1):
        pascal.append([0] * (i + 1))
    for i in range(len(pascal)):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for j in range(len(pascal[i])):
            if pascal[i][j] == 0:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            else:
                pass
    return pascal[-1]

import tkinter as tk
window = tk.Tk()
window.title("Pascals Triangle")
window.geometry("400x300")
tk.mainloop()