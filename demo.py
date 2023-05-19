import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
data = {
    'Name': ['John', 'Emma', 'Tom', 'Lisa', 'Mike'],
    'Age': [25, 28, 31, 27, 35],
    'Salary': [50000, 60000, 70000, 55000, 80000]
}
df = pd.DataFrame(data)

# Create a file using pandas
df.to_csv('data.csv', index=False)

# Create a tkinter window
window = tk.Tk()
window.title("Data Visualization")

# Read the data from the CSV file
data = pd.read_csv('data.csv')

# Create a bar plot using matplotlib
plt.bar(data['Name'], data['Salary'])
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Employee Salaries')

# Display the plot using tkinter
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()
canvas.draw()
figure = plt.gcf()
figure.set_size_inches(6, 4)
figure_canvas_agg = FigureCanvasAgg(figure)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

# Run the tkinter event loop
window.mainloop()
