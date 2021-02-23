from random import shuffle
from random import choice
import tkinter as tk
from tkinter.messagebox import showinfo

name1 = input("Please enter player 1's name (The Dealer): ")
name2 = input("Please enter player 2's name (The Player): ")

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'white', 'gray', 'black', 'maroon',
          'turquoise', 'cyan', 'magenta', 'indigo', 'violet']

print("\nThese are all the colors that the game can contain: ", colors)

userChoice = str(input("\nDo you want me to remove any colors from the list?\n If you want me to, just enter the color "
                       "and I will remove it for you,\n or else just press enter if you don't want me to remove any "
                       "colors: ")).lower()

while userChoice != "":
    if userChoice in colors:
        print("\nAlright, I will remove that color for you.")
        colors.remove(userChoice)
        userChoice = str(input("\nDo you want me to remove any colors from the list?\n If you want me to, just enter "
                               "the color and I will remove it for you,\n or else just press enter if you don't want me"
                               " to remove any colors: ")).lower()

    else:
        print("\nSorry, that's an invalid response!")
        userChoice = str(input("\nDo you want me to remove any colors from the list?\n If you want me to, just enter "
                               "the color and I will remove it for you,\n or else just press enter if you don't want me"
                               " to remove any colors: ")).lower()
else:
    print("Alright, here is the final color list: ", colors)


def loadImages(cardImages):
    suits = ['club', 'heart', 'spade', 'diamond']
    faces = ['jack', 'queen', 'king']

    if tk.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:

        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            cardImages.append((card, image,))

        for card in faces:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            cardImages.append((10, image,))


def _dealCard(frame):
    nextCard = deck.pop(0)
    deck.append(nextCard)
    tk.Label(frame, image=nextCard[1], relief='raised').pack(side='left')
    return nextCard


def scoreHand(hand):
    score = 0
    ace = False
    for nextCard in hand:
        cardValue = nextCard[0]
        if cardValue == 1 and not ace:
            ace = True
            cardValue = 11
        score += cardValue
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def dealDealer():
    global dealerPoints
    global playerPoints

    dealerScore = scoreHand(dealerHand)
    while 0 < dealerScore < 17:
        dealerHand.append(_dealCard(dealerCardFrame))
        dealerScore = scoreHand(dealerHand)
        dealerScoreLabel.set(dealerScore)

    playerScore = scoreHand(playerHand)

    if playerScore > 21:
        showinfo(name1, "Dealer Wins!")
        reset()
        thePoints = dealerPoints.get() + 1
        dealerPoints.set(thePoints)
    elif dealerScore > 21 or dealerScore < playerScore:
        showinfo(name2, "Player Wins!")
        reset()
        thePoints = playerPoints.get() + 1
        playerPoints.set(thePoints)
    elif dealerScore > playerScore:
        showinfo(name1, "Dealer Wins!")
        reset()
        thePoints = dealerPoints.get() + 1
        dealerPoints.set(thePoints)
    else:
        showinfo(name1 + " and " + name2, "It's a Draw!")
        reset()
        dealerPoints.set(dealerPoints.get())
        playerPoints.set(playerPoints.get())


def dealPlayer():
    global dealerPoints

    playerHand.append(_dealCard(playerCardFrame))
    playerScore = scoreHand(playerHand)
    playerScoreLabel.set(playerScore)

    if playerScore > 21:
        showinfo(name1, "Dealer Wins!")
        reset()
        thePoints = dealerPoints.get() + 1
        dealerPoints.set(thePoints)


def newGame():
    finalPlayerScore = playerPoints.get()
    finalDealerScore = dealerPoints.get()

    if finalPlayerScore > finalDealerScore:
        showinfo(name2, "Well done! You have won the whole game!!!")
        reset()
        playerPoints.set(0)
        dealerPoints.set(0)
    elif finalDealerScore > finalPlayerScore:
        showinfo(name1, "Well done! You have won the whole game!!!")
        reset()
        playerPoints.set(0)
        dealerPoints.set(0)
    else:
        showinfo(name1 + " and " + name2, "Well done! You both have drawn the game!!!")
        reset()
        playerPoints.set(0)
        dealerPoints.set(0)


def initialDeal():
    dealPlayer()
    dealerHand.append(_dealCard(dealerCardFrame))
    dealerScoreLabel.set(scoreHand(dealerHand))
    dealPlayer()


def reset():
    global playerHand
    global dealerHand
    global playerCardFrame
    global dealerCardFrame

    playerHand.clear()
    dealerHand.clear()

    playerCardFrame.destroy()
    playerCardFrame = tk.Frame(cardFrame, bg=choice(colors))
    playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

    dealerCardFrame.destroy()
    dealerCardFrame = tk.Frame(cardFrame, bg=choice(colors))
    dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

    playerHand = []
    dealerHand = []

    playerButton.config(state='normal')
    dealerButton.config(state='normal')

    shuffle(deck)
    initialDeal()


def instructions():
    showinfo(name1 + " and " + name2, "Welcome to this game of blackjack. You 2 will in turns click the respective "
                                      "button and a random card will show up on the screen. There is a new game button "
                                      "which resets everything and determines the winner, the reset button just resets "
                                      "everything. The score for the cards' total will show up on the left side. When "
                                      "someone wins a round, or a whole game, the game will automatically determine "
                                      "the winner, and adds up the score or resets the score for new game. If you do "
                                      "not know the rules of blackjack, just do some satisfying research on google to "
                                      "study the rules, then you can play with each other. Good luck to both of you, "
                                      "Hope you 2 enjoy the game and have fun together!!!")


def quit():
    showinfo(name1 + " and " + name2, "Thank you for interacting with this game, maybe next time!!!")
    gameWindow.destroy()


def play():
    initialDeal()
    gameWindow.mainloop()


gameWindow = tk.Tk()
gameWindow.title('BLACKJACK')
gameWindow.geometry('700x600+0+0')
gameWindow.minsize(550, 520)
gameWindow.maxsize(1450, 850)
gameWindow.config(bg=choice(colors))

cardFrame = tk.Frame(gameWindow, relief='ridge', bd=1, bg=choice(colors), width=10, height=10)
cardFrame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealerScoreLabel = tk.IntVar()
tk.Label(cardFrame, text='Dealer', bg=choice(colors), fg=choice(colors)).grid(row=0, column=0)
tk.Label(cardFrame, textvariable=dealerScoreLabel, bg=choice(colors), fg=choice(colors)).grid(row=1, column=0)

dealerCardFrame = tk.Frame(cardFrame, bg=choice(colors))
dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

playerScoreLabel = tk.IntVar()

tk.Label(cardFrame, text='Player', bg=choice(colors), fg=choice(colors)).grid(row=2, column=0)
tk.Label(cardFrame, textvariable=playerScoreLabel, bg=choice(colors), fg=choice(colors)).grid(row=3, column=0)

playerCardFrame = tk.Frame(cardFrame, bg=choice(colors))
playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

buttonFrame = tk.Frame(gameWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')

dealerButton = tk.Button(buttonFrame, text='Dealer', command=dealDealer, bg=choice(colors), fg=choice(colors))
dealerButton.grid(row=0, column=0)

playerButton = tk.Button(buttonFrame, text='Player', command=dealPlayer, bg=choice(colors), fg=choice(colors))
playerButton.grid(row=0, column=1)

mainFrame = tk.Frame(gameWindow, bg=choice(colors), bd=20, width=600, height=300)
mainFrame.grid(row=5, column=0)

playerPoints = tk.IntVar()
dealerPoints = tk.IntVar()

labelPlayerScore = tk.Label(mainFrame, font=('arial', 40, 'bold'), text=name1, bg=choice(colors), fg=choice(colors),
                            padx=2, pady=2)
labelPlayerScore.grid(row=0, column=0, sticky='w')

textPlayerScore = tk.Entry(mainFrame, bd=2, font=('arial', 40, 'bold'), textvariable=dealerPoints, fg=choice(colors),
                           width=5, bg=choice(colors), justify='left')
textPlayerScore.grid(row=0, column=1)

labelDealerScore = tk.Label(mainFrame, font=('arial', 40, 'bold'), text=name2, bg=choice(colors), fg=choice(colors),
                            padx=2, pady=2)
labelDealerScore.grid(row=1, column=0, sticky='w')

textDealerScore = tk.Entry(mainFrame, bd=2, font=('arial', 40, 'bold'), textvariable=playerPoints, fg=choice(colors),
                           width=5, bg=choice(colors), justify='left')
textDealerScore.grid(row=1, column=1)

newGameButton = tk.Button(mainFrame, text='New Game', justify='center', font=('arial', 40, 'bold'), bg=choice(colors),
                          fg=choice(colors), command=lambda: newGame(), padx=2, pady=2)
newGameButton.grid(row=2, column=0)

instructionsButton = tk.Button(mainFrame, text='Instructions', justify='center', font=('arial', 40, 'bold'),
                               fg=choice(colors), bg=choice(colors), command=lambda: instructions(), padx=2, pady=2)
instructionsButton.grid(row=2, column=1)

resetButton = tk.Button(mainFrame, text='Reset', justify='center', font=('arial', 40, 'bold'), bg=choice(colors),
                        fg=choice(colors), command=lambda: reset(), padx=2, pady=2)
resetButton.grid(row=3, column=0)

quitButton = tk.Button(mainFrame, text='Quit', justify='center', font=('arial', 40, 'bold'), bg=choice(colors),
                       fg=choice(colors), command=lambda: quit(), padx=2, pady=2)
quitButton.grid(row=3, column=1)

cards = []
loadImages(cards)
print(cards)

deck = list(cards)
shuffle(deck)

dealerHand = []
playerHand = []

if __name__ == "__main__":
    play()
