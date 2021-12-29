import random

suits = ("Clubs", "Diamonds", "Hearts", "Spades")
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f"A {self.rank} of {self.suit}"

      
class Deck:
    def __init__(self):
        self.all_cards = []
    
    def full_deck(self):
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
        
    def shuffle(self):
        random.shuffle(self.all_cards)

       
class Player:
    def __init__(self, name, position, bet):
        self.name = name
        self.position = position + 1
        self.bet = bet
        self.hand = []
        self.hand_value = 0
        self.money = 0
    
    def hit(self, card):
        self.hand.append(card)
        
        print(f"{self.name}, Player {self.position}, has decided to hit")
        
        print(f"{self.name} now has the following cards in their hand:")
    
        for asset in self.hand:
            print(asset)
        
        print("\n")
        
        print(f"We are about to update the hand value of {self.name}, Player {self.position}")
        
        if card.rank == "Ace":
            print(f"This card is an Ace. You will need to choose the value of your Ace")
                
            while True:
                
                try:
                    ace_value = int(input("Enter either 1 or 11: "))
                    
                except:
                    print("You have not entered an integer value. Please try again")
                    continue
                
                else:
                    
                    if ace_value not in [1, 11]:
                        print("You have not entered a valid number. Please try again.")
                        continue
                    
                    else:
                        self.hand_value = self.hand_value + ace_value
                        break
                    
        if card.rank == "Two":
            self.hand_value = self.hand_value + 2
            
        if card.rank == "Three":
            self.hand_value = self.hand_value + 3
            
        if card.rank == "Four":
            self.hand_value = self.hand_value + 4
            
        if card.rank == "Five":
            self.hand_value = self.hand_value + 5
            
        if card.rank == "Six":
            self.hand_value = self.hand_value + 6
            
        if card.rank == "Seven":
            self.hand_value = self.hand_value + 7
            
        if card.rank == "Eight":
            self.hand_value = self.hand_value + 8
            
        if card.rank == "Nine":
            self.hand_value = self.hand_value + 9
            
        if card.rank in ["Ten", "Jack", "Queen", "King"]:
            self.hand_value = self.hand_value + 10
        
        print(f"The new hand value for {self.name}, Player {self.position}, is {self.hand_value}")

    def starting_hand_value(self):
        
        print(f"{self.name}, Player {self.position}, we are about to calculate the value of your starting hand")
        
        for card in self.hand:
            i = self.hand.index(card)
            
            if card.rank == "Ace":
                print(f"Card in index {i} is an Ace. You will need to choose the value of your Ace")
                
                while True:
                    
                    try:
                        ace_value = int(input("Enter either 1 or 11: "))
                        
                    except:
                        print("You have not entered an integer value. Please try again")
                        continue
                    
                    else:
                        
                        if ace_value not in [1, 11]:
                            print("You have not entered a valid number. Please try again.")
                            continue
                        
                        else:
                            self.hand_value = self.hand_value + ace_value
                            break
            
            if card.rank == "Two":
                self.hand_value = self.hand_value + 2
                
            if card.rank == "Three":
                self.hand_value = self.hand_value + 3
                
            if card.rank == "Four":
                self.hand_value = self.hand_value + 4
                
            if card.rank == "Five":
                self.hand_value = self.hand_value + 5
                
            if card.rank == "Six":
                self.hand_value = self.hand_value + 6
                
            if card.rank == "Seven":
                self.hand_value = self.hand_value + 7
                
            if card.rank == "Eight":
                self.hand_value = self.hand_value + 8
                
            if card.rank == "Nine":
                self.hand_value = self.hand_value + 9
                
            if card.rank in ["Ten", "Jack", "Queen", "King"]:
                self.hand_value = self.hand_value + 10
                
        print(f"The starting hand value for {self.name}, Player {self.position}, is {self.hand_value}\n")
        

        
    def __str__(self):
        return f"This is {self.name}, Player {self.position}, with an original bet of {self.bet}."


class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.money = 0
        
    def starting_hand_value(self):
        
        for card in self.hand:
            
            if card.rank == "Ace":
                self.hand_value = self.hand_value + 11
                
            if card.rank == "Two":
                self.hand_value = self.hand_value + 2
                
            if card.rank == "Three":
                self.hand_value = self.hand_value + 3
                
            if card.rank == "Four":
                self.hand_value = self.hand_value + 4
                
            if card.rank == "Five":
                self.hand_value = self.hand_value + 5
                
            if card.rank == "Six":
                self.hand_value = self.hand_value + 6
                
            if card.rank == "Seven":
                self.hand_value = self.hand_value + 7
                
            if card.rank == "Eight":
                self.hand_value = self.hand_value + 8
                
            if card.rank == "Nine":
                self.hand_value = self.hand_value + 9
                
            if card.rank in ["Ten", "Jack", "Queen", "King"]:
                self.hand_value = self.hand_value + 10
        
        print(f"The starting hand value for the dealer is {self.hand_value}\n")
    
    def hit(self, card):
        self.hand.append(card)
        
        #print(f"{self.name}, Player {self.position}, has decided to hit")
        
        print("Dealer now has the following cards in their hand:")
    
        for asset in self.hand:
            print(asset)
        
        print(" ")
        
        print("We are about to update the hand value of the dealer")
        
        if card.rank == "Ace":
            self.hand_value = self.hand_value + 11
                    
        if card.rank == "Two":
            self.hand_value = self.hand_value + 2
            
        if card.rank == "Three":
            self.hand_value = self.hand_value + 3
            
        if card.rank == "Four":
            self.hand_value = self.hand_value + 4
            
        if card.rank == "Five":
            self.hand_value = self.hand_value + 5
            
        if card.rank == "Six":
            self.hand_value = self.hand_value + 6
            
        if card.rank == "Seven":
            self.hand_value = self.hand_value + 7
            
        if card.rank == "Eight":
            self.hand_value = self.hand_value + 8
            
        if card.rank == "Nine":
            self.hand_value = self.hand_value + 9
            
        if card.rank in ["Ten", "Jack", "Queen", "King"]:
            self.hand_value = self.hand_value + 10
        
        print(f"The new hand value for the dealer is {self.hand_value}")

    '''
    def add_card(self, card):
        if type([]) == type(card):
            self.hand.extend(card)
        else:
            self.hand.append(card)
    '''
            
def get_number_of_players():
    
    while True:
        
        try:
            game_number_of_players = int(input("How many players, excluding the dealer, will be playing this game?: "))
            
        except:
            print("You have not entered a valid number. Try again")
            continue
        
        else:
            return game_number_of_players
            break
        
def get_list_of_game_players(number):
    
    list_of_players = []
    
    for i in range(number):
        player_name = "1"
        
        while player_name.isnumeric() == True:
            player_name = input(f"Enter the name of Player {i+1}: ")
            
            if player_name.isnumeric() == True:
                print("You have not entered a valid value. Try again")
                
            else:
                break

        while True:
            
            try:
                player_bet = int(input(f"Enter the bet value of Player {i+1}: "))
                
            except:
                print("You have not entered a valid value. Try again")
                continue
            
            else:
                break
        
        list_of_players.append(Player(player_name, i, player_bet))
        
    return list_of_players

def print_game_players(players_list):
    
    for player in players_list:
        print(player)
        
        print(f"{player.name}, Player {player.position} has the following cards in their hand:")
    
        for card in player.hand:
            print(card)
    
        print("\n")
        
def initial_dealings(players_list, card_deck, dealer):
    
    for player in players_list:
        player.hand.append(card_deck.all_cards.pop()) # 1st dealings for the players
    
    dealer.hand.append(card_deck.all_cards.pop()) # 1st dealing for the dealer
    
    for player in players_list:
        player.hand.append(card_deck.all_cards.pop()) # 2nd dealings for the players
    
    dealer.hand.append(card_deck.all_cards.pop()) # 2nd dealing for the dealer. This is the card with face down