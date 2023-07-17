import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
import Chart
import pytz
from datetime import datetime

df = None  # Establishing global dataframe variable

def convert_to_local_time(utc_time, time_zone):
    utc = pytz.timezone('UTC')
    local = pytz.timezone(time_zone)
    utc_time = utc.localize(utc_time)
    local_time = utc_time.astimezone(local)
    return local_time

def convert_to_utc_time(local_time, time_zone):
    local = pytz.timezone(time_zone)
    utc = pytz.timezone('UTC')
    local_time = local.localize(local_time)
    utc_time = local_time.astimezone(utc)
    return utc_time

def upload_file():
    global df
    file_types = [('CSV files', '*.csv'), ('All Files', '*.*')]
    file_path = filedialog.askopenfilename(filetypes=file_types)

    if file_path:
        df = pd.read_csv(file_path, parse_dates=['Datetime (UTC)'],
                         date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%dT%H:%M:%SZ'))

        # Displaying the DataFrame in the console
        print(df)

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

    chart = Chart.chart(combo_chart.get(), df["Datetime (UTC)"], df[combo_datastream.get()])
    chart.display(chart_space)
    
def get_utc_time():
    utc_time = datetime.now(pytz.utc)
    utc_label.config(text="UTC Time: " + utc_time.strftime('%Y-%m-%d %H:%M:%S'))

def get_local_time():
    local_timezone = pytz.timezone('America/New_York')  # Replace 'Your_Time_Zone' with the desired time zone
    local_time = datetime.now(local_timezone)
    local_label.config(text="Local Time: " + local_time.strftime('%Y-%m-%d %H:%M:%S'))

window = tk.Tk()


window.title("CSV File Reader")
window.geometry("1280x1080")

sidebar = tk.Frame(window)
sidebar.pack(side="left", fill="y")

utc_button = tk.Button(window, text="Get UTC Time", command=get_utc_time)
utc_button.pack()

local_button = tk.Button(window, text="Get Local Time", command=get_local_time)
local_button.pack()

utc_label = tk.Label(window, text="UTC Time: ")
utc_label.pack()

local_label = tk.Label(window, text="Local Time: ")
local_label.pack()

chart_space = tk.Frame(window)
chart_space.pack(side="right", fill="y")

btn_browse = tk.Button(sidebar, text="Browse File", command=upload_file, height=2, width=20, bg='lightblue')
btn_browse.pack()

combo_datastream = ttk.Combobox(sidebar, values="", state="readonly")
combo_datastream.pack()

btn_delete = tk.Button(sidebar, text="Delete All Charts", command=destroy_charts, height=2, width=20, bg='lightcoral')
btn_delete.pack()

btn_clear = tk.Button(sidebar, text="Clear Participant", command=clear_participant, height=2, width=20, bg='silver',
                      state="disabled")
btn_clear.pack()

btn_chart = tk.Button(sidebar, text="Create Chart", command=create_chart, height=2, width=20, bg='lightgreen',
                      state="disabled")
btn_chart.pack()

style = ttk.Style()
style.configure("Treeview", borderwidth=100)

combo_chart = ttk.Combobox(sidebar, values=["Line", "Bar", "Scatter"])
combo_chart.current(0)  # Set default value to "Line"
combo_chart.pack(padx=10, pady=(0, 10))

window.mainloop()
