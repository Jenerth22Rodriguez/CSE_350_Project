import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class WearableSensorDataExplorer:
    def __init__(self, root):
        self.root = root
        self.df = None
        self.time_box = None

        self.create_widgets()

    def create_widgets(self):
        load_button = tk.Button(self.root, text="Load Sensor Data", command=self.load_sensor_data)
        load_button.pack()

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

        self.time_box = tk.Entry(self.root)
        self.time_box.pack()

    def load_sensor_data(self):
        # Open file dialog to select a CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        if file_path:
            try:
                # Load the CSV file into a DataFrame
                self.df = pd.read_csv(file_path)

                # Perform data analysis and visualization
                self.analyze_and_visualize_data()

                messagebox.showinfo("Success", "Sensor data loaded successfully!")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load sensor data: {str(e)}")

    def analyze_and_visualize_data(self):
        self.ax.clear()
        time_input = self.time_box.get()
        filtered_data = self.df

        if time_input:
            filtered_data = self.df.loc[self.df["Name"] == time_input]

        statistics = filtered_data.describe()

        messagebox.showinfo("Data Statistics", statistics.to_string())

        x = filtered_data["Name"]
        y = filtered_data["Age"]
        z = filtered_data["Salary"]
        self.ax.plot(x, y, z)
        self.ax.set_xlabel("Name")
        self.ax.set_ylabel("Age")
        self.ax.set_ylabel("Salary")

        # Format the plot
        self.ax.set_title("Wearable Sensor Data")
        self.fig.autofmt_xdate()

        self.canvas.draw()

window = tk.Tk()
window.title("Wearable Sensor Data Explorer")

data_explorer = WearableSensorDataExplorer(window)

window.mainloop()
