import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

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
        
def clear_treeview():
    trv.delete(*trv.get_children())

# Create the main Tkinter window
window = tk.Tk()
window.title("CSV File Reader")
window.geometry("500x350")

# Create and place the "Browse File" button
btn_browse = tk.Button(window, text="Browse File", command=upload_file)
btn_browse.pack(pady=10)

# Create and place the label for displaying the DataFrame dimensions
lb2 = tk.Label(window, text="")
lb2.pack()

# Create the Treeview widget
style = ttk.Style()
style.configure("Treeview", borderwidth=100)  # Remove the default border
trv = ttk.Treeview(window, style="Treeview", show="headings")
trv.pack(padx=10, pady=(0, 10))

# Run the Tkinter event loop
window.mainloop()
