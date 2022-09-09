import time

from tkinter import *

background=Tk()

## Setting background parameters
background.title('PiTimer')
background.config(bg='black')
background.geometry("300x150")

def timerstart():
    timer = ent.get()
    if timer == 5:
        print('Your timer for', timer, 'seconds starts NOW!')
    else:
        print('Invalid input')
        exit()

## Display 'PiTimer' text at the top of the window
lbl=Label(background, text="PiTimer", fg='grey', bg='black', font=('arial', 20))
lbl.pack(side=TOP, anchor=N, pady=5)

ent=Entry(background, fg='blue', bg='white', font=('arial', 15))
ent.pack(anchor=N, pady=10)

## Displas the start button
btn=Button(background, text="Start", fg='red', bg='black', font=('arial', 10), command=timerstart)
btn.pack(side=BOTTOM, anchor=N, pady=10)

background.mainloop()
