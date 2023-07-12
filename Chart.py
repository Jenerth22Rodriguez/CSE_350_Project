import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as Canvas
from matplotlib.figure import Figure

class chart():
    def __init__(self, chartType: str, dataX, dataY):
        self.chartType = chartType
        self.dataX = dataX
        self.dataY = dataY

    def delete_frame(self):
        self.chart_and_button.destroy()
    
    def display(self, parent):
        self.chart_and_button = tk.Frame(parent)
        self.chart_and_button.pack(fill="y")
        self.fig = Figure(figsize=(12, 2), dpi=100, tight_layout=True)
        self.plot = self.fig.add_subplot(111)
        self.canvas = Canvas(self.fig, self.chart_and_button)
        self.canvas.get_tk_widget().pack(side="left")
        btn_delete_chart = tk.Button(self.chart_and_button, text="Delete", command=self.delete_frame, height=2, width=20, bg='lightcoral')
        btn_delete_chart.pack(side="right")
        if self.chartType == "Line":
            self.plot.plot(self.dataX, self.dataY)
        elif self.chartType == "Bar":
            self.plot.bar(self.dataX, self.dataY)
        elif self.chartType == "Scatter":
            self.plot.scatter(self.dataX, self.dataY)
        self.canvas.draw()
