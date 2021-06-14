from tkinter import *
import rsaidnumber
from datetime import *
from tkinter import messagebox

root = Tk()
root.title("Player ID")
root.geometry("500x500")
root.config(bg = "yellow")


class Player:

    def __init__(self, master):
        self.name_lab = Label(master, text = "Please Enter Your Name:")
        self.name_lab.place(x=5, y=5)
        self.name_ent = Entry(master)
        self.name_ent.place(x=200, y=5)
        self.email_lab = Label(master, text = "Email:")
        self.email_lab.place(x=125, y=50)
        self.email_ent = Entry(master)
        self.email_ent.place(x=200, y=50)
        self.address_lab = Label(master, text = "Address:")
        self.address_lab.place(x=110, y=100)
        self.address_ent = Entry(master)
        self.address_ent.place(x=200, y=100, width = 250, height = 75)
        self.id_lab = Label(master, text = "ID Number")
        self.id_lab.place(x=100, y=200)
        self.id_ent = Entry(master)
        self.id_ent.place(x=200, y=200)
        self.button = Button(master, text = "Verify", command = self.calulate_Age ,borderwidth = "3")
        self.button.place(x=100, y=300, width = 100)


    def calulate_Age(self):
            id_number = rsaidnumber.parse(self.id_ent.get())
            age = str((datetime.today() - id_number.date_of_birth) // timedelta(365.25))
            try:
                if int(age) >= 18:
                    messagebox.showinfo("Qualification", "Let`s Play")
                elif int(age) < 18:
                    messagebox.showinfo("Qualification", "Your Are Too Young to Play. Please Try Again In" + age + "years")

            except ValueError:
                messagebox.showerror("ERROR", "Please Enter Valid Integer")

x = Player(root)
root.mainloop()
