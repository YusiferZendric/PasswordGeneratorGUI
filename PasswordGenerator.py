import random
import pyperclip

def Password(User_length, User_size):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = upper_case.lower()
    symbols = "^%$#@!*?"
    numbers = "1234567890"
    upper = True
    lower = True
    syms = True
    nums = True
    Chars = ""
    if upper:
        Chars+=upper_case
    if lower:
        Chars+=lower_case
    if syms:
        Chars+=symbols
    if nums:
        Chars+=numbers

    
    length = User_length
    
    size = User_size
  

    for i in range(length):
   
        password = random.sample(Chars, size)
        
        Real_password = "".join(password)
        
        return Real_password


from tkinter import *
splash_root = Tk()
splash_root.title("Password Generator")
splash_img = PhotoImage(file="splash_img.png")
splash_bg = Label(image=splash_img)
splash_bg.place(x=0, y=0, relheight=1, relwidth=1)
splash_root.geometry("580x470")

def main():
    splash_root.destroy()
    root = Tk()
    


    def password_generator():

        global a
        entry_label.delete(0, END)
        a = Password(1, 10)
        entry_label.insert(0, a)

    def copy_command():
        pyperclip.copy(a)




    root.geometry("580x470")
    root.config(bg="black")
    root.title("Password Generator")
    f1 = Frame(root, borderwidth=14,bg="red", relief=SUNKEN)
    f1.pack()

    label = Label(f1, text="Password Generator", bg='yellow', fg="red", font="Arial 39 bold", borderwidth=3)
    label.pack(pady=21)
    pass_val = StringVar()
    entry_label = Entry(f1, bg="yellow", fg="red", font="arial 35 bold", borderwidth=3, textvariable=pass_val)
    entry_label.pack(pady=20)
    generate_button = Button(f1,text="generate password", bg="yellow", fg="red", font="arial 30 bold", borderwidth=3, command=password_generator)
    generate_button.pack(pady=20)
    copy_button = Button(f1,text="copy", bg="yellow", fg="red", font="arial 30 bold", borderwidth=3, command=copy_command)
    copy_button.pack(pady=20)
    root.mainloop()












splash_root.after(3500, main)


mainloop()

    
        

        

