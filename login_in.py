from tkinter import *
import rsaidnumber
from datetime import *
from tkinter import messagebox
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from systemd import login

import login_in

root = Tk()
root.title("Login Screen")
root.geometry("500x350")
root.config(bg = "#f8db19")

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

my_pic = PhotoImage(file = "resize-16240941251614889765southafricalottologoremovebgpreview2.png")
background = Label(root, image = my_pic, bg = "#f8db19").place(x=130, y=5)

class login0:
    def  __init__(self,master):
        self.frame = LabelFrame(root)
        self.frame.place(x=80, y=100, height = 200, width = 350)
        self.frame.config(bg = "#ffe015")
        self.namelab = Label(master, text = "Username:", font = "Georgia 15")
        self.namelab.place(x=100, y=120)
        self.namelab.config(bg = "#f8db19")
        self.nameEnt = Entry(master)
        self.nameEnt.place(x=250, y=126)
        self.playIdLab = Label(master, text = "Player ID:",font = "Georgia 15")
        self.playIdLab.place(x=111, y=170)
        self.playIdLab.config(bg = "#f8db19")
        self.playIdEnt = Entry(master)
        self.playIdEnt.place(x=250, y=176)
        self.loginbtn = Button(master, text = "Log In", borderwidth = "2", command = self.login)
        self.loginbtn.place(x=120, y = 250)
        self.loginbtn.config(bg = "yellow")
        self.registerbtn = Button(master, text = "Sign Up", borderwidth = "2", command = self.signUp)
        self.registerbtn.place(x= 250, y=250)
        self.registerbtn.config(bg = "yellow")

    def login(self):
             root.destroy()
             import lotto_game

    def signUp(self):
        root.destroy()
        self.player_id()


    def player_id(self):
        log = Tk()
        log.title("Player ID")
        log.geometry("500x500")
        log.config(bg = "light green")

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
                self.button1 = Button(master, text = "Verify", command = self.valid_age ,borderwidth = "3")
                self.button1.place(x=100, y=300, width = 100)
                self.button1.config(bg="yellow")

           def email_check(self):
                if re.search(regex, self.email_ent.get()):
                    self.id_ent.config(state="normal")
                else:
                    messagebox.showerror("Email Error", "Please Enter Email Address")
                    self.id_ent.config(state = "readonly")
                    self.email_ent.delete(0, END)

           def valid_age(self):
                player_Id = self.name_ent.get().strip() + self.id_ent.get()[2:4]
                player = open('details.txt', 'a')
                player.write("Player Name: " + self.name_ent.get() + " " + self.lastname_ent.get())
                player.write('\n')
                player.write("Email: " + self.email_ent.get())
                player.write('\n')
                player.write("Id Number: " + self.id_ent.get())
                player.write('\n')
                player.write("Player ID: " + player_Id)
                player.write('\n')
                senders_email = 'aslamdien90@gmail.com'
                receivers_email = self.email_ent.get()
                password = 'nitrocharge'
                subject = "Player ID"
                try:
                    for i in range(len(self.email_ent.get())):
                        if re.search(regex,self.email_ent.get()):
                            msg = MIMEMultipart()
                            msg["From"] = senders_email
                            msg["To"] = receivers_email
                            msg["Subject"] = subject

                            body = "Hi There " + str(self.name_ent.get())+"\n"
                            body = body + "This Is Your Player ID: " + str(player_Id)
                            msg.attach(MIMEText(body, 'plain'))
                            text = msg.as_string()
                            s = smtplib.SMTP("smtp.gmail.com", 587)

                            s.starttls()

                            s.login(senders_email, password)
                            s.sendmail(senders_email, receivers_email, text)
                            s.quit()
                            break
                    id_number = rsaidnumber.parse(self.id_ent.get())
                    age = str((datetime.today() - id_number.date_of_birth) // timedelta(365.25))

                    if int(age) >= 18:
                        messagebox.showinfo("OK", "You Should Be Receiving An Email With Player ID Soon")
                        player.close()
                        log.destroy()
                        var = login_in.root

                    elif int(age) < 18:
                        year = str(int(age) - 18)
                        messagebox.showinfo("Sorry", "Your Are Too Young to Play. Please Try Again In " + year + " Year(s)")

                except ValueError:
                    if str(self.id_ent.get()) != "":
                        messagebox.showerror("ID ERROR!!!", "Please Enter Valid Integer")
                        self.id_ent.delete(0, END)

                    elif len(self.id_ent.get()) < 13:
                        messagebox.showerror("Error", "ID Numbers Only Have 13 Digits")
                        self.id_ent.delete(0,END)

                    else:
                        messagebox.showerror("ID ERROR!!", "Please Enter ID Number")
                        self.id_ent.delete(0, END)
        login = Player(log)
        log.mainloop()




x = login0(root)
root.mainloop()
