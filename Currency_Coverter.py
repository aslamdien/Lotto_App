from tkinter import *
from tkinter import ttk
import requests
from tkinter import messagebox

root = Tk()
root.title("Covert Your Winnings")
root.geometry("500x500")
root.config(bg = "blue")

result = StringVar()

responce = requests.get('https://v6.exchangerate-api.com/v6/6698980fefc5cd611ec51be2/latest/ZAR')
results = responce.json()

conversion_rates = results['conversion_rates']

currency = []
for i in conversion_rates.keys():
    currency.append(i)



class covert:
    def __init__(self, master):
        with open('details_lotto_winnings.txt') as files:
            for line in files:
                file = line.split()
            player = file
            files.close()
            game = player[2]

        self.amountlab = Label(master, text = "Please Enter Amount:")
        self.amountlab.place(x=5, y=50)
        self.amountEnt = Entry(master)
        self.amountEnt.place(x=200, y=50)
        self.amountEnt.insert(0, game)
        self.covertFrom = Label(master, text = "Covert Currency Of")
        self.covertFrom.place(x=5, y=80)
        self.currZAR = Label(master, text = "ZAR", width = "20", bg = "white")
        self.currZAR.place(x=200, y=80)


        self.currency_cb = ttk.Combobox(master)
        self.currency_cb['values'] = currency
        self.currency_cb['state'] = 'normal'
        self.currency_cb.set('Select')
        self.currency_cb.place(x=200, y=120)

        self.new_curr_amountlab = Label(master, text = "New Currency Amount is:")
        self.new_curr_amountlab.place(x=5, y=230)
        self.new_curr_amountEnt = Entry(master, text = '', textvariable = result)
        self.new_curr_amountEnt.place(x=200, y=230)

        self.convetbtn = Button(master, text = 'Covert', borderwidth = 3, command = self.covertSwitch)
        self.convetbtn.place(x=200, y=180)
        self.calm = Button(master, text = "Calm Prize", command= self.toClaim, borderwidth = 3)
        self.calm.place(x =200, y=260 )
        self.clear = Button(master, text = "Clear", command = self.clear, borderwidth = 3)
        self.clear.place(x=330, y=260)

    def currencyConvert(self, from_currency, to_currency, amount):
        amount = round(amount * conversion_rates[to_currency], 2)
        return amount

    def covertSwitch(self):

        try:
            amount = float(self.amountEnt.get())
            from_curr = conversion_rates
            to_curr = self.currency_cb.get()

            covert_amount = self.currencyConvert(from_curr, to_curr, amount)
            result.set(covert_amount)
        except ValueError:
            messagebox.showerror('Error!!!', "No or Invalid Amount Detected")
            self.amountEnt.delete(0, END)
        except KeyError:
            messagebox.showerror("Error", "Please Select Currency")

        player = open('details_of_.txt', 'a')
        player.write("New Amount From " + str(self.currency_cb.get()))
        player.write('\n')
        player.write("Amount: " + self.new_curr_amountEnt.get())
        player.write('\n')

    def clear(self):
        self.amountEnt.delete(0, END)
        self.currency_cb.set('Select')
        self.new_curr_amountEnt.delete(0, END)

    def toClaim(self):
        root.destroy()
        import Bank


x = covert(root)
root.mainloop()
