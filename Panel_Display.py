from tkinter import *

def add_new_user():
    pass 

main = Tk()
main.title("CS50")
main.geometry("500x150")
#
label1 = Label(text = "Enter Username:")
label1.place(x = 30, y = 30)
label1.config(bg= 'lightgreen', padx = 0)
#
username = Entry(text = "")
username.place(x=150, y=40, width= 200, height = 25)
##
label2 = Label(text = "Enter Password:")
label2.place(x = 30, y = 80)
label2.config(bg= 'lightgreen', padx = 0)
##
password = Entry(text = "")
password.place(x=150, y=80, width= 200, height = 25)
#
button = Button(text = "ADD", command = add_new_user)
button.place( x = 150, y = 120, width = 75, height = 35)

main.mainloop()