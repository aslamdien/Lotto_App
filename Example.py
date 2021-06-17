# main program
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Weather")
root.geometry("800x1000")
root.configure(bg="black")

entry1 = []
entry2 = []
entry3 = []
randomlist = []
winnings1= []
winnings2 = []
winnings3 = []
earnings = [0, 0, 20, 100.50, 2384, 8584, 10000000]



class main:
    def __init__(self,master):
        def adding(add):
            if len(entry1) < 6 and add not in entry1:
                entry1.append(add)
                self.ent1.config(text=entry1)

            elif len(entry1) == 6 and len(entry2) < 6 and add not in entry2:
                entry2.append(add)
                self.ent2.config(text=entry2)
            elif len(entry2) == 6 and len(entry3) < 6 and add not in entry3:
                entry3.append(add)
                self.ent3.config(text=entry3)

            else:
                if len(entry3) == 6:
                    messagebox.showerror("Error","Tries are full")
                else:
                    messagebox.showerror("Error","you can only select the same number once per entry")

        # frames within master
        self.frame = Frame(master, width=700, height=300, bg="", highlightbackground="gold", highlightthickness=15)
        self.frame.place(x=50, y=120)
        self.frame_two = Frame(master, width=330, height=250, bg="", highlightbackground="gold", highlightthickness=15)
        self.frame_two.place(x=50, y=445)
        self.frame_three = Frame(master, width=330, height=250, bg="", highlightbackground="gold",highlightthickness=15)
        self.frame_three.place(x=420, y=445)
        self.frame_four = Frame(master, width=700, height=230, bg="", highlightbackground="gold", highlightthickness=15)
        self.frame_four.place(x=50, y=720)

        # labels for frame 2
        self.ent1 = Label(self.frame_two, text="", textvariable=entry1, fg="gold",bg="black")
        self.ent1.place(x=50,y=30)
        self.ent2 = Label(self.frame_two,text="",fg="gold",bg="black", textvariable=entry2)
        self.ent2.place(x=50,y=100)
        self.ent3=Label(self.frame_two,text="",fg="gold",bg="black", textvariable=entry3)
        self.ent3.place(x=50,y=170)

        # labels for frame 3
        self.mainwin=Label(self.frame_three,text=randomlist.sort(),bg="gold")
        self.mainwin.place(x=100,y=30)
        self.ent1_win=Label(self.frame_three,text="",bg="gold")
        self.ent1_win.place(x=100,y=60)
        self.ent2_win = Label(self.frame_three, text="", bg="gold")
        self.ent2_win.place(x=100, y=120)
        self.ent3_win = Label(self.frame_three, text="", bg="gold")
        self.ent3_win.place(x=100, y=180)

        self.total=Label(self.frame_four,text="",bg="gold")
        self.total.place(x=100,y=100)
        #buttons

        self.one = Button(master, text="1", bg="gold", width=1, command=lambda: adding(1))
        self.one.place(x=100, y=200)
        self.two = Button(master, text="2", bg="gold", width=1, command=lambda: adding(2))
        self.two.place(x=140, y=200)
        self.three = Button(master, text="3", bg="gold", width=1, command=lambda: adding(3))
        self.three.place(x=180, y=200)
        self.four = Button(master, text="4", bg="gold", width=1, command=lambda: adding(4))
        self.four.place(x=220, y=200)
        self.five = Button(master, text="5", bg="gold", width=1, command=lambda: adding(5))
        self.five.place(x=260, y=200)
        self.six = Button(master, text="6", bg="gold", width=1, command=lambda: adding(6))
        self.six.place(x=300, y=200)
        self.seven = Button(master, text="7", bg="gold", width=1, command=lambda: adding(7))
        self.seven.place(x=340, y=200)
        self.eight = Button(master, text="8", bg="gold", width=1, command=lambda: adding(8))
        self.eight.place(x=380, y=200)
        self.nine = Button(master, text="9", bg="gold", width=1, command=lambda: adding(9))
        self.nine.place(x=420, y=200)
        self.ten = Button(master, text="10", bg="gold", width=1, command=lambda: adding(10))
        self.ten.place(x=460, y=200)
        self.eleven = Button(master, text="11", bg="gold", width=1, command=lambda: adding(11))
        self.eleven.place(x=500, y=200)
        self.twelve = Button(master, text="12", bg="gold", width=1, command=lambda: adding(12))
        self.twelve.place(x=540, y=200)
        self.thirteen = Button(master, text="13", bg="gold", width=1, command=lambda: adding(13))
        self.thirteen.place(x=580, y=200)
        self.fourteen = Button(master, text="14", bg="gold", width=1, command=lambda: adding(14))
        self.fourteen.place(x=620, y=200)
        self.fifteen= Button(master, text="15", bg="gold", width=1, command=lambda: adding(15))
        self.fifteen.place(x=660, y=200)
        self.sixteen = Button(master, text="16", bg="gold", width=1, command=lambda: adding(16))
        self.sixteen.place(x=140, y=230)
        self.seventeen = Button(master, text="17", bg="gold", width=1, command=lambda: adding(17))
        self.seventeen.place(x=180, y=230)
        self.eighteen = Button(master, text="18", bg="gold", width=1, command=lambda: adding(18))
        self.eighteen.place(x=220, y=230)
        self.nineteen = Button(master, text="19", bg="gold", width=1, command=lambda: adding(19))
        self.nineteen.place(x=260, y=230)
        self.twenty= Button(master, text="20", bg="gold", width=1, command=lambda: adding(20))
        self.twenty.place(x=300, y=230)
        self.twenty_one = Button(master, text="21", bg="gold", width=1, command=lambda: adding(21))
        self.twenty_one.place(x=340, y=230)
        self.twenty_two= Button(master, text="22", bg="gold", width=1, command=lambda: adding(22))
        self.twenty_two.place(x=380, y=230)
        self.twenty_three = Button(master, text="23", bg="gold", width=1, command=lambda: adding(23))
        self.twenty_three.place(x=420, y=230)
        self.twenty_four= Button(master, text="24", bg="gold", width=1, command=lambda: adding(24))
        self.twenty_four.place(x=460, y=230)
        self.twenty_five= Button(master, text="25", bg="gold", width=1, command=lambda: adding(25))
        self.twenty_five.place(x=500, y=230)
        self.twenty_six= Button(master, text="26", bg="gold", width=1, command=lambda: adding(26))
        self.twenty_six.place(x=540, y=230)
        self.twenty_seven = Button(master, text="27", bg="gold", width=1, command=lambda: adding(27))
        self.twenty_seven.place(x=580, y=230)
        self.twenty_eight= Button(master, text="28", bg="gold", width=1, command=lambda: adding(28))
        self.twenty_eight.place(x=620, y=230)
        self.twenty_nine = Button(master, text="29", bg="gold", width=1, command=lambda: adding(29))
        self.twenty_nine.place(x=180, y=260)
        self.thirty = Button(master, text="30", bg="gold", width=1, command=lambda: adding(30))
        self.thirty.place(x=220, y=260)
        self.thirty_one = Button(master, text="31", bg="gold", width=1, command=lambda: adding(31))
        self.thirty_one.place(x=260, y=260)
        self.thirty_two= Button(master, text="32", bg="gold", width=1, command=lambda: adding(32))
        self.thirty_two.place(x=300, y=260)
        self.thirty_three= Button(master, text="33", bg="gold", width=1, command=lambda: adding(33))
        self.thirty_three.place(x=340, y=260)
        self.thirty_four = Button(master, text="34", bg="gold", width=1, command=lambda: adding(34))
        self.thirty_four.place(x=380, y=260)
        self.thirty_five= Button(master, text="35", bg="gold", width=1, command=lambda: adding(35))
        self.thirty_five.place(x=420, y=260)
        self.thirty_six= Button(master, text="36", bg="gold", width=1, command=lambda: adding(36))
        self.thirty_six.place(x=460, y=260)
        self.thirty_seven= Button(master, text="37", bg="gold", width=1, command=lambda: adding(37))
        self.thirty_seven.place(x=500, y=260)
        self.thirty_eight= Button(master, text="38", bg="gold", width=1, command=lambda: adding(38))
        self.thirty_eight.place(x=540, y=260)
        self.thirty_nine= Button(master, text="39", bg="gold", width=1, command=lambda: adding(39))
        self.thirty_nine.place(x=580, y=260)
        self.forty = Button(master, text="40", bg="gold", width=1, command=lambda: adding(40))
        self.forty.place(x=220, y=290)
        self.forty_one = Button(master, text="41", bg="gold", width=1, command=lambda: adding(41))
        self.forty_one.place(x=260, y=290)
        self.forty_two = Button(master, text="42", bg="gold", width=1, command=lambda: adding(42))
        self.forty_two.place(x=300, y=290)
        self.forty_three= Button(master, text="43", bg="gold", width=1, command=lambda: adding(43))
        self.forty_three.place(x=340, y=290)
        self.forty_four= Button(master, text="44", bg="gold", width=1, command=lambda: adding(44))
        self.forty_four.place(x=380, y=290)
        self.forty_five = Button(master, text="45", bg="gold", width=1, command=lambda: adding(45))
        self.forty_five.place(x=420, y=290)
        self.forty_six = Button(master, text="46", bg="gold", width=1, command=lambda: adding(46))
        self.forty_six.place(x=460, y=290)
        self.forty_seven = Button(master, text="47", bg="gold", width=1, command=lambda: adding(47))
        self.forty_seven.place(x=500, y=290)
        self.forty_eight= Button(master, text="48", bg="gold", width=1, command=lambda: adding(48))
        self.forty_eight.place(x=540, y=290)
        self.forty_nine = Button(master, text="49", bg="gold", width=31, command=lambda: adding(49))
        self.forty_nine.place(x=260, y=322)

        def play():

            while len(randomlist) < 6:
                n = random.randint(1, 49)
                if n not in randomlist:
                    randomlist.append(n)
                    randomlist.sort()
                    self.mainwin.config(text=randomlist)
            for x in randomlist:
                if x in entry1 :
                    winnings1.append(x)
                    self.ent1_win.config(text=str(len(winnings1)) + "  R" + str(earnings[len(winnings1)]))
            for x in randomlist:
                if x in entry2:
                    winnings2.append(x)
                    self.ent2_win.config(text=str(len(winnings2)) + "   R" + str(earnings[len(winnings2)]))
            for x in randomlist:
                if x in entry3:
                    winnings3.append(x)
                    self.ent3_win.config(text=str(len(winnings3)) + "   R" + str(earnings[len(winnings3)]))
            total ="  total winnings:  R" + str(earnings[len(winnings1)]+earnings[len(winnings2)]+earnings[len(winnings3)])
            self.total.config(text=total)

        def play_again():
            entry1.clear()
            entry2.clear()
            entry3.clear()
            randomlist.clear()
            winnings1.clear()
            winnings2.clear()
            winnings3.clear()
            self.ent1.config(text="")
            self.ent2.config(text="")
            self.ent3.config(text="")
            self.mainwin.config(text="")
            self.ent1_win.config(text="")
            self.ent2_win.config(text="")
            self.ent3_win.config(text="")

        self.play_ag = Button(self.frame_four, text="PLAY AGAIN", bg="gold", command=play_again)
        self.play_ag.place(x=50, y=50)

#       function button
        self.play=Button(self.frame_two,text="PLAY",bg="gold",command=play)
        self.play.place(x=200,y=170)




m = main(root)
root.mainloop()