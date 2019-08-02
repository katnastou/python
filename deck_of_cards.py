from random import shuffle

#Card 

class Card:
#    Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades"). --done
#    Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"). --done   
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        
#    Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.) --done
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

#Deck 

class Deck:
    
    #    Each instance of Deck  should have a cards attribute with all 52 possible instances of Card . -- Done
    def __init__(self):
        
        valid_suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        valid_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] 
        self.cards = [Card(value,suit) for value in valid_value for suit in valid_suit]
        #print(self.cards)
        #without list comprehension
        # for x in valid_suit:
        #     for y in valid_value:
        #         new_card = Card(x,y)
        #         self.cards.append(new_card)
               
    #    Deck  should have an instance method called count  which returns a count of how many cards remain in the deck. -- Done
    def count(self):
        return len(self.cards)               
    
    #    Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)  -- Done
    def __repr__(self):
        return "Deck of {} cards".format(self.count())  

    #Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck 
    #(it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method 
    #should return a ValueError  with the message "All cards have been dealt".
    def _deal(self, num_of_cards):
        count =self.count()
        actual_num = min([count,num_of_cards])
        #print("Going to remove {} cards".format(actual_num))
        if count == 0:
            raise ValueError("All cards have been dealt")
        hand = self.cards[-actual_num:] #s;ice actual_num positions from the end, to the end e.g. [1,2,3,4,5,6] slice[-3:] --> [1,2,3]
        self.cards = self.cards[:-actual_num]
        return hand
        
        
    #    Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
    def deal_card(self):
        return self._deal(1)[0] #_deal returns a list, to get a single element we return the 0th element
    #    Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.
    def deal_hand(self,num_of_cards):
        return self._deal(num_of_cards)

    #Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. 
    #If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  
    #shuffle should return the shuffled deck.
    def shuffle(self):
        if self.count() == 52:
            shuffle(self.cards)
            return self
        else:
            raise ValueError("Only full decks can be shuffled")
            
d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()