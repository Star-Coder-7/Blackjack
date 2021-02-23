import random
import tkinter as tk


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


def dealCard(frame):
    nextCard = deck.pop(0)
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
    dealerScore = scoreHand(dealerHand)
    while 0 < dealerScore < 17:
        dealerHand.append(dealCard(dealerCardFrame))
        dealerScore = scoreHand(dealerHand)
        dealerScoreLabel.set(dealerScore)

    playerScore = scoreHand(playerHand)

    if playerScore > 21:
        resultText.set("Dealer Wins!")
    elif dealerScore > 21 or dealerScore < playerScore:
        resultText.set("Player Wins!")
    elif dealerScore > playerScore:
        resultText.set("Dealer Wins!")
    else:
        resultText.set("It's a Draw!")


def dealPlayer():
    playerHand.append(dealCard(playerCardFrame))
    playerScore = scoreHand(playerHand)
    playerScoreLabel.set(playerScore)

    if playerScore > 21:
        resultText.set("Dealer Wins!")
    elif playerScore == 21:
        resultText.set("BlackJack!")
    # global playerScore
    # global playerAce
    # cardValue = dealCard(playerCardFrame)[0]
    # if cardValue == 1 and not playerAce:
    #     playerAce = True
    #     cardValue = 11
    # playerScore += cardValue
    # if playerScore > 21 and playerAce:
    #     playerScore -= 10
    #     playerAce = False
    # playerScoreLabel.set(playerScore)
    # if playerScore > 21:
    #     resultText.set("Dealer Wins!")
    # if playerScore == 21:
    #     resultText.set("BlackJack!")
    # print(locals())


gameWindow = tk.Tk()
gameWindow.title('BLACKJACK')
gameWindow.geometry('640x480+0+0')
gameWindow.config(bg='green')

resultText = tk.StringVar()
result = tk.Label(gameWindow, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tk.Frame(gameWindow, relief='ridge', bd=1, bg='green')
cardFrame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealerScoreLabel = tk.IntVar()
tk.Label(cardFrame, text='Dealer', bg='green', fg='white').grid(row=0, column=0)
tk.Label(cardFrame, textvariable=dealerScoreLabel, bg='green', fg='white').grid(row=1, column=0)

dealerCardFrame = tk.Frame(cardFrame, bg='green')
dealerCardFrame.grid(row=0, column=1, sticky='ew', rowspan=2)

playerScoreLabel = tk.IntVar()

tk.Label(cardFrame, text='Player', bg='green', fg='white').grid(row=2, column=0)
tk.Label(cardFrame, textvariable=playerScoreLabel, bg='green', fg='white').grid(row=3, column=0)

playerCardFrame = tk.Frame(cardFrame, bg='green')
playerCardFrame.grid(row=2, column=1, sticky='ew', rowspan=2)

buttonFrame = tk.Frame(gameWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky='w')

dealerButton = tk.Button(buttonFrame, text='Dealer', command=dealDealer)
dealerButton.grid(row=0, column=0)

playerButton = tk.Button(buttonFrame, text='Player', command=dealPlayer)
playerButton.grid(row=0, column=1)

cards = []
loadImages(cards)
print(cards)

deck = list(cards)
random.shuffle(deck)

dealerHand = []
playerHand = []

dealPlayer()
dealerHand.append(dealCard(dealerCardFrame))
dealerScoreLabel.set(scoreHand(dealerHand))
dealPlayer()

gameWindow.mainloop()

