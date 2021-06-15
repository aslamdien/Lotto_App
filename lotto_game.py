from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Lotto Game")
root.geometry("500x600")
root.config(bg = "#f8db19")

my_pic = PhotoImage(file = "lotto.png")
background = Label(root, image = my_pic, bg = "#f8db19").place(x=100, y=10)
class lotto:
    def __init__(self, master):
        self.lab = Label(master, text = "Select Your Numbers:", font = "Georgia 15")
        self.lab.place(x=135, y=330)
        self.lab.config(bg = "gold")
        self.numlab1 = Button(master, text = "First Lotto Numbers Set:", command = self.first_set)
        self.numlab1.place(x=30, y=370)
        self.numlab1.config(bg = "gold")
        self.numEn1 = Entry(master)
        self.numEn1.place(x=230, y=370)
        self.numlab2 = Button(master, text = "Second Lotto Number Set:", command = self.second_set)
        self.numlab2.place(x=30, y=400)
        self.numlab2.config(bg = "gold")
        self.numEn2 = Entry(master)
        self.numEn2.place(x=230, y=400)
        self.numEn2.config(state = "readonly")
        self.numlab3 = Button(master, text = "Third Lotto Number Set:", command= self.thrid_set)
        self.numlab3.place(x=30, y=430)
        self.numlab3.config(bg = "gold")
        self.numEn3 = Entry(master)
        self.numEn3.place(x=230, y=430)
        self.numEn3.config(state = "readonly")
        self.btn1 = Button(master, text = "1", width = 1, command = self.one)
        self.btn1.place(x=5, y=120)
        self.btn2 = Button(master, text = "2", width = 1, command = self.two)
        self.btn2.place(x=50, y=120)
        self.btn3 = Button(master, text = "3", width = 1, command = self.three)
        self.btn3.place(x=95, y=120)
        self.btn4 = Button(master, text = "4", width = 1, command = self.four)
        self.btn4.place(x=140, y=120)
        self.btn5 = Button(master, text = "5", width = 1, command = self.five)
        self.btn5.place(x=185, y=120)
        self.btn6 = Button(master, text = "6", width = 1, command = self.six)
        self.btn6.place(x=230, y=120)
        self.btn7 = Button(master, text = "7", width = 1, command = self.seven)
        self.btn7.place(x=275, y=120)
        self.btn8 = Button(master, text = "8", width = 1, command = self.eight)
        self.btn8.place(x=320, y=120)
        self.btn9 = Button(master, text = "9", width = 1, command = self.nine)
        self.btn9.place(x=365, y=120)
        self.btn10 = Button(master, text = "10", width = 1, command = self.ten)
        self.btn10.place(x=410, y=120)
        self.btn11 = Button(master, text = "11", width = 1, command = self.eleven)
        self.btn11.place(x=455, y=120)
        self.btn12 = Button(master, text = "12", width = 1, command = self.twelve)
        self.btn12.place(x=5, y=160)
        self.btn13 = Button(master, text = "13", width = 1, command = self.thriteen)
        self.btn13.place(x=50, y=160)
        self.btn14 = Button(master, text = "14", width = 1, command = self.fourteen)
        self.btn14.place(x=50, y=160)
        self.btn15 = Button(master, text = "15", width = 1, command = self.fivteen)
        self.btn15.place(x=95, y=160)
        self.btn16 = Button(master, text = "16", width = 1, command = self.sixteen)
        self.btn16.place(x=140, y=160)
        self.btn17 = Button(master, text = "17", width = 1, command = self.seventeen)
        self.btn17.place(x=185, y=160)
        self.btn18 = Button(master, text = "18", width = 1, command = self.eightteen)
        self.btn18.place(x=230, y=160)
        self.btn19 = Button(master, text = "19", width = 1, command = self.nineteen)
        self.btn19.place(x=275, y=160)
        self.btn20 = Button(master, text = "20", width = 1, command = self.tweenty_0)
        self.btn20.place(x=320, y=160)
        self.btn21 = Button(master, text = "21", width = 1, command = self.tweenty_1)
        self.btn21.place(x=365, y=160)
        self.btn22 = Button(master, text = "22", width = 1, command = self.tweenty_2)
        self.btn22.place(x=410, y=160)
        self.btn23 = Button(master, text = "23", width = 1, command = self.tweenty_3)
        self.btn23.place(x=455, y=160)
        self.btn24 = Button(master, text = "24", width = 1, command = self.tweenty_4)
        self.btn24.place(x=5, y=200)
        self.btn25 = Button(master, text = "25", width = 1, command = self.tweenty_5)
        self.btn25.place(x=50, y=200)
        self.btn26 = Button(master, text = "26", width = 1, command = self.tweenty_6)
        self.btn26.place(x=95, y=200)
        self.btn27 = Button(master, text = "27", width = 1, command = self.tweenty_7)
        self.btn27.place(x=140, y=200)
        self.btn28 = Button(master, text = "28", width = 1, command = self.tweenty_8)
        self.btn28.place(x=185, y=200)
        self.btn29 = Button(master, text = "29", width = 1, command = self.tweenty_9)
        self.btn29.place(x=230, y=200)
        self.btn30 = Button(master, text = "30", width = 1, command = self.thrity_0)
        self.btn30.place(x=275, y=200)
        self.btn31 = Button(master, text = "31", width = 1, command = self.thrity_1)
        self.btn31.place(x=320, y=200)
        self.btn32 = Button(master, text = "32", width = 1, command = self.thrity_2)
        self.btn32.place(x=365, y=200)
        self.btn33 = Button(master, text = "33", width = 1, command = self.thrity_3)
        self.btn33.place(x=410, y=200)
        self.btn34 = Button(master, text = "34", width = 1, command = self.thrity_4)
        self.btn34.place(x=455, y=200)
        self.btn35 = Button(master, text = "35", width = 1, command = self.thrity_5)
        self.btn35.place(x=5, y=240)
        self.btn36 = Button(master, text = "36", width = 1, command = self.thrity_6)
        self.btn36.place(x=50, y=240)
        self.btn37 = Button(master, text = "37", width = 1, command = self.thrity_7)
        self.btn37.place(x=95, y=240)
        self.btn38 = Button(master, text = "38", width = 1, command = self.thrity_8)
        self.btn38.place(x=140, y=240)
        self.btn39 = Button(master, text = "39", width = 1, command = self.thrity_9)
        self.btn39.place(x=185, y=240)
        self.btn40 = Button(master, text = "40", width = 1, command = self.forty_0)
        self.btn40.place(x=230, y=240)
        self.btn41 = Button(master, text = "41", width = 1, command = self.forty_1)
        self.btn41.place(x=275, y=240)
        self.btn42 = Button(master, text = "42", width = 1, command = self.forty_2)
        self.btn42.place(x=320, y=240)
        self.btn43 = Button(master, text = "43", width = 1, command = self.forty_3)
        self.btn43.place(x=365, y=240)
        self.btn44 = Button(master, text = "44", width = 1, command = self.forty_4)
        self.btn44.place(x=410, y=240)
        self.btn45 = Button(master, text = "45", width = 1, command = self.forty_5)
        self.btn45.place(x=455, y=240)
        self.btn46 = Button(master, text = "46", width = 1, command = self.forty_6)
        self.btn46.place(x=5, y=280)
        self.btn47 = Button(master, text = "47", width = 1, command = self.forty_7)
        self.btn47.place(x=50, y=280)
        self.btn48 = Button(master, text = "48", width = 1, command= self.forty_8)
        self.btn48.place(x=95, y=280)
        self.btn49 = Button(master, text = "49", width = 1, command = self.forty_9)
        self.btn49.place(x=140, y=280)

        self.int = []
        self.compare = []

    def one(self):
        insert = self.int.append(1)
        self.numEn1.insert(END, "1 ") or self.numEn2.insert(END, "1 ") or self.numEn3.insert(END, "1 ")
        self.btn1.config(state = "disabled")

    def two(self):
        insert = self.int.append(2)
        self.numEn1.insert(END, "2 ") or self.numEn2.insert(END, "2 ") or self.numEn3.insert(END, "2 ")
        self.btn2.config(state = "disabled")

    def three(self):
        insert = self.int.append(3)
        self.numEn1.insert(END, "3 ") or self.numEn2.insert(END, "3 ") or self.numEn3.insert(END, "3 ")
        self.btn3.config(state = "disabled")

    def four(self):
        insert = self.int.append(4)
        self.numEn1.insert(END, "4 ") or self.numEn2.insert(END, "4 ") or self.numEn3.insert(END, "4 ")
        self.btn4.config(state = "disabled")

    def five(self):
        insert = self.int.append(5)
        self.numEn1.insert(END, "5 ") or self.numEn2.insert(END, "5 ") or self.numEn3.insert(END, "5 ")
        self.btn9.config(state = "disabled")

    def six(self):
        insert = self.int.append(6)
        self.numEn1.insert(END, "6 ") or self.numEn2.insert(END, "6 ") or self.numEn3.insert(END, "6 ")
        self.btn6.config(state = "disabled")

    def seven(self):
        insert = self.int.append(7)
        self.numEn1.insert(END, "7 ") or self.numEn2.insert(END, "7 ") or self.numEn3.insert(END, "7 ")
        self.btn7.config(state = "disabled")

    def eight(self):
        insert = self.int.append(8)
        self.numEn1.insert(END, "8 ") or self.numEn2.insert(END, "8 ") or self.numEn3.insert(END, "8 ")
        self.btn8.config(state = "disabled")

    def nine(self):
        insert = self.int.append(9)
        self.numEn1.insert(END, "9 ") or self.numEn2.insert(END, "9 ") or self.numEn3.insert(END, "9 ")
        self.btn9.config(state = "disabled")

    def ten(self):
        insert = self.int.append(10)
        self.numEn1.insert(END, "10 ") or self.numEn2.insert(END, "10 ") or self.numEn3.insert(END, "10 ")
        self.btn10.config(state = "disabled")

    def eleven(self):
        insert = self.int.append(11)
        self.numEn1.insert(END, "11 ") or self.numEn2.insert(END, "11 ") or self.numEn3.insert(END, "11 ")
        self.btn11.config(state = "disabled")

    def twelve(self):
        insert = self.int.append(12)
        self.numEn1.insert(END, "12 ") or self.numEn2.insert(END, "12 ") or self.numEn3.insert(END, "12 ")
        self.btn12.config(state = "disabled")

    def thriteen(self):
        insert = self.int.append(13)
        self.numEn1.insert(END, "13 ") or self.numEn2.insert(END, "13 ") or self.numEn3.insert(END, "13 ")
        self.btn13.config(state = "disabled")

    def fourteen(self):
        insert = self.int.append(14)
        self.numEn1.insert(END, "14 ") or self.numEn2.insert(END, "14 ") or self.numEn3.insert(END, "14 ")
        self.btn14.config(state = "disabled")

    def fivteen(self):
        insert = self.int.append(15)
        self.numEn1.insert(END, "15 ") or self.numEn2.insert(END, "15 ") or self.numEn3.insert(END, "15 ")
        self.btn15.config(state = "disabled")

    def sixteen(self):
        insert = self.int.append(16)
        self.numEn1.insert(END, "16 ") or self.numEn2.insert(END, "16 ") or self.numEn3.insert(END, "16 ")
        self.btn16.config(state = "disabled")

    def seventeen(self):
        insert = self.int.append(17)
        self.numEn1.insert(END, "17 ") or self.numEn2.insert(END, "17 ") or self.numEn3.insert(END, "17 ")
        self.btn17.config(state = "disabled")

    def eightteen(self):
        insert = self.int.append(18)
        self.numEn1.insert(END, "18 ") or self.numEn2.insert(END, "18 ") or self.numEn3.insert(END, "18 ")
        self.btn18.config(state = "disabled")

    def nineteen(self):
        insert = self.int.append(19)
        self.numEn1.insert(END, "19 ") or self.numEn2.insert(END, "19 ") or self.numEn3.insert(END, "19 ")
        self.btn19.config(state = "disabled")

    def tweenty_0(self):
        insert = self.int.append(20)
        self.numEn1.insert(END, "20 ") or self.numEn2.insert(END, "20 ") or self.numEn3.insert(END, "20 ")
        self.btn20.config(state = "disabled")

    def tweenty_1(self):
        insert = self.int.append(21)
        self.numEn1.insert(END, "21 ") or self.numEn2.insert(END, "21 ") or self.numEn3.insert(END, "21 ")
        self.btn21.config(state = "disabled")

    def tweenty_2(self):
        insert = self.int.append(22)
        self.numEn1.insert(END, "22 ") or self.numEn2.insert(END, "22 ") or self.numEn3.insert(END, "22 ")
        self.btn22.config(state = "disabled")

    def tweenty_3(self):
        insert = self.int.append(23)
        self.numEn1.insert(END, "23 ") or self.numEn2.insert(END, "23 ") or self.numEn3.insert(END, "23 ")
        self.btn23.config(state = "disabled")

    def tweenty_4(self):
        insert = self.int.append(24)
        self.numEn1.insert(END, "24 ") or self.numEn2.insert(END, "24 ") or self.numEn3.insert(END, "24 ")
        self.btn24.config(state = "disabled")

    def tweenty_5(self):
        insert = self.int.append(25)
        self.numEn1.insert(END, "25 ") or self.numEn2.insert(END, "25 ") or self.numEn3.insert(END, "25 ")
        self.btn25.config(state = "disabled")

    def tweenty_6(self):
        insert = self.int.append(26)
        self.numEn1.insert(END, "26 ") or self.numEn2.insert(END, "26 ") or self.numEn3.insert(END, "26 ")
        self.btn26.config(state = "disabled")

    def tweenty_7(self):
        insert = self.int.append(27)
        self.numEn1.insert(END, "27 ") or self.numEn2.insert(END, "27 ") or self.numEn3.insert(END, "27 ")
        self.btn27.config(state = "disabled")

    def tweenty_8(self):
        insert = self.int.append(28)
        self.numEn1.insert(END, "28 ") or self.numEn2.insert(END, "28 ") or self.numEn3.insert(END, "28 ")
        self.btn28.config(state = "disabled")

    def tweenty_9(self):
        insert = self.int.append(29)
        self.numEn1.insert(END, "29 ") or self.numEn2.insert(END, "29 ") or self.numEn3.insert(END, "29 ")
        self.btn29.config(state = "disabled")

    def thrity_0(self):
        insert = self.int.append(30)
        self.numEn1.insert(END, "30 ") or self.numEn2.insert(END, "30 ") or self.numEn3.insert(END, "30 ")
        self.btn30.config(state = "disabled")

    def thrity_1(self):
        insert = self.int.append(31)
        self.numEn1.insert(END, "31 ") or self.numEn2.insert(END, "31 ") or self.numEn3.insert(END, "31 ")
        self.btn31.config(state = "disabled")

    def thrity_2(self):
        insert = self.int.append(32)
        self.numEn1.insert(END, "32 ") or self.numEn2.insert(END, "32 ") or self.numEn3.insert(END, "32 ")
        self.btn32.config(state = "disabled")

    def thrity_3(self):
        insert = self.int.append(33)
        self.numEn1.insert(END, "33 ") or self.numEn2.insert(END, "33 ") or self.numEn3.insert(END, "33 ")
        self.btn33.config(state = "disabled")

    def thrity_4(self):
        insert = self.int.append(34)
        self.numEn1.insert(END, "34 ") or self.numEn2.insert(END, "34 ") or self.numEn3.insert(END, "3 4")
        self.btn34.config(state = "disabled")

    def thrity_5(self):
        insert = self.int.append(35)
        self.numEn1.insert(END, "35 ") or self.numEn2.insert(END, "35 ") or self.numEn3.insert(END, "35 ")
        self.btn35.config(state = "disabled")

    def thrity_6(self):
        insert = self.int.append(36)
        self.numEn1.insert(END, "36 ") or self.numEn2.insert(END, "36 ") or self.numEn3.insert(END, "36 ")
        self.btn36.config(state = "disabled")

    def thrity_7(self):
        insert = self.int.append(37)
        self.numEn1.insert(END, "37 ") or self.numEn2.insert(END, "37 ") or self.numEn3.insert(END, "37 ")
        self.btn37.config(state = "disabled")

    def thrity_8(self):
        insert = self.int.append(38)
        self.numEn1.insert(END, "38 ") or self.numEn2.insert(END, "38 ") or self.numEn3.insert(END, "38 ")
        self.btn38.config(state = "disabled")

    def thrity_9(self):
        insert = self.int.append(39)
        self.numEn1.insert(END, "39 ") or self.numEn2.insert(END, "39 ") or self.numEn3.insert(END, "39 ")
        self.btn39.config(state = "disabled")

    def forty_0(self):
        insert = self.int.append(40)
        self.numEn1.insert(END, "40 ") or self.numEn2.insert(END, "40 ") or self.numEn3.insert(END, "40 ")
        self.btn40.config(state = "disabled")

    def forty_1(self):
        insert = self.int.append(41)
        self.numEn1.insert(END, "41 ") or self.numEn2.insert(END, "41 ") or self.numEn3.insert(END, "41 ")
        self.btn41.config(state = "disabled")

    def forty_2(self):
        insert = self.int.append(42)
        self.numEn1.insert(END, "42 ") or self.numEn2.insert(END, "42 ") or self.numEn3.insert(END, "42 ")
        self.btn42.config(state = "disabled")

    def forty_3(self):
        insert = self.int.append(43)
        self.numEn1.insert(END, "43 ") or self.numEn2.insert(END, "43 ") or self.numEn3.insert(END, "43 ")
        self.btn43.config(state = "disabled")

    def forty_4(self):
        insert = self.int.append(44)
        self.numEn1.insert(END, "44 ") or self.numEn2.insert(END, "44 ") or self.numEn3.insert(END, "44 ")
        self.btn44.config(state = "disabled")

    def forty_5(self):
        insert = self.int.append(45)
        self.numEn1.insert(END, "45 ") or self.numEn2.insert(END, "45 ") or self.numEn3.insert(END, "45 ")
        self.btn45.config(state = "disabled")

    def forty_6(self):
        insert = self.int.append(46)
        self.numEn1.insert(END, "46 ") or self.numEn2.insert(END, "46 ") or self.numEn3.insert(END, "46 ")
        self.btn46.config(state = "disabled")

    def forty_7(self):
        insert = self.int.append(47)
        self.numEn1.insert(END, "47 ") or self.numEn2.insert(END, "47 ") or self.numEn3.insert(END, "47 ")
        self.btn47.config(state = "disabled")

    def forty_8(self):
        insert = self.int.append(48)
        self.numEn1.insert(END, "48 ") or self.numEn2.insert(END, "48 ") or self.numEn3.insert(END, "48 ")
        self.btn48.config(state = "disabled")

    def forty_9(self):
        insert = self.int.append(49)
        self.numEn1.insert(END, "49 ") or self.numEn2.insert(END, "49 ") or self.numEn3.insert(END, "49 ")
        self.btn49.config(state = "disabled")
    
    def first_set(self):
        self.numEn1.config(state = "normal")
        self.numEn2.config(state = "readonly")
        self.numEn3.config(state = "readonly")
        
    def second_set(self):
        self.numEn1.config(state = "readonly")
        self.numEn2.config(state = "normal")
        self.numEn3.config(state = "readonly")
    
    def thrid_set(self):
        self.numEn1.config(state = "readonly")
        self.numEn2.config(state = "readonly")
        self.numEn3.config(state = "normal")


x = lotto(root)
root.mainloop()
