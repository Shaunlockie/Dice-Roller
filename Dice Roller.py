import random
from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Dice Roller")
root.geometry('425x300')
root.minsize(500, 300)
root.configure(background='white')

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

buttonFrame = Frame(root)
buttonFrame.grid(row=2, column=0, sticky="nswe")
buttonFrame.grid_columnconfigure(0, weight = 5)
buttonFrame.grid_columnconfigure(1, weight = 5)
buttonFrame.grid_columnconfigure(2, weight = 5)
buttonFrame.grid_columnconfigure(3, weight = 5)
buttonFrame.grid_columnconfigure(4, weight = 5)
buttonFrame.grid_columnconfigure(5, weight = 5)

modFrame = Frame(root)
modFrame.grid(row=3, column=0, stick="nswe")
modFrame.grid_columnconfigure(0, weight=1)
modFrame.grid_columnconfigure(1, weight=1)

img = Image.open("images\dice.png")
img = img.resize((200,200),Image.ANTIALIAS)
newImg = ImageTk.PhotoImage(img)

var = StringVar(root)
var.set("0")
roll = IntVar()
diceRolled = IntVar()
modVar = IntVar()


def main():
    rollLbl = Label(root, textvariable=roll, padx=10, pady = 10, justify=CENTER, background='white').grid(sticky="n",row=0, columnspan=5)
    diceLbl = Label(root, image = newImg, textvariable = diceRolled , compound = "center", padx=10, pady = 10, justify=CENTER, background='white',font=("Courier", 29)).grid(sticky="nsew",row=1, columnspan=5)

    d4Button = Button(buttonFrame, text="Roll D4", command=lambda: d4_roll(modifier), padx=10, pady = 10, background='white').grid(row=2, column=0, sticky="nsew")
    d6Button = Button(buttonFrame, text="Roll D6", command=lambda: d6_roll(modifier), padx=10, pady = 10, background='white').grid(row=2, column=1, sticky="nsew")
    d8Button = Button(buttonFrame, text="Roll D8", command=lambda: d8_roll(modifier), padx=10, pady = 10, background='white').grid(row=2, column=2, sticky="nsew")
    d10Button = Button(buttonFrame, text="Roll D10", command=lambda: d10_roll(modifier), padx=10, pady = 10, background='white').grid(row=2, column=3, sticky="nsew")    
    d20Button = Button(buttonFrame, text="Roll D20", command=lambda: d20_roll(modifier),  padx=10, pady = 10, background='white').grid(row=2, column=4, sticky="nsew")  
    d100Button = Button(buttonFrame, text="Roll D100", command=lambda: d100_roll(modifier), padx=10, pady = 10, background='white').grid(row=2, column=5, sticky="nsew")
    
    modLbl = Label(modFrame, text = "Modifier:", width = 20, justify=LEFT, background='white').grid(row = 3, columnspan = 4,  sticky="nsew")
    modifier = Spinbox(modFrame, from_=-5, to=10, textvariable=modVar)
    modifier.grid(row=3, column=5, sticky="nsew")
            
def d4_roll(modifier):
    d4 = random.randint(1,4) + int(modifier.get())
    roll.set("D4 result was  " + str(d4))
    diceRolled.set(str(d4))
    return d4 

def d6_roll(modifier):
    d6 = random.randint(1,6) + int(modifier.get())
    roll.set("D6 result was " + str(d6))
    diceRolled.set(str(d6))
    return d6

def d8_roll(modifier):
    d8 = random.randint(1,8) + int(modifier.get())
    roll.set("D8 result was " + str(d8))
    diceRolled.set(str(d8))
    return d8

def d10_roll(modifier):
    d10 = random.randint(1,8) + int(modifier.get())
    roll.set("D10 Result was " + str(d10))
    diceRolled.set(str(d10))
    return d10
    
def d20_roll(modifier):
    d20 = random.randint(1,20) + int(modifier.get())
    if d20 == 1:
        roll.set("D20 result was " + str(d20) + "   Critical Fail!")
        diceRolled.set(str(d20))
    elif d20 == 20:
        roll.set("D20 result was " + str(d20)+ "    Critical Hit!")
        diceRolled.set(str(d20))
    else:
        roll.set("D20 result was " + str(d20))
        diceRolled.set(str(d20))
    return d20
    
def d100_roll(modifier):
    d100 = random.randint(1,100) + int(modifier.get())
    d100Moded = d100 
    roll.set("D100 result was " + str(d100))
    diceRolled.set(str(d100))
    return d100 


main()
root.mainloop()
