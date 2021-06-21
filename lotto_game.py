from tkinter import *
import random
from tkinter import messagebox
from playsound import playsound
playsound('3, 2, 1 Go!.mp3')
root = Tk()
root.title("Lotto Game")
root.geometry("500x800")
root.config(bg = "#f8db19")

my_pic = PhotoImage(file = "thelogo-removebg-preview.png")
background = Label(root, image = my_pic, bg = "#f8db19").place(x=100, y=10)

result = StringVar()

set1 = []
set2 = []
set3 = []
amount = [0, 0, 20, 100.50, 2384, 8584, 10000000]
mylist = []


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
                    playsound('Error 404.mp3')
                    messagebox.showinfo("Woah!!!","Sets Are Completed")
                else:
                    playsound('Fail sound.mp3')
                    messagebox.showerror("Sorry","Your Already Picked That number")

        self.frame = LabelFrame(root)
        self.frame.place(x=20, y=350, height = 120, width = 450)
        self.frame.config(bg = "#ffe015")
        self.lab = Label(master, text = "Select Your Numbers:", font = "Georgia 15")
        self.lab.place(x=135, y=330)
        self.lab.config(bg = "#ffe015")
        self.numlab1 = Label(master, text = "First Lotto Numbers Set:")
        self.numlab1.place(x=30, y=370)
        self.numlab1.config(bg = "#ffe015")
        self.numEn1 = Label(master, text = set1, width = "25")
        self.numEn1.place(x=230, y=370)
        self.numEn1.config(bg = "white")
        self.numlab2 = Label(master, text = "Second Lotto Number Set:")
        self.numlab2.place(x=30, y=400)
        self.numlab2.config(bg = "#ffe015")
        self.numEn2 = Label(master, text = set2, width = "25")
        self.numEn2.place(x=230, y=400)
        self.numEn2.config(bg = "white")
        self.numlab3 = Label(master, text = "Third Lotto Number Set:")
        self.numlab3.place(x=30, y=430)
        self.numlab3.config(bg = "#ffe015")
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
        self.lottobtn = Button(master, text = "Play", borderwidth = 3, command = self.gen_num)
        self.lottobtn.place(x= 50, y= 550)

        self.playagainbtn = Button(master, text = "Play Again", borderwidth = 3, command = self.playAgain)
        self.playagainbtn.place(x=120, y=550)
        self.playagainbtn.config(state = "disabled")
        self.covertbtn = Button(master, text = "Covert Currency", borderwidth = 3, command = self.covert)
        self.covertbtn.place(x=230, y=550)
        self.covertbtn.config(state = "disabled")
        self.claimbtn = Button(master, text = "Calm Prize", borderwidth = 3, command = self.claim)
        self.claimbtn.place(x=380, y=550)
        self.claimbtn.config(state = "disabled")

        self.result1 = Label(master)
        self.result1.place(x=20, y=600)
        self.result1.config(bg = "#f8db19")
        self.result2 = Label(master)
        self.result2.place(x=170, y=600)
        self.result2.config(bg = "#f8db19")
        self.result3 = Label(master)
        self.result3.place(x=320, y=600)
        self.result3.config(bg = "#f8db19")
        self.total = Label(master)
        self.total.place(x=20, y=700)
        self.total.config(bg = "#f8db19")


    # Lotto Generator Function
    def gen_num(self):
        global match, match2, match3
        amount = [0, 0, 20, 100.50, 2384, 8584, 10000000]
        mylist.clear()
        x = 0
        if len(set3) != 6:
            playsound('Error 404.mp3')
            messagebox.showerror("Error", "Complete All Sets")
            self.lottoEnt.config(state = "readonly")
        else:
             playsound('Drum Roll Please.mp3')
             while len(mylist) < 6:
                 lotto = random.randint(1, 49)
                 if lotto not in mylist:
                     mylist.append(lotto)
                 x = x + 1
             else:
                 x = x - 1
                 mylist.sort()
                 result.set(mylist)

                 self.lottoEnt.config(state = "normal")
                 self.lottobtn.config(state = "disabled")
                 self.playagainbtn.config(state = "normal")
                 self.covertbtn.config(state = "normal")
                 self.claimbtn.config(state = "normal")

        if len(set1) == 6 and len(set2) == 6 and len(set3) == 6:
            # gets the value visible in the sets and the generated numbers
            match = set(set1).intersection(set(mylist))
            match2 = set(set2).intersection(set(mylist))
            match3 = set(set3).intersection(set(mylist))
            claim_prize = amount

            if len(match) == 0:
                self.result1.config(text = "First Set: "
                                           "\nMatches: 0"
                                           "\nSo You`ve Won: R" + str(claim_prize[0]))
            elif len(match) == 1:
                self.result1.config(text = "First Set:"
                                           "\nMatches: " + str(len(match)) +" "+str(match) +
                                           "\nSo You`ve won: R" + str(claim_prize[1]))
            elif len(match) == 2:
                self.result1.config(text = "First Set:"
                                           "\nMatches: " + str(len(match)) +" "+str(match) +
                                           "\nSo You`ve won: R" + str(claim_prize[2]))
            elif len(match) == 3:
                self.result1.config(text = "First Set:"
                                           "\nMatches: " + str(len(match)) +" "+str(match) +
                                           "\nSo You`ve won: R" + str(claim_prize[3]))

            elif len(match) == 4:
                self.result1.config(text = "First Set:"
                                           "\nMatches: " + str(len(match)) +" "+str(match) +
                                           "\nSo You`ve won: R" + str(claim_prize[4]))

            elif len(match) == 5:
                self.result1.config(text = "First Set:"
                                           "\nMatches: " + str(len(match)) +" "+str(match) +
                                           "\nSo You`ve won: R" + str(claim_prize[5]))

            elif len(match) == 6:
                self.result1.config(text = "First Set:"
                                           "\nMatches: " + str(len(match)) +" "+str(match) +
                                           "\nSo You`ve won: R" + str(claim_prize[6]))

            if len(match2) == 0:
                self.result2.config(text = "Second Set: "
                                           "\nMatches: 0"
                                           "\nSo You`ve Won: R"+ str(claim_prize[0]))
            elif len(match2) == 1:
                self.result2.config(text = "Second Set: " 
                                           "\nMatches: " + str(len(match2)) +" "+str(match2) +
                                           "\nSo You`ve won: R" + str(claim_prize[1]))
            elif len(match2) == 2:
                self.result2.config(text = "Second Set: "
                                           "\nMatches: " + str(len(match2)) +" "+str(match2) +
                                           "\nSo You`ve won: R" + str(claim_prize[2]))
            elif len(match2) == 3:
                self.result2.config(text = "Second Set: "
                                           "\nMatches: " + str(len(match2)) +" "+str(match2) +
                                           "\nSo You`ve won: R" + str(claim_prize[3]))
            elif len(match2) == 4:
                self.result2.config(text = "Second Set: "
                                           "\nMatches: " + str(len(match2)) +" "+ str(match2) +
                                           "\nSo You`ve won: R" + str(claim_prize[4]))
            elif len(match2) == 5:
                self.result2.config(text = "Second Set: "
                                           "\nMatches: " + str(len(match2)) +" "+str(match2) +
                                           "\nSo You`ve won: R" + str(claim_prize[5]))
            else:
                self.result2.config(text = "Second Set: "
                                           "\nMatches: " + str(len(match2)) +" "+str(match2) +
                                           "\nSo You`ve won: R" + str(claim_prize[6]))

            if len(match3) == 0:
                self.result3.config(text = "Third Set:"
                                           "\nMatches: 0"
                                           "\nSo You`ve Won: R"+ str(claim_prize[0]))
            elif len(match3) == 1:
                self.result3.config(text = "Third Set: " 
                                           "\nMatches: " + str(len(match3)) +" "+str(match3) +
                                           "\nSo You`ve won: R" + str(claim_prize[1]))
            elif len(match3) == 2:
                self.result3.config(text = "Third Set: "
                                           "\nMatches: " + str(len(match3)) +" "+str(match3) +
                                           "\nSo You`ve won: R" + str(claim_prize[2]))
            elif len(match3) == 3:
                self.result3.config(text = "Third Set: "
                                           "\nMatches: " + str(len(match3)) +" "+str(match3) +
                                           "\nSo You`ve won: R" + str(claim_prize[3]))
            elif len(match3) == 4:
                self.result3.config(text = "Third Set: "
                                           "\nMatches: " + str(len(match3)) +" "+str(match3) +
                                           "\nSo You`ve won: R" + str(claim_prize[4]))
            elif len(match3) == 5:
                self.result3.config(text = "Third Set: "
                                           "\nMatches: " + str(len(match3)) +" "+str(match3) +
                                           "\nSo You`ve won: R" + str(claim_prize[5]))
            else:
                self.result3.config(text = "Third Set: "
                                           "\nMatches: " + str(len(match3)) +" "+str(match3) +
                                           "\nSo You`ve won: R" + str(claim_prize[6]))
        total = (int(amount[len(match)])+int(amount[len(match2)])+int(amount[len(match3)]))
        self.total.config(text = "Total: R"+ str(total))


        player = open('details_lotto_winnings.txt', 'a')
        player.write('\n')
        player.write("Lotto Results")
        player.write('\n')
        player.write("First Set: "+ str(set1))
        player.write('\n')
        player.write("Second Set: " + str(set2))
        player.write('\n')
        player.write("Third Set: " + str(set3))
        player.write('\n')
        player.write("Lotto Numbers: "+ self.lottoEnt.get())
        player.write('\n')
        player.write("Winnings: R " + str(total))
        player.write('\n')
        player.close()

        playsound('Applause Crowd Cheering.mp3')

    def playAgain(self):
        self.numEn1.config(text="")
        set1.clear()
        self.numEn2.config(text="")
        set2.clear()
        self.numEn3.config(text="")
        set3.clear()
        self.lottoEnt.delete(0, END)
        self.lottobtn.config(state="normal")
        self.result1.config(text="")
        self.result2.config(text="")
        self.result3.config(text="")
        self.total.config(text="")
        self.playagainbtn.config(state = "disabled")
        self.lottoEnt.config(state ="readonly")
        self.covertbtn.config(state = "disabled")
        self.claimbtn.config(state = "disabled")

    def covert(self):
        messagebox.showinfo("Going To Corvert","The Game Will Reset Once You Leave")
        root.destroy()
        import Currency_Coverter

    def claim(self):
        messagebox.showinfo("Claim", "To Claim Your Prize, We need Your Banking Details")
        root.destroy()
        import Bank


x = lotto(root)
root.mainloop()
