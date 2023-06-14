import csv
from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def read_csv_file():
    # Open file dialog to select a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Read the selected CSV file
    df = pd.read_csv(file_path)

    # Display the content in a messagebox
    tk.messagebox.showinfo("CSV Content", df.to_string())

main = Tk()
main.title("CS50")
main.geometry("500x550")

# label1 = Label(text="Enter Username:")
# label1.place(x=30, y=30)
# label1.config(bg='lightgreen', padx=0)

# username = Entry(text="")
# username.place(x=150, y=40, width=200, height=25)

# label2 = Label(text="Enter Password:")
# label2.place(x=30, y=80)
# label2.config(bg='lightgreen', padx=0)

# password = Entry(text="")
# password.place(x=150, y=80, width=200, height=25)

# button = Button(text="ADD", command=add_new_user)
# button.place(x=150, y=120, width=75, height=35)

read_csv_button = Button(main, text="Read CSV File", command=read_csv_file)
read_csv_button.pack(pady=10)

main.mainloop()
