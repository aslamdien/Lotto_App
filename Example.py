import tkinter as tk
from random import sample

# This creates the window object for the application
window = tk.Tk()

window.title('Lotto Generator')
window.resizable(0, 0)

# Creating the widgets
label1 = tk.Label(window, text = '...', relief='groove', width = 2)
label2 = tk.Label(window, text = '...', relief='groove', width = 2)
label3 = tk.Label(window, text = '...', relief='groove', width = 2)
label4 = tk.Label(window, text = '...', relief='groove', width = 2)
label5 = tk.Label(window, text = '...', relief='groove', width = 2)
label6 = tk.Label(window, text = '...', relief='groove', width = 2)
getNumbers = tk.Button(window, text = 'Get Your Lotto Numbers')
resetNumbers = tk.Button(window, text = 'Reset Numbers')

# Designing the layout of the widgets
label1.grid(row = 1, column = 2, padx = 10)
label2.grid(row = 1, column = 3, padx = 10)
label3.grid(row = 1, column = 4, padx = 10)
label4.grid(row = 1, column = 5, padx = 10)
label5.grid(row = 1, column = 6, padx = 10)
label6.grid(row = 1, column = 7, padx = (10, 20))
getNumbers.grid(row = 2, column = 2, columnspan = 4)
resetNumbers.grid(row = 2, column = 6, columnspan = 2)



resetNumbers.configure(state = tk.DISABLED)



def pickNumbers():
    numbers = sample( range(1, 59), 6)
    label1.configure(text = numbers[0])
    label2.configure(text = numbers[1])
    label3.configure(text = numbers[2])
    label4.configure(text = numbers[3])
    label5.configure(text = numbers[4])
    label6.configure(text = numbers[5])
    getNumbers.configure( state = tk.DISABLED)
    resetNumbers .configure( state = tk.NORMAL)

def reset():
    label1.configure(text = '...')
    label2.configure(text = '...')
    label3.configure(text = '...')
    label4.configure(text = '...')
    label5.configure(text = '...')
    label6.configure(text = '...')
    getNumbers.configure( state = tk.NORMAL)
    resetNumbers .configure( state = tk.DISABLED)

getNumbers.configure( command = pickNumbers)
resetNumbers .configure( command = reset)


# The mainloop syntax sustains the window being open for the application
window.mainloop()
