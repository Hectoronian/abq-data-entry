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

time_values = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = tk.StringVar()
ttk.Label(rec_info, text = 'Time').grid(row = 0, column = 1)
ttk.Combobox(
    rec_info,
    textvariable = variables['Time'],
    values = time_values).grid(row = 1, column = 1, sticky = (tk.W + tk.E))

# Second row lab input

variables['Lab'] = tk.StringVar()
ttk.Label(rec_info, text='Lab').grid(row = 2, column = 0)
labframe = ttk.Frame(rec_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
        labframe, value = lab, text = lab, variable = variables['Lab']
        ).pack(side = tk.LEFT, expand = True)
labframe.grid(row = 3, column = 0, sticky = (tk.W + tk.E))

# Plot and seed samples

variables['Plot'] = tk.IntVar()
ttk.Label(rec_info, text = 'Plot').grid(row = 2, column = 1)
ttk.Combobox(
    rec_info,
    textvariable = variables['Plot'],
    values = list(range(1, 21))
    ).grid(row = 3, column = 1, sticky = (tk.W + tk.E))

variables['Seed Sample'] = tk.StringVar()
ttk.Label(rec_info, text = 'Seed Sample').grid(row = 2, column = 2)
ttk.Entry(
    rec_info,
    textvariable = variables['Seed Sample']
    ).grid(row = 3, column = 2, sticky = (tk.W + tk.E))

# Environment Data Section

env_info = ttk.LabelFrame(drf, text = "Environment Data")
env_info.grid(sticky = (tk.W + tk.E))
for i in range(3):
    env_info.columnconfigure(i, weight = 1)

variables['Humidity'] = tk.DoubleVar()
ttk.Label(env_info, text = "Humidity (g/m3)").grid(row = 0, column = 0)
ttk.Spinbox(
    env_info, textvariable = variables['Humidity'],
    from_ = 0.5, to = 52.0, increment = 0.01
    ).grid(row = 1, column = 0, sticky = (tk.W + tk.E))
