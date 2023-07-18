import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
import Chart
from tkinter import *
import datetime

df = None  # Establishing global dataframe variable

def upload_file():
    global df
    file_types = [('CSV files', '*.csv'), ('All Files', '*.*')]
    file_path = filedialog.askopenfilename(filetypes=file_types)

    if file_path:
        df = pd.read_csv(file_path, parse_dates=['Datetime (UTC)'],
                         date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%dT%H:%M:%SZ'))
        # display_dataframe()
        combo_datastream["values"] = list(df.columns)[3:]  # Populating datastream combobox
        combo_datastream.current(0)  # Setting default datastream combobox value
        btn_chart["state"] = "normal"  # Enabling create chart button
        btn_clear["state"] = "normal"  # Enabling clear participant button

def destroy_charts():
    for widget in chart_space.winfo_children():
        widget.destroy()

def clear_participant():
    destroy_charts()
    btn_chart["state"] = "disable"
    btn_clear["state"] = "disable"
    combo_datastream["values"] = ""
    combo_datastream.set('')

def create_chart():
    global df

    df['Datetime'] = df['Datetime (UTC)'].dt.tz_localize('UTC')

    if combo_time.get() == "UTC":
        chart = Chart.chart(combo_chart.get(), df['Datetime (UTC)'], df[combo_datastream.get()])
        chart.display(chart_space)

    elif combo_time.get() == "US Eastern":
        df['time'] = df['Datetime'].dt.tz_convert('US/Eastern')
        chart = Chart.chart(combo_chart.get(), df['time'], df[combo_datastream.get()])
        chart.display(chart_space)

    elif combo_time.get() == "US Mountain":
        df['time'] = df['Datetime'].dt.tz_convert('US/Mountain')
        chart = Chart.chart(combo_chart.get(), df['time'], df[combo_datastream.get()])
        chart.display(chart_space)

    elif combo_time.get() == "US Central":
        df['time'] = df['Datetime'].dt.tz_convert('US/Central')
        chart = Chart.chart(combo_chart.get(), df['time'], df[combo_datastream.get()])
        chart.display(chart_space)

    elif combo_time.get() == "US Alanskan":
        df['time'] = df['Datetime'].dt.tz_convert('US/Alaska')
        chart = Chart.chart(combo_chart.get(), df['time'], df[combo_datastream.get()])
        chart.display(chart_space)

    elif combo_time.get() == "US Pacific":
        df['time'] = df['Datetime'].dt.tz_convert('US/Pacific')
        chart = Chart.chart(combo_chart.get(), df['time'], df[combo_datastream.get()])
        chart.display(chart_space)

    elif combo_time.get() == "US Hawaiian":
        df['time'] = df['Datetime'].dt.tz_convert('US/Hawaii')
        chart = Chart.chart(combo_chart.get(), df['time'], df[combo_datastream.get()])
        chart.display(chart_space)

window = tk.Tk()
window.title("CSV File Reader")
window.geometry("1920x1080")

sidebar = tk.Frame(window)
sidebar.pack(side="left", fill="y")

chart_space = tk.Frame(window)
chart_space.pack(side="right", fill="y")

btn_browse = tk.Button(sidebar, text="Browse File", command=upload_file, height=2, width=20, bg='lightblue')
btn_browse.pack()

combo_datastream = ttk.Combobox(sidebar, values="", state="readonly")
combo_datastream.pack()

btn_delete = tk.Button(sidebar, text="Delete All Charts", command=destroy_charts, height=2, width=20, bg='lightcoral')
btn_delete.pack()

btn_clear = tk.Button(sidebar, text="Clear Participant", command=clear_participant, height=2, width=20, bg='silver', state="disabled")
btn_clear.pack()

btn_chart = tk.Button(sidebar, text="Create Chart", command=create_chart, height=2, width=20, bg='lightgreen', state="disabled")
btn_chart.pack()

style = ttk.Style()
style.configure("Treeview", borderwidth=100)

combo_chart = ttk.Combobox(sidebar, values=["Line", "Bar", "Scatter"])
combo_chart.current(0)  # Set default value to "Line"
combo_chart.pack(padx=10, pady=(0, 10))

label_time = Label(sidebar, text="Select Time")
label_time.pack()

combo_time = ttk.Combobox(sidebar, values=["UTC", "US Eastern", "US Central", "US Mountain", "US Pacific", "US Alanskan", "US Hawaiian"])
combo_time.current(0)
combo_time.pack()

window.mainloop()
