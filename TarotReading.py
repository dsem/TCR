# Tarot Reading GUI
from tkinter import *
from PIL import ImageTk, Image
from Deck import *
import random
# Things to work on: add more spreads


def careerSpread():
    global panel
    global spread
    global card_spread
    global click
    career_meanings = ["The first card asks us if our job that we have right now is indeed our ideal job: ",
                       "The second card emphasizes the actions we must take to further boost our career: ",
                       "The third card tells us certain "
                       "things about our job that we can no longer alter: ", "The fourth card refers to our skills "
                       "and if they’re enough to get us a promotion or if we are behind everyone else: ",
                       "The fifth card tells us about the things we can do in our career to improve and start a "
                       "new one or just small things we can do in our current career to at least get noticed: ",
                       "The sixth card tells us if our past mistakes are influencing "
                       "our career now: ", "The final card tells you if you are making any bad career choices,"
                                           " as it might result in you making other bad career choices: "]
    l0.grid_forget()
    bSuccess.destroy()
    bLove.destroy()
    bCareer.destroy()
    click = Label(card_spread, text="Would you like to see your cards?", font=("Ariel", 20))
    click.grid(row=0, column=1, columnspan=3)
    panel.grid()
    card_spread.grid()
    spread = []
    while len(spread) < 7:
        spread.append(drawCard())
    b_yes = Button(card_spread, text="Yes", command=lambda: showCards(True, "career", career_meanings),
                   font=("Ariel", 10), pady=10, padx=10)
    b_yes.grid(column=1)


def successSpread():
    global panel
    global spread
    global card_spread
    global click
    success_meanings = ["This card signifies the true colors of the challenge in front of you. It will help "
                        "you to identify what sort of skill set and resources you will need in order to not "
                        "just solve but also overcome the challenge: ", "This card further clarifies your current "
                        "problems and challenges: ", "The third card reveals the hidden factors affecting your current"
                        " situation. You need to have knowledge about what these factors are to really overcome "
                        "the obstacle you’re facing: ", "The fourth card represents new plans, people, or objects "
                        "that can help you grow further. By adapting yourself to these new aspects, your vision of the "
                        "situation will change, leaving you with better solutions to your problems: ", "The final card "
                        "shows what requirements you need to fulfill in order to be proven successful and things you "
                        "should avoid as they will lead you to failure. It will point you towards success if proven to "
                        "be a positive card but in other cases it could be a negative card and will warn you about an "
                        "upcoming disaster in your life: "]
    l0.grid_forget()
    bSuccess.destroy()
    bLove.destroy()
    bCareer.destroy()
    click = Label(card_spread, text="Would you like to see your cards?", font=("Ariel", 20))
    click.grid(row=0, column=1)
    panel.grid()
    card_spread.grid()
    spread = []
    while len(spread) < 6:
        spread.append(drawCard())
    b_yes = Button(card_spread, text="Yes", command=lambda: showCards(True, "success", success_meanings), font=("Ariel", 10),
                   pady=10, padx=10)
    b_yes.grid(column=1)


def loveSpread():
    global panel
    global spread
    global card_spread
    global click
    love_meanings = ["This card signifies what you currently feel about your relationship, your approach, and your "
                     "outlook: ", "This card represents your partner's current emotions towards you, their attitude, "
                                  "and expectations about your relationship: ", "This card is a connection card. It"
                     " represents commonalities between you and your partner: ", "This card indicates the strength of "
                     "your relationship: ", "This card shows the weaknesses in your relationship: ",
                     "This final card is your true love card. It interprets if the relationship is going to be "
                     "successful or not: "]
    l0.grid_forget()
    bLove.destroy()
    bSuccess.destroy()
    bCareer.destroy()
    click = Label(card_spread, text="Would you like to see your cards?", font=("Ariel", 20))
    click.grid(row=0, column=1)
    panel.grid()
    card_spread.grid()
    spread = []
    while len(spread) < 6:
        spread.append(drawCard())
    b_yes = Button(card_spread, text="Yes", command=lambda: showCards(True, "love", love_meanings), font=("Ariel", 10),
                   pady=10, padx=10)
    b_yes.grid(column=1)


# shows card meanings based on the spread that is chosen
# card = tarot card from TarotCard class
# image = card image(not path)
# num_card = card number in spread
# type = spread type
# meanings = list of card placement interpretations/meanings based on type of spread
def showMeaning(card, image, num_card, type, meanings):
    global spread
    global panel
    global card_spread
    global m
    card_spread.grid_forget()
    m = Frame(root)
    m.grid()
    interp = meanings[num_card-1]
    meaning = Label(m, text=interp + " " + card.__getMeaning__(), font=("Ariel", 15), wraplength=300,
                    justify="center")
    pic = Label(m, image=image)
    panel.image = image
    back = Button(m, text="Back", command=lambda: showCards(False, type, meanings))
    pic.grid(row=0, column=0)
    meaning.grid(row=0, column=1)
    back.grid(row=2, column=1)


def showCards(start, type, meanings):
    global spread
    global panel
    global click
    global card_spread
    global m
    panel.grid_forget()
    if not start:
        m.grid_forget()
        card_spread.grid()
    click.config(text="Click a card to get it's meaning")
    c_img1 = ImageTk.PhotoImage(Image.open((spread[0].__getPath__())))
    c_img2 = ImageTk.PhotoImage(Image.open((spread[1].__getPath__())))
    c_img3 = ImageTk.PhotoImage(Image.open((spread[2].__getPath__())))
    c_img4 = ImageTk.PhotoImage(Image.open((spread[3].__getPath__())))
    c_img5 = ImageTk.PhotoImage(Image.open((spread[4].__getPath__())))
    c_img6 = ImageTk.PhotoImage(Image.open((spread[5].__getPath__())))
    c1 = Button(card_spread, image=c_img1, command=lambda: showMeaning(spread[0], c_img1, 1, type, meanings))
    c1.image = c_img1
    c2 = Button(card_spread, image=c_img2, command=lambda: showMeaning(spread[1], c_img2, 2, type, meanings))
    c2.image = c_img2
    c3 = Button(card_spread, image=c_img3, command=lambda: showMeaning(spread[2], c_img3, 3, type, meanings))
    c3.image = c_img3
    c4 = Button(card_spread, image=c_img4, command=lambda: showMeaning(spread[3], c_img4, 4, type, meanings))
    c4.image = c_img4
    c5 = Button(card_spread, image=c_img5, command=lambda: showMeaning(spread[4], c_img5, 5, type, meanings))
    c5.image = c_img5
    c1.grid(row=1, column=0)
    c2.grid(row=1, column=1)
    c3.grid(row=1, column=2)
    c4.grid(row=2, column=0)
    c5.grid(row=2, column=1)
    if type != "success":
        c_img6 = ImageTk.PhotoImage(Image.open((spread[5].__getPath__())))
        c6 = Button(card_spread, image=c_img6, command=lambda: showMeaning(spread[5], c_img6, 6, type, meanings))
        c6.image = c_img6
        c6.grid(row=2, column=2)
        if type != "love":
            c_img7 = ImageTk.PhotoImage(Image.open((spread[6].__getPath__())))
            c7 = Button(card_spread, image=c_img7, command=lambda: showMeaning(spread[6], c_img7, 7, type, meanings))
            c7.image = c_img7
            c7.grid(row=2, column=3)


def drawCard():
    num_cards = deck.__cardsLeft__()
    if num_cards > 0:
        c = deck.__draw__(random.randint(0, num_cards - 1))
        # print(str(c.__getArch__()) + " " + str(c.__getType__()) + " " + c.__getName__())
        return c
    else:
        print("No cards left")


global panel
global spread
global card_spread
global click
global m
deck = Deck()
root = Tk()
root.geometry("1400x800")
root.title("Tarot Reading")
card_spread = Frame(root)
img = ImageTk.PhotoImage(Image.open("tarot_pic.jpg"))
panel = Label(root, image=img)
l0 = Label(root, text="What kind of reading would you like today?", font=("Ariel", 20))
bLove = Button(root, text="Love", command=loveSpread, padx=40, pady=80, bg="red")
bSuccess = Button(root, text="Success", command=successSpread, padx=40, pady=80, bg="orange")
bCareer = Button(root, text="Career", command=careerSpread, padx=40, pady=80, bg="blue")
l1 = Label(root, text="Are you ready to start your journey?")
l1.config(font=("Ariel", 30))
bDrawCard = Button(root, text="Draw Card", command=drawCard)
l0.grid()
bLove.grid()
bSuccess.grid()
bCareer.grid()

root.mainloop()
