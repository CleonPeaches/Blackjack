import blackjackUtilities as util, time, pdb

def main():
    
    listOfPlayers = []

    dealer = util.Dealer()
    dealer.name = 'Winston the Dealer'

    util.printIntro(dealer)
    
    numPlayers = int(util.getNumPlayers())
    
    util.populatePlayerList(listOfPlayers, numPlayers)

    isPlaying = True

    while isPlaying == True:

        deck = util.getDeck()

        shuffledDeck = util.shuffle(deck)

        print('Shuffling deck...\n')
        time.sleep(1)
        
        #Shuffles deck 10 times
        for i in range (10):
            shuffledDeck = util.shuffle(shuffledDeck)

        util.dealFirstHand(dealer, listOfPlayers, shuffledDeck)

        #TODO Display all cards after EACH action
        util.displayAllCards(dealer, listOfPlayers, shuffledDeck)

        util.getAllActions(listOfPlayers, shuffledDeck)

        #TODO
        #Dealer reveals card and hits

        #Compare scores and declare winners
        

        #Ask for another hand
        isPlaying = util.askForAnotherHand(listOfPlayers, dealer)
           
if __name__ == '__main__':
    main()
            
