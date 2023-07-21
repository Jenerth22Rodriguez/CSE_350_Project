import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
import datetime
import Chart
from tkinter import *
import datetime
import statistics

df = None  # Establishing global dataframe variable

def upload_file():
    global df
    file_types = [('CSV files', '*.csv'), ('All Files', '*.*')]
    file_path = filedialog.askopenfilename(filetypes=file_types)

    if file_path:
        df = pd.read_csv(file_path)
        df["Datetime (UTC)"] = pd.to_datetime(df["Datetime (UTC)"], format="%Y-%m-%dT%H:%M:%SZ")
        df['Datetime'] = df['Datetime (UTC)'].dt.tz_localize('UTC')
        df['time'] = df['Datetime']
        combo_datastream["values"] = list(df.columns)[3:]  # Populating datastream combobox
        combo_datastream.current(0)  # Setting default datastream combobox value
        combo_time["values"] = ["UTC", "US Eastern", "US Central", "US Mountain", "US Pacific", "US Alaskan", "US Hawaiian"]
        combo_time.current(0)
        update_start_and_end_time_comboboxes()
        btn_chart["state"] = "normal"  # Enabling create chart button
        btn_clear["state"] = "normal"  # Enabling clear participant button

def timezone_update(event):
    global df

    if combo_time.get() == "UTC":
        df['time'] = df['Datetime']

    elif combo_time.get() == "US Eastern":
        df['time'] = df['Datetime'].dt.tz_convert('US/Eastern')

    elif combo_time.get() == "US Mountain":
        df['time'] = df['Datetime'].dt.tz_convert('US/Mountain')

    elif combo_time.get() == "US Central":
        df['time'] = df['Datetime'].dt.tz_convert('US/Central')

    elif combo_time.get() == "US Alaska":
        df['time'] = df['Datetime'].dt.tz_convert('US/Alaska')

    elif combo_time.get() == "US Pacific":
        df['time'] = df['Datetime'].dt.tz_convert('US/Pacific')

    elif combo_time.get() == "US Hawaiian":
        df['time'] = df['Datetime'].dt.tz_convert('US/Hawaii')
    
    update_start_and_end_time_comboboxes()

def update_start_and_end_time_comboboxes():
    combo_start_time["values"] = list(df["time"])
    combo_start_time.current(0)
    combo_end_time["values"] = list(df["time"])
    combo_end_time.current(len(list(df["time"])) - 1)

def destroy_charts():
    for widget in chart_space.winfo_children():
        widget.destroy()

def clear_participant():
    destroy_charts()
    btn_chart["state"] = "disabled"
    btn_clear["state"] = "disabled"
    combo_datastream["values"] = ""
    combo_datastream.set('')
    combo_start_time["values"] = ""
    combo_start_time.set('')
    combo_end_time["values"] = ""
    combo_end_time.set('')
    combo_time["values"] = ""
    combo_time.set('')

def create_chart():
    global df
    timeframe = df["time"][combo_start_time.current():combo_end_time.current()]
    data = df[combo_datastream.get()][combo_start_time.current():combo_end_time.current()]
    chart = Chart.chart(combo_chart.get(), timeframe, data)
    chart.display(chart_space, sidebar)

def update_combo_end_time(event):
    combo_end_time["values"] = list(df["time"])[list(df["time"]).index(pd.to_datetime(combo_start_time.get(), format="ISO8601")):]

def update_combo_start_time(event):
    combo_start_time["values"] = list(df["time"])[:list(df["time"]).index(pd.to_datetime(combo_end_time.get(), format="ISO8601")) + 1]

window = tk.Tk()
window.title("CSV File Reader")
window.geometry("1920x1080")

sidebar = tk.Frame(window, background="light grey")
sidebar.pack(side="left", fill="y")

chart_space = tk.Frame(window)
chart_space.pack(side="right", fill="y")

btn_browse = tk.Button(sidebar, text="Browse File", command=upload_file, height=2, width=20, bg='lightblue')
btn_browse.pack(padx=10, pady=10)

label_start = Label(sidebar, text="Select Start Time", background="light grey")
label_start.pack()
combo_start_time = ttk.Combobox(sidebar)
combo_start_time.pack(padx=10, pady=(0, 10))
combo_start_time.bind("<<ComboboxSelected>>", update_combo_end_time)

label_end = Label(sidebar, text="Select End Time", background="light grey")
label_end.pack()
combo_end_time = ttk.Combobox(sidebar)
combo_end_time.pack(padx=10, pady=(0, 10))
combo_end_time.bind("<<ComboboxSelected>>", update_combo_start_time)

label_datastream = Label(sidebar, text="Select Datastream", background="light grey")
label_datastream.pack()
combo_datastream = ttk.Combobox(sidebar, values="", state="readonly")
combo_datastream.pack(padx=10)

btn_delete = tk.Button(sidebar, text="Delete All Charts", command=destroy_charts, height=2, width=20, bg='lightcoral')
btn_delete.pack(padx=10, pady=10)

btn_clear = tk.Button(sidebar, text="Clear Participant", command=clear_participant, height=2, width=20, bg='silver', state="disabled")
btn_clear.pack(padx=10, pady=10)

btn_chart = tk.Button(sidebar, text="Create Chart", command=create_chart, height=2, width=20, bg='lightgreen', state="disabled")
btn_chart.pack(padx=10, pady=10)

label_chart = Label(sidebar, text="Select Chart Type", background="light grey")
label_chart.pack()
combo_chart = ttk.Combobox(sidebar, values=["Line", "Bar", "Scatter"])
combo_chart.current(0)  # Set default value to "Line"
combo_chart.pack(padx=10, pady=(0, 10))

label_time = Label(sidebar, text="Select Timezone", background="light grey")
label_time.pack()
combo_time = ttk.Combobox(sidebar)
combo_time.pack(padx=10, pady=(0, 10))
combo_time.bind("<<ComboboxSelected>>", timezone_update)

stats = tk.Frame(sidebar, background="light grey")
stats.pack(fill="y")

style = ttk.Style()
style.configure("Treeview", borderwidth=100)

window.mainloop()