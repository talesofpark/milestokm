#Basic needed UI imports
import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    try:
        mile_input= float(entry_int.get())
        km_output = mile_input * 1.61
        output_string.set(km_output)
        print("clicked")
    except ValueError:
        output_string.set("Enter a number")

#window
window = tk.Tk()
window.title("Demo")
window.geometry("300x220")  # FIX: was 300x150, output was getting pushed off screen

#title,   #im guessing there is more functions within ttk, and master is one of them
title_label = ttk.Label(master = window, text = "Miles to KM", font = "Calibri 24 bold")
# master is equivalent to parent
title_label.pack(pady = 20) # space or gap of y axis


#input field
input_frame = ttk.Frame(master = window)
#entry.get(), now getting the input variabl e
entry_int = tk.IntVar()

entry = ttk.Entry(master = input_frame, textvariable = entry_int) #parents to input frame now
button = ttk.Button(master = input_frame, text = "convert", command = convert)
#now we have to pack the entry and button into the window
entry.pack(side = "left" , padx = 10) #x axis gap
button.pack(side = "left")
input_frame.pack(pady = 10)


#output widget
output_string = tk.StringVar(value = "Output")
output_label = ttk.Label(master = window,
                         text = "Output",
                         font = "Calibri 24 bold",
                         textvariable = output_string)

output_label.pack(pady = 10)


#running
window.mainloop()