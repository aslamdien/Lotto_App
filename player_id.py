from tkinter import *
import rsaidnumber
from datetime import *
from tkinter import messagebox
import re

root = Tk()
root.title("Player ID")
root.geometry("500x500")
root.config(bg = "light green")


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class Player:

    def __init__(self, master):
        self.name_lab = Label(master, text = "Please Enter First Name:")
        self.name_lab.place(x=5, y=5)
        self.name_lab.config(bg = "light green")
        self.name_ent = Entry(master)
        self.name_ent.place(x=200, y=5)
        self.lastname_lab = Label(master, text = "Surname:")
        self.lastname_lab.place(x=105, y=50)
        self.lastname_lab.config(bg = "light green")
        self.lastname_ent = Entry(master)
        self.lastname_ent.place(x=200, y=50)
        self.email_lab = Label(master, text = "Email:")
        self.email_lab.place(x=125, y=100)
        self.email_lab.config(bg = "light green")
        self.email_ent = Entry(master, width = "23")
        self.email_ent.place(x=200, y=100)
        self.id_btn = Button(master, text = "ID Number", command = self.email_check)
        self.id_btn.place(x=75, y=195)
        self.id_btn.config(bg = "yellow")
        self.id_ent = Entry(master)
        self.id_ent.config(state = "readonly")
        self.id_ent.place(x=200, y=200)
        self.button1 = Button(master, text = "Verify", command = self.calculate_age ,borderwidth = "3")
        self.button1.place(x=100, y=300, width = 100)
        self.button1.config(bg="yellow")

    def email_check(self):
        if re.search(regex, self.email_ent.get()):
            self.id_ent.config(state="normal")
        else:
            messagebox.showerror("Email Error", "Please Enter Email Address")
            self.id_ent.config(state = "readonly")
            self.email_ent.delete(0, END)

    def calculate_age(self):
        try:
            id_number = rsaidnumber.parse(self.id_ent.get())
            age = str((datetime.today() - id_number.date_of_birth) // timedelta(365.25))

            if int(age) >= 18:
                messagebox.showinfo("Qualification", "Let`s Play")
            elif int(age) < 18:
                year = str(int(age) - 18)
                messagebox.showinfo("Qualification", "Your Are Too Young to Play. Please Try Again In" + year + " Year(s)")
                messagebox.showerror("ID Error", "ID Must Have 13 Digits Only")

        except ValueError:
            if str(self.id_ent.get()) != "":
                messagebox.showerror("ID ERROR!!!", "Please Enter Valid Integer")
                self.id_ent.delete(0, END)

            else:
                messagebox.showerror("ID ERROR!!", "Please Enter ID Number")
                self.id_ent.delete(0, END)


x = Player(root)
root.mainloop()
