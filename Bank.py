from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root = Tk()
root.title("Calming Your Cash")
root.geometry("500x500")

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

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

        self.email_lab = Label(master, text = "Email Address: ", font = "15")
        self.email_lab.place(x=107, y=200)
        self.email_ent = Entry(master)

        self.claimbtn = Button(master, text = "Claim", borderwidth = 3, font = "15")
        self.claimbtn.place(x=100, y=300)
        self.clear = Button(master, text = "Clear", borderwidth = 3, font = "15")
        self.clear.place(x=200, y=300)

    def claim(self):
        player = open('details.txt', 'a')
        player.write("Account Holder: " + self.accHolderEnt.get())
        player.write('\n')
        player.write("Account Number: " + self.accNumberEnt.get())
        player.write('\n')
        player.write("Bank: " + self.selctBank.get())
        player.write('\n')

        senders_email = 'aslamdien90@gmail.com'
        receivers_email = self.email_ent.get()
        password = 'nitrocharge'
        subject = "Your Winnings"

        msg = MIMEMultipart()
        msg["From"] = senders_email
        msg["To"] = receivers_email
        msg["Subject"] = subject
        body = "Account Holder: " + str(self.accHolderEnt.get())+"\n"
        body = body + "Account Number: " + str(self.accNumberEnt.get())+"\n"
        body = body + body + "Bank: " + str(self.selctBank.get())
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP("smtp.gmail.com", 587)

        s.starttls()

        s.login(senders_email, password)
        s.sendmail(senders_email, receivers_email, text)
        s.quit()



x = banking(root)
root.mainloop()
