from numpy import mean, median
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as Canvas
from matplotlib.figure import Figure
import statistics


class chart():
    def __init__(self, chartType: str, dataX, dataY, y):
        self.chartType = chartType
        self.dataX = dataX
        self.dataY = dataY
        self.y = y
        
    def delete_frame(self):
        self.chart_and_button.destroy()
        self.static.destroy()
    
    def delete_static(self):
        for widget in self.static.winfo_children():
            widget.destroy()
    
    def create_stats_anal(self):
        self.label = tk.Label(self.static, text=" Statistics of " + str(self.y))
        self.label.config(font=('', 8, 'bold'))
        self.label.pack()
        self.label_max = tk.Label(self.static, text=" ")
        self.label_min = tk.Label(self.static, text=" ")
        self.label_median = tk.Label(self.static, text=" ")
        self.label_mean = tk.Label(self.static, text=" ")

        self.label_max["text"] = 'Max: ' + str(max(self.dataY))
        self.label_min["text"] = 'Min: ' + str(min(self.dataY))
        self.label_median["text"] = 'Median: ' + str(median(self.dataY))
        self.label_mean["text"] = 'Mean: ' + str(mean(self.dataY))
        btn_del = tk.Button(self.static, text="Delete Statistics", command=self.delete_static, height=1, width=15, bg='lightblue', state="normal")

        self.label_max.pack()
        self.label_min.pack()
        self.label_median.pack()
        self.label_mean.pack()
        btn_del.pack()
        
    def display(self, parent, sidebar):
        self.static = tk.Frame(sidebar)
        self.static.pack(fill="y")

        self.chart_and_button = tk.Frame(parent)
        self.chart_and_button.pack(fill="y")
        self.fig = Figure(figsize=(22, 3), dpi=55, tight_layout=True)
        self.plot = self.fig.add_subplot(111)
        self.canvas = Canvas(self.fig, self.chart_and_button)
        self.canvas.get_tk_widget().pack(side="left")

        label_chart = tk.Label(self.chart_and_button, text=self.y)
        label_chart.pack()

        btn_stat = tk.Button(self.chart_and_button, text="Show Statistics", command=self.create_stats_anal, height=2, width=20, bg='lightblue')
        btn_stat.pack()

        btn_delete_chart = tk.Button(self.chart_and_button, text="Delete", command=self.delete_frame, height=2, width=20, bg='lightcoral')
        btn_delete_chart.pack(side="right")

        if self.chartType == "Line":
            self.plot.plot(self.dataX, self.dataY)
        elif self.chartType == "Bar":
            self.plot.bar(self.dataX, self.dataY)
        elif self.chartType == "Scatter":
            self.plot.scatter(self.dataX, self.dataY)
        
        self.canvas.draw()
