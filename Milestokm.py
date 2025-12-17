#Basic needed UI imports
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

#title,   #im guessing there is more functions within ttk, and master is one of them
title_label = ttk.Label(master = window, text = "Miles to KM" )