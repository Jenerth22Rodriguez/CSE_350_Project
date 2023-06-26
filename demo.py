from tkinter import messagebox
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from tkinter import filedialog
from PIL import ImageTk, Image

def upload_file():
    file_types = [('CSV files', '*.csv'), ('All Files', '*.*')]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    
    if file_path:
        df = pd.read_csv(file_path)  # Read the CSV file and create a DataFrame
        display_dataframe(df)  # Display the DataFrame in the Treeview

def display_dataframe(df):
    clear_treeview()
    rows, columns = df.shape
    lb2.config(text=f"Rows: {rows}, Columns: {columns}")
    
    header_labels = list(df.columns)
    trv["columns"] = header_labels
    
    for i, header in enumerate(header_labels):
        trv.heading(header, text=header)
        trv.column(header, width=50, anchor=tk.CENTER)
    
    for index, row in df.iterrows():
        trv.insert("", tk.END, text=index, values=list(row))
        
def delete_row():
    selected_items = trv.selection()
    if selected_items:
        for item in selected_items:
            trv.delete(item)

def clear_treeview():
    trv.delete(*trv.get_children())

def create_chart():
    selected_items = trv.selection()
    if len(selected_items) == 1:
        selected_item = selected_items[0]
        selected_row = trv.item(selected_item)["text"]
        selected_columns = trv.item(selected_item)["values"]
        if selected_row and selected_columns:
            chart_type = combo_chart.get()
            if chart_type == "Line":
                x = list(selected_columns)
                y = []

                for value in x:
                    try:
                        y_value = int(value)
                        y.append(y_value)
                    except ValueError:
                        pass

          
                if len(x) != len(y):
                    messagebox.showerror("Error", "Invalid data for line plot")
                    return

                plt.plot(x, y)
                plt.xlabel("Columns")
                plt.ylabel("Values")
                plt.title("Line Plot")
                plt.show()

# Create the main Tkinter window
window = tk.Tk()
window.title("CSV File Reader")
window.geometry("750x400")

# Load and set the background image
background_image = Image.open("coding.jpeg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create and place the "Browse File" button
btn_browse = tk.Button(window, text="Browse File", command=upload_file, height=2, width=20, bg='lightblue')
btn_browse.place(x=175, y=300)

# Create and place the "Delete" button
btn_delete = tk.Button(window, text="Delete", command=delete_row, height=2, width=20, bg='lightcoral')
btn_delete.place(x=375, y=300)

# Create and place the "Clear The Screen" button
btn_clear = tk.Button(window, text="Clear The Screen", command=clear_treeview, height=2, width=20, bg='silver')
btn_clear.place(x=575, y=300)

# Create and place the "Create Chart" button
btn_chart = tk.Button(window, text="Create Chart", command=create_chart, height=2, width=20, bg='lightgreen')
btn_chart.place(x=375, y=350)

# Create and place the label for displaying the DataFrame dimensions
lb2 = tk.Label(window, text="")
lb2.pack()

# Create the Treeview widget
style = ttk.Style()
style.configure("Treeview", borderwidth=100)  # Remove the default border
trv = ttk.Treeview(window, style="Treeview", show="headings")
trv.pack(padx=10, pady=(0, 10))

# Create and place the chart type dropdown menu
combo_chart = ttk.Combobox(window, values=["Line"])
combo_chart.current(0)  # Set default value to "Line"
combo_chart.pack(padx=10, pady=(0, 10))

# Run the Tkinter event loop
window.mainloop()
