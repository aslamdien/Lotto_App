from tkinter import *
from tkinter import messagebox

from playsound import playsound

global player_id

root = Tk()
root.title("Login Screen")
root.geometry("500x350")
root.config(bg = "#f8db19")

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

my_pic = PhotoImage(file = "resize-16240941251614889765southafricalottologoremovebgpreview2.png")
background = Label(root, image = my_pic, bg = "#f8db19").place(x=130, y=5)


class login:
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
        player = 0
        with open('details.txt','r') as files:
            for line in files:
                if "Player ID" and self.playIdEnt.get() in line:
                    player = str(line[11:-1])

        if player == self.playIdEnt.get():
            playsound('BellDing Sound Effect.mp3')
            messagebox.showinfo("Access Granted", "Let The Games Begin!!!")
            root.destroy()
            import lotto_game

        else:
            playsound("Intruder Alert.mp3")
            messagebox.showerror("Error", "Username and Player ID Do Not Match \nSign Up if You Are not Registered")
            self.nameEnt.delete(0, END)
            self.playIdEnt.delete(0, END)

    def signUp(self):
        root.destroy()
        import player_id


x = login(root)
root.mainloop()



