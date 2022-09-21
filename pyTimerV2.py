import time

from tkinter import *

background=Tk()

## Setting background parameters
background.title('PiTimer')
background.config(bg='black')
background.geometry("300x150")

def timerstart():
timer = get.ent:
    while True:
        try:
            timer = int(input("Enter a number in seconds"))
        except ValueError:
            print("Please, enter a valid number")
            continue
        else:
            time.sleep (timer - 3)
            print('3!')
            time.sleep(1)
            print('2!')
            time.sleep(1)
            print('1!')
            time.sleep(1)
            print('Timer done!')
            break

## Display 'PiTimer' text at the top of the window
lbl=Label(background, text="PiTimer", fg='grey', bg='black', font=('arial', 20))
lbl.pack(side=TOP, anchor=N, pady=5)

ent=Entry(background, fg='blue', bg='white', font=('arial', 15))
ent.pack(anchor=N, pady=10)

## Displas the start button
btn=Button(background, text="Start", fg='red', bg='black', font=('arial', 10), command=timerstart)
btn.pack(side=BOTTOM, anchor=N, pady=10)

background.mainloop()
