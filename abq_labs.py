# data_entry_app.py
"""The ABQ Data Entry application"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv

variables = dict()
records_saved = 0

root = tk.Tk()
root.title('ABQ Data Entry Application')
# Prevent menus to stay on the left if root window's expanded
root.columnconfigure(0, weight = 1)

ttk.Label(
    root, text ="ABQ Data Entry Application",
    font = ("TkDefaultFont", 16)
    ).grid()

# Main Data Entry Form (drf)

drf = ttk.Frame(root)
drf.grid(padx=10, sticky = (tk.E + tk.W))
drf.columnconfigure(0, weight = 1)

# Record information Section

rec_info = ttk.LabelFrame(drf, text = 'Record Information')
rec_info.grid(sticky = (tk.W + tk.E))
for i in range(3):
    rec_info.columnconfigure(i, weight = 1)

variables['Date'] = tk.StringVar()
ttk.Label(rec_info, text = 'Date').grid(row = 0, column = 0)
ttk.Entry(
    rec_info,
    textvariable = variables['Date']
    ).grid(row = 1, column = 0, sticky = (tk.W + tk.E))
