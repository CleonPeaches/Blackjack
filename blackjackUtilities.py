__name__ = 'blackjackUtilities'

import random, time, sys

#Parent class of Human and Dealer
class Player(object):

    def __init__(self):
        self.total = 0
        self.cards = []
        self.name = ''
        self.bust = False

    def hit(self, deck):
        self.cards.append(deck.pop())

    def checkForBust(self):
        if self.total > 21:
            for card in self.cards:
                if card.isAce == True:
                    card.value = 1
                    self.getTotal()
                    break

            self.bust = True
            print(self.name, ' busted!')
            
    def getTotal(self):
        total = 0
        for card in self.cards:
            total += card.value
            self.total = total


class Human(Player):
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.total = 0
        self.bust = False

    def quit(self, deck):
        choice = ''
        while choice != '1' and choice != '2':
            choice = input ('Are you sure you want to quit? [1] Quit [2] Back: ')
        if choice == '1':
            sys.exit()
        else:
            self.getAction(deck)

    def getAction(self, deck):
        validSelections = ['1', '2', '3']
        choice = ''
        while choice not in validSelections:
            choice = input('Action is to you, ' + self.name + '. [1] Hit [2] Stand [3] Quit: ')
        if choice == '1':
            self.hit(deck)
            self.getTotal()
            self.checkForBust()
            if self.bust == False:
                self.getAction(deck)
        elif choice == '2':
            print(self.name + ' stands.')
        else:
            self.quit(deck)
            

class Dealer(Player):
    #Overrides Player hit().
    def hit(self, deck):
        while self.total < 17:
            self.cards.append(deck.pop())
            displayAllCards()
            self.setTotal()
            self.checkForBust()

    def snideExpression(self):
        snideExpressions = ['*' + self.name + ' smiles confidently*\n',
                            '*' + self.name + ' smirks at your current circumstance*\n',
                            '*' + self.name + ' yawns*\n',
                            '*' + self.name + ' muses to himself that the drapes are looking particularly dull today*\n',
                            '*' + self.name + ' grows weary of being surrounded by drunkards*',
                            '*' + self.name + ' shakes his head in disappointment*',
                            '*You get the impression that ' + self.name + ' is filled with ennui*']

        return snideExpressions[random.randint(0, len(snideExpressions) - 1)]


class Card(object):
    def __init__(self, name, value, isAce):
        self.name = name
        self.value = value
        self.isAce = isAce


def getDeck():
    #Creates an ordered deck of card objects.
    nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = [' of Diamonds', ' of Spades', ' of Clubs', ' of Hearts']
    deck = []

    for num in nums:
        for suit in suits:
            isAce = False  
            name = num + suit
            try:
                value = int(num)
            except(ValueError):
                if num == 'Ace':
                    value = 11
                    isAce = True
                else:
                    value = 10
            deck.append(Card(name, value, isAce))

    return deck

#Takes a list of card objects and shuffles it.
def shuffle(deck):
    shuffledDeck = []
    for i in range(52):
        index = random.randint(0, len(deck) - 1)        
        shuffledDeck.append(deck[index])
        deck.remove(deck[index])
        
    return shuffledDeck


def printIntro(dealer):
    print('WELCOME TO CASINO DE', dealer.name.upper(), '\n')


#Returns number of players at the table.
def getNumPlayers():
    validSelections = [str(x) for x in range(1,8)]
    numPlayers = ''

    while numPlayers not in validSelections:
        numPlayers = input('How many will be playing Blackjack this evening? [1-7] ')

    return int(numPlayers)


#Returns name of human player.
def getName(playerNum):
    name = input('What is your name, player ' + str(playerNum) + '? ')
    return name


#Populates listOfPlayers with Human player objects and welcomes them to table.
def populatePlayerList(listOfPlayers, numPlayers):
    for i in range(numPlayers):
        name = getName(str(i + 1))
        listOfPlayers.append(Human(name))
        
    print('Welcome to the table, ', end='')
    for i in range(len(listOfPlayers)):
        if i == len(listOfPlayers) and len(listOfPlayers) > 1:
            print('and ' + listOfPlayers[i].name + '.\n')
        elif i == len(listOfPlayers) - 1:
            print(listOfPlayers[i].name + '.\n')
        else:
            print(listOfPlayers[i].name + ', ', end='')


def dealFirstHand(dealer, listOfPlayers, deck):
    for i in range(2):
        dealer.cards.append(deck.pop())
        for player in listOfPlayers:
            player.cards.append(deck.pop())

    
def getAllActions(listOfPlayers, deck):
    for player in listOfPlayers:
        player.getAction(deck)

def displayAllCards(dealer, listOfPlayers, deck):
    print(dealer.name + '\'s hand: ' + dealer.cards[0].name + ', [?]', end='')
    for player in listOfPlayers:
        print('\n' + player.name + '\'s hand: ', end='')
        for card in player.cards:
            print(card.name + ' ', end='')

    print('\n' + dealer.snideExpression() + '\n')

def askForAnotherHand(listOfPlayers, dealer):
    validSelections = ['1', '2']
    isPlaying = False
    choice = ''
    while choice not in validSelections:
        choice = input('Another hand? [1] Yes [2] No: ')
    if choice == '1':
        dealer.cards = []
        dealer.points = 0
        dealer.bust = False
        for player in listOfPlayers:
            player.cards = []
            player.points = 0
            player.bust = False
            isPlaying = True
    else:
        print('*' + dealer.name + ' does not seem to mind that you are leaving.*')
        time.sleep(1)

    return isPlaying
