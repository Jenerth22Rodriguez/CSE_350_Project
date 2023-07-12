import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
import Chart

df = None #Establishing global dataframe variable

def upload_file():
    global df 
    file_types = [('CSV files', '*.csv'), ('All Files', '*.*')]
    file_path = filedialog.askopenfilename(filetypes=file_types)
    
    if file_path:
        df = pd.read_csv(file_path, parse_dates=['Datetime (UTC)'],
                              date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%dT%H:%M:%SZ'))  
        # display_dataframe()
        combo_datastream["values"] = list(df.columns)[3:] #Populating datastream combobox
        combo_datastream.current(0) #Setting default datastream combobox value
        btn_chart["state"]="normal" #Enabling create chart button
        btn_clear["state"]="normal" #Enabling clear participant button

# def display_dataframe():
#     global df
#     clear_treeview()
#     rows, columns = df.shape
#     lb2.config(text=f"Rows: {rows}, Columns: {columns}")
    
#     header_labels = list(df.columns)
#     trv["columns"] = tuple(header_labels)

#     for i, header in enumerate(header_labels):
#         trv.heading(header, text=header)
#         trv.column(header, width=50, anchor=tk.CENTER)
    
#     for index, row in df.iterrows():
#         trv.insert("", tk.END, text=index, values=list(row))

    # chart = Chart.chart("line", df)
    # chart.display(chart_space)

def destroy_charts():
    for widget in chart_space.winfo_children():
         widget.destroy()
        
def clear_participant():
    destroy_charts()
    btn_chart["state"]="disable"
    btn_clear["state"]="disable"
    combo_datastream["values"] = ""
    combo_datastream.set('')

def create_chart():
    global df
    # selected_items = trv.selection()
    # if len(selected_items) == 1:
    #     selected_item = selected_items[0]
    #     selected_row = trv.item(selected_item)["values"]
        
    #     if selected_row:
    #         datetime_utc = selected_row[0]
    #         timezone_minutes = selected_row[1]
    #         firmware_version = selected_row[2]
    #         app_version = selected_row[4]
    #         mobile_os_version = selected_row[6]
    #         gtcs_algorithm_version = selected_row[7]
            
    #         if datetime_utc and timezone_minutes and firmware_version and app_version and mobile_os_version and gtcs_algorithm_version:
                
    #             x = ["Timezone", "Firmware Version", "App Version", "Mobile OS Version", "GTCS Algorithm Version"]
    #             y = [str(timezone_minutes), firmware_version, app_version, mobile_os_version, gtcs_algorithm_version]
    
    #             fig = plt.figure(figsize=(10, 6), dpi=150)
    #             plt.bar(x, y, color='blue')
    
    #             plt.xlabel("Attributes")
    #             plt.ylabel("Values")
    #             plt.title("Device Information")
    #             plt.grid(True)
    
              
    #             canvas = FigureCanvasTkAgg(fig, master=chart_space)
    #             canvas.draw()
    #             canvas.get_tk_widget().pack()
    chart = Chart.chart(combo_chart.get(), df["Datetime (UTC)"], df[combo_datastream.get()])
    chart.display(chart_space)

window = tk.Tk()
window.title("CSV File Reader")
window.geometry("1920x1080")

sidebar = tk.Frame(window)
sidebar.pack(side="left",fill="y")

chart_space = tk.Frame(window)
chart_space.pack(side="right",fill="y")

# background_image = Image.open("coding.jpeg")
# background_photo = ImageTk.PhotoImage(background_image)
# background_label = tk.Label(sidebar)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


btn_browse = tk.Button(sidebar, text="Browse File", command=upload_file, height=2, width=20, bg='lightblue')
# btn_browse.place(x=175, y=300)
btn_browse.pack()

combo_datastream = ttk.Combobox(sidebar, values="", state="readonly")
combo_datastream.pack()

btn_delete = tk.Button(sidebar, text="Delete All Charts", command=destroy_charts, height=2, width=20, bg='lightcoral')
# btn_delete.place(x=375, y=300)
btn_delete.pack()


btn_clear = tk.Button(sidebar, text="Clear Participant", command=clear_participant, height=2, width=20, bg='silver', state="disabled")
# btn_clear.place(x=575, y=300)
btn_clear.pack()


btn_chart = tk.Button(sidebar, text="Create Chart", command=create_chart, height=2, width=20, bg='lightgreen', state="disabled")
# btn_chart.place(x=375, y=350)
btn_chart.pack()


# lb2 = tk.Label(chart_space, text="")
# lb2.pack()


style = ttk.Style()
style.configure("Treeview", borderwidth=100)  
# trv = ttk.Treeview(chart_space, style="Treeview", show="headings")
# trv.pack(padx=10, pady=(0, 10))


combo_chart = ttk.Combobox(sidebar, values=["Line", "Bar", "Scatter"])
combo_chart.current(0)  # Set default value to "Line"
combo_chart.pack(padx=10, pady=(0, 10))


window.mainloop()
