from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Lotto Game")
root.geometry("500x700")
root.config(bg = "#f8db19")

my_pic = PhotoImage(file = "thelogo-removebg-preview.png")
background = Label(root, image = my_pic, bg = "#f8db19").place(x=100, y=10)

result = StringVar()

set1 = []
set2 = []
set3 = []
amount = [0, 0, 20, 100.50, 2384, 8584, 10000000]

prize1 = []
prize2 = []
prize3 = []

class lotto:
    def __init__(self, master):
        def adding(add):
            if len(set1) < 6 and add not in set1:
                set1.append(add)
                self.numEn1.config(text=set1)

            elif len(set1) == 6 and len(set2) < 6 and add not in set2:
                set2.append(add)
                self.numEn2.config(text=set2)
            elif len(set2) == 6 and len(set3) < 6 and add not in set3:
                set3.append(add)
                self.numEn3.config(text=set3)

            else:
                if len(set3) == 6:
                    messagebox.showinfo("Woah!!!","Sets Are Completed")
                else:
                    messagebox.showerror("Sorry","Your Already Picked That number")

        self.lab = Label(master, text = "Select Your Numbers:", font = "Georgia 15")
        self.lab.place(x=135, y=330)
        self.lab.config(bg = "#f8db19")
        self.numlab1 = Label(master, text = "First Lotto Numbers Set:")
        self.numlab1.place(x=30, y=370)
        self.numlab1.config(bg = "#f8db19")
        self.numEn1 = Label(master, text = set1, width = "25")
        self.numEn1.place(x=230, y=370)
        self.numEn1.config(bg = "white")
        self.numlab2 = Label(master, text = "Second Lotto Number Set:")
        self.numlab2.place(x=30, y=400)
        self.numlab2.config(bg = "#f8db19")
        self.numEn2 = Label(master, text = set2, width = "25")
        self.numEn2.place(x=230, y=400)
        self.numEn2.config(bg = "white")
        self.numlab3 = Label(master, text = "Third Lotto Number Set:")
        self.numlab3.place(x=30, y=430)
        self.numlab3.config(bg = "#f8db19")
        self.numEn3 = Label(master, text = set3, width = "25")
        self.numEn3.place(x=230, y=430)
        self.numEn3.config(bg = "white")
        self.btn1 = Button(master, text = "1", width = 1, command = lambda :adding(1))
        self.btn1.place(x=5, y=120)
        self.btn2 = Button(master, text = "2", width = 1, command = lambda :adding(2))
        self.btn2.place(x=50, y=120)
        self.btn3 = Button(master, text = "3", width = 1, command = lambda :adding(3))
        self.btn3.place(x=95, y=120)
        self.btn4 = Button(master, text = "4", width = 1, command = lambda :adding(4))
        self.btn4.place(x=140, y=120)
        self.btn5 = Button(master, text = "5", width = 1, command = lambda :adding(5))
        self.btn5.place(x=185, y=120)
        self.btn6 = Button(master, text = "6", width = 1, command = lambda :adding(6))
        self.btn6.place(x=230, y=120)
        self.btn7 = Button(master, text = "7", width = 1, command = lambda :adding(7))
        self.btn7.place(x=275, y=120)
        self.btn8 = Button(master, text = "8", width = 1, command = lambda :adding(8))
        self.btn8.place(x=320, y=120)
        self.btn9 = Button(master, text = "9", width = 1, command = lambda :adding(9))
        self.btn9.place(x=365, y=120)
        self.btn10 = Button(master, text = "10", width = 1, command = lambda :adding(10))
        self.btn10.place(x=410, y=120)
        self.btn11 = Button(master, text = "11", width = 1, command = lambda :adding(11))
        self.btn11.place(x=455, y=120)
        self.btn12 = Button(master, text = "12", width = 1, command = lambda :adding(12))
        self.btn12.place(x=5, y=160)
        self.btn13 = Button(master, text = "13", width = 1, command = lambda :adding(13))
        self.btn13.place(x=50, y=160)
        self.btn14 = Button(master, text = "14", width = 1, command = lambda :adding(14))
        self.btn14.place(x=50, y=160)
        self.btn15 = Button(master, text = "15", width = 1, command = lambda :adding(15))
        self.btn15.place(x=95, y=160)
        self.btn16 = Button(master, text = "16", width = 1, command = lambda : adding(16))
        self.btn16.place(x=140, y=160)
        self.btn17 = Button(master, text = "17", width = 1, command = lambda : adding(17))
        self.btn17.place(x=185, y=160)
        self.btn18 = Button(master, text = "18", width = 1, command = lambda : adding(18))
        self.btn18.place(x=230, y=160)
        self.btn19 = Button(master, text = "19", width = 1, command = lambda : adding(19))
        self.btn19.place(x=275, y=160)
        self.btn20 = Button(master, text = "20", width = 1, command = lambda : adding(20))
        self.btn20.place(x=320, y=160)
        self.btn21 = Button(master, text = "21", width = 1, command = lambda : adding(21))
        self.btn21.place(x=365, y=160)
        self.btn22 = Button(master, text = "22", width = 1, command = lambda : adding(22))
        self.btn22.place(x=410, y=160)
        self.btn23 = Button(master, text = "23", width = 1, command = lambda : adding(23))
        self.btn23.place(x=455, y=160)
        self.btn24 = Button(master, text = "24", width = 1, command = lambda : adding(24))
        self.btn24.place(x=5, y=200)
        self.btn25 = Button(master, text = "25", width = 1, command = lambda : adding(25))
        self.btn25.place(x=50, y=200)
        self.btn26 = Button(master, text = "26", width = 1, command = lambda : adding(26))
        self.btn26.place(x=95, y=200)
        self.btn27 = Button(master, text = "27", width = 1, command = lambda : adding(27))
        self.btn27.place(x=140, y=200)
        self.btn28 = Button(master, text = "28", width = 1, command = lambda : adding(28))
        self.btn28.place(x=185, y=200)
        self.btn29 = Button(master, text = "29", width = 1, command = lambda : adding(29))
        self.btn29.place(x=230, y=200)
        self.btn30 = Button(master, text = "30", width = 1, command = lambda : adding(30))
        self.btn30.place(x=275, y=200)
        self.btn31 = Button(master, text = "31", width = 1, command = lambda : adding(31))
        self.btn31.place(x=320, y=200)
        self.btn32 = Button(master, text = "32", width = 1, command = lambda : adding(32))
        self.btn32.place(x=365, y=200)
        self.btn33 = Button(master, text = "33", width = 1, command = lambda : adding(33))
        self.btn33.place(x=410, y=200)
        self.btn34 = Button(master, text = "34", width = 1, command = lambda : adding(34))
        self.btn34.place(x=455, y=200)
        self.btn35 = Button(master, text = "35", width = 1, command = lambda : adding(35))
        self.btn35.place(x=5, y=240)
        self.btn36 = Button(master, text = "36", width = 1, command = lambda : adding(36))
        self.btn36.place(x=50, y=240)
        self.btn37 = Button(master, text = "37", width = 1, command = lambda : adding(37))
        self.btn37.place(x=95, y=240)
        self.btn38 = Button(master, text = "38", width = 1, command = lambda : adding(38))
        self.btn38.place(x=140, y=240)
        self.btn39 = Button(master, text = "39", width = 1, command = lambda : adding(39))
        self.btn39.place(x=185, y=240)
        self.btn40 = Button(master, text = "40", width = 1, command = lambda : adding(40))
        self.btn40.place(x=230, y=240)
        self.btn41 = Button(master, text = "41", width = 1, command = lambda : adding(41))
        self.btn41.place(x=275, y=240)
        self.btn42 = Button(master, text = "42", width = 1, command = lambda : adding(42))
        self.btn42.place(x=320, y=240)
        self.btn43 = Button(master, text = "43", width = 1, command = lambda : adding(43))
        self.btn43.place(x=365, y=240)
        self.btn44 = Button(master, text = "44", width = 1, command = lambda : adding(44))
        self.btn44.place(x=410, y=240)
        self.btn45 = Button(master, text = "45", width = 1, command = lambda : adding(45))
        self.btn45.place(x=455, y=240)
        self.btn46 = Button(master, text = "46", width = 1, command = lambda : adding(46))
        self.btn46.place(x=5, y=280)
        self.btn47 = Button(master, text = "47", width = 1, command = lambda : adding(47))
        self.btn47.place(x=50, y=280)
        self.btn48 = Button(master, text = "48", width = 1, command = lambda : adding(48))
        self.btn48.place(x=95, y=280)
        self.btn49 = Button(master, text = "49", width = 1, command = lambda : adding(49))
        self.btn49.place(x=140, y=280)

        # Lotto Number Generator
        self.lottolab = Label(master, text = "Lotto Numbers:")
        self.lottolab.place(x=100, y=500)
        self.lottolab.config(bg = "#f8db19" )
        self.lottoEnt = Entry(master, textvariable = result)
        self.lottoEnt.place(x=230, y=500)
        self.lottoEnt.config(state = "readonly")
        self.lottobtn = Button(master, text = "Play", command = self.gen_num)
        self.lottobtn.place(x= 100, y= 550)

        self.result1 = Label(master)
        self.result1.place(x=20, y=600)
        self.result1.config(bg = "#f8db19")
        self.result2 = Label(master)
        self.result2.place(x=20, y=630)
        self.result2.config(bg = "#f8db19")
        self.result3 = Label(master)
        self.result3.place(x=20, y=660)
        self.result3.config(bg = "#f8db19")
        self.total = Label(master)
        self.total.place(x=300, y=660)
        self.total.config(bg = "#f8db19")

    # Lotto Generator Function
    def gen_num(self):
        global mylist
        if len(set3) != 6:
            messagebox.showerror("Error", "Complete All The Sets")
            self.lottoEnt.config(state = "readonly")
        else:
             x = 0
             mylist = []
             while x < 6:
                 numbers = random.randint(1, 49)
                 if numbers not in mylist:
                     mylist.append(numbers)
                     x = x + 1
             else:
                  x = x - 1
                  mylist.sort()
                  result.set(mylist)
             self.lottoEnt.config(state = "normal")
        for x in mylist:
            if x in set1:
                prize1.append(x)
                self.result1 .config(text=str(len(prize1)) + "  R" + str(amount[len(prize1)]))
        for x in mylist:
            if x in set2:
                prize2.append(x)
                self.result2 .config(text=str(len(prize2)) + "  R" + str(amount[len(prize2)]))
        for x in mylist:
            if x in set3:
                prize3.append(x)
                self.result3 .config(text=str(len(prize3)) + "  R" + str(amount[len(prize3)]))

x = lotto(root)
root.mainloop()
