
import pandas
from tkinter import *
import random
BACKROUND_COLOR = "#B1DDC6"
card_side = 0
current_card = {}


def front():
    global current_card
    canvas.itemconfig(card_title,text="EINGLES",fill= "black")
    canvas.itemconfig(card_word,text=(current_card["front"]),fill="black")
    canvas.itemconfig(card_image,image=f_image)
    

try:
    data = pandas.read_csv("data/words_to_lern")
except FileNotFoundError:
    or_data = pandas.read_csv("data/card_data.csv")
    to_lern = or_data.to_dict(orient="records")
else:
    to_lern = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_lern)
    canvas.itemconfig(card_title,text="EINGLES",fill= "black")
    canvas.itemconfig(card_word,text=(current_card["front"]),fill="black")
    canvas.itemconfig(card_image,image=f_image)
    
def side():
    global card_side
    canvas.itemconfig(card_image, image= b_image)
    canvas.itemconfig(card_title, text= "עברית",fill= "white")
    canvas.itemconfig(card_word, text=current_card["back"],fill= "white")
    if card_side == 1:
        front()
        print("f")
        card_side = 0
    elif card_side == 0:
        side()
        print("b")
        card_side = 1


def is_known():
    to_lern.remove(current_card)
    data = pandas.DataFrame(to_lern)
    data.to_csv("data/words_to_lern",index= False)
    next_card()

win = Tk()
win.title("כרטיסיות אנגלית")
win.config(padx=50,pady= 50, bg=BACKROUND_COLOR)

f_image = PhotoImage(file="images/card_front.png")
b_image = PhotoImage(file="images/card_back.png")



canvas = Canvas(width=800,height=526)
card_image = canvas.create_image(400,263,image=f_image)
card_title = canvas.create_text(400, 150, text="Titel",font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text="word in en",font=("Ariel", 60, "italic"))
canvas.config(bg=BACKROUND_COLOR,highlightthickness= 0)
canvas.grid(row=0, column=0,columnspan=3)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image,highlightthickness=0,command=next_card)
cross_button.grid(row= 1, column= 0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image,highlightthickness=0,command=is_known)
check_button.grid(row=1, column=2)

side_image = PhotoImage(file="images/side.png")
side_button = Button(image=side_image,highlightthickness=0,command=side)
side_button.grid(row=1,column=1)



next_card()
win.mainloop()
