from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calming Your Cash")
root.geometry("500x500")

class banking:
    def __init__(self,master):
        self.subhead = Label(master, text = "Banking Details" , font = "Georgia 15")
        self.subhead.place(x= 170, y=10)
        self.accHolderlab = Label(master, text = "Account Holder:", font = "15")
        self.accHolderlab.place(x=100 ,y=50)
        self.accHolderEnt = Entry(master)
        self.accHolderEnt.place(x=250, y=50)
        self.accNumberlab = Label(master, text = "Bank Account Number:", font = "15")
        self.accNumberlab.place(x=40, y=100)
        self.accNumberEnt = Entry(master)
        self.accNumberEnt.place(x=250, y=100)
        self.selctBanklab = Label(master, text = "Bank:", font = "15")
        self.selctBanklab.place(x=180, y=150)

        self.selctBank = ttk.Combobox(master)
        self.selctBank['values'] = ["ABSA", "Netbank", "FNB", "Capitec"]
        self.selctBank['state'] = 'normal'
        self.selctBank.set('Select Bank')
        self.selctBank.place(x=250, y=150)

        self.claimbtn = Button(master, text = "Claim", borderwidth = 3, font = "15")
        self.claimbtn.place(x=100, y=300)
        self.clear = Button(master, text = "Clear", borderwidth = 3, font = "15")
        self.clear.place(x=200, y=300)


x = banking(root)
root.mainloop()
