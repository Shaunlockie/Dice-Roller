import random
from tkinter import *

root = Tk()
root.title("Dice Roller")
root.resizable(width=FALSE, height=FALSE)
root.geometry('375x300')
roll = StringVar()
def main():
    RollLbl = Label(root, textvariable=roll, padx=10, pady = 10, justify=LEFT).grid(sticky="w",row=0, columnspan=5)
    
    d4Button = Button(root, text="Roll D4", command=d4_roll, height = 2, width = 5, padx=10, pady = 10).grid(row=1, column=0)
    d6Button = Button(root, text="Roll D6", command=d6_roll, height = 2, width = 5, padx=10, pady = 10).grid(row=1, column=1)
    d8Button = Button(root, text="Roll D8", command=d8_roll, height = 2, width = 5, padx=10, pady = 10).grid(row=1, column=2)
    d10Button = Button(root, text="Roll D10", command=d10_roll,height = 2, width = 5, padx=10, pady = 10).grid(row=1, column=3)    
    d20Button = Button(root, text="Roll D20", command=d20_roll, height = 2, width = 5, padx=10, pady = 10).grid(row=1, column=4)  
    d100Button = Button(root, text="Roll D100", command=d100_roll, height= 2, width = 5, padx=10, pady = 10).grid(row=1, column=5)  

    
def d4_roll():
    d4 = random.randint(1,4)
    roll.set("D4 result was  " + str(d4))
    return d4 

def d6_roll():
    d6 = random.randint(1,6)
    roll.set("D6 result was " + str(d6))
    return d6

def d8_roll():
    d8 = random.randint(1,8)
    roll.set("D8 result was " + str(d8))
    return d8

def d10_roll():
    d10 = random.randint(1,8)
    roll.set("D10 Result was " + str(d10))
    return d10
    
def d20_roll():
    d20 = random.randint(1,20)
    if d20 == 1:
        roll.set("D20 result was " + str(d20) + "   Critical Fail!")
    elif d20 == 20:
        roll.set("D20 result was " + str(d20)+ "    Critical Hit!")
    else:
        roll.set("D20 result was " + str(d20))
    return d20
    
def d100_roll():
    d100 = random.randint(1,100)
    roll.set("D100 result was " + str(d100))
    return d100


main()
root.mainloop()
