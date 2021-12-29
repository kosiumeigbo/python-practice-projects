from game_package import game_module # Importing the game_module module from the game_package package

new_game_deck = game_module.Deck() # Initialising the new deck of cards for the game
new_game_deck.full_deck() # The full deck method to generate the total 52 cards before playing the game
new_game_deck.shuffle() # The full deck of 52 cards is now shuffled

number_of_players = game_module.get_number_of_players() # Getting the number of players for this game

game_players = game_module.get_list_of_game_players(number_of_players) # Getting the list that holds the players of the game

dealer = game_module.Dealer() # Initialising the dealer of the game

game_module.initial_dealings(game_players, new_game_deck, dealer) # Initial dealings for players and dealer

print("Each player now has exactly 2 cards\n")

game_module.print_game_players(game_players) # Print the list of all the players and their cards

print("The dealer now also has 2 cards, with the last card picked face down\n")

print("The dealer has the following card up:\n")
print(dealer.hand[0])
print("")

win_players = []
loss_players = []

for player in game_players:
    
    if (player.hand[0].rank == "Ace" and player.hand[1].rank in ["Ten", "Jack", "Queen", "King"]) or (player.hand[1].rank == "Ace" and player.hand[0].rank in ["Ten", "Jack", "Queen", "King"]):
        print(f"{player.name}, Player {player.position} has a natural")
        player.money = 1.5 * player.bet
        print(f"Your money won is {player.money}")
        print("You are now done for this round\n")
        win_players.append(game_players.pop(game_players.index(player)))

print("We are about to calculate and print the starting hand value of each remaining player in the game that currently does not have a natural")
print("For every Ace ranked card in your hand, each player will need to choose either 1 or 11 for the value of that Ace card")
print("The value for the other ranked cards will automatically be added to the starting hand value\n")

for player in game_players:
    player.starting_hand_value()

for player in game_players:
    print(f"{player.name}, Player {player.position}, it is now your turn in this round")
    continue_turn = True
    
    while continue_turn == True:
        
        while True:
            play_option = input(f"{player.name}, Player {player.position}, enter 'stand' if you would like to stand or 'hit' if you would like to hit: ")
            
            if play_option not in ['stand', 'hit']:
                print("You have not entered a valid value. You will need to try again.")
                continue
            
            else:
                break
        
        if play_option == 'stand':
            print(f"{player.name}, Player {player.position}, you have decided to stand.\n")
            break
        
        else:
            player.hit(new_game_deck.all_cards.pop())
            
            if player.hand_value > 21:
                print(f"{player.name}, Player {player.position}, you have Bust. This means you are out of this round and the dealer will get your bet.\n")
                dealer.money = dealer.money + player.bet
                loss_players.append(game_players.pop(game_players.index(player)))
                break
            
            if player.hand_value == 21:
                print(f"{player.name}, Player {player.position}, you have a natural and are now done for this round.")
                player.money = 1.5 * player.bet
                print(f"Your money won is {player.money}.\n")
                win_players.append(game_players.pop(game_players.index(player)))
                break
            
            if player.hand_value < 21:
                print(f"{player.name}, Player {player.position}, your hand value is less than 21")
                
                while True:
                    y_n = input("Enter 'y' if you would like to continue with your turn or Enter 'n' if you are you through with your turn: ")
                    
                    if y_n not in ['y', 'n']:
                        print("You have not entered a valid value. You will need to try again.")
                        continue
                    
                    else:
                        break
                
                if y_n == 'y':
                    break
                
                else:
                    continue_turn = False

print("The second card of the dealer has now been turned over and it is:")
print(dealer.hand[1])
print(" ")
print("Therefore the dealer has the following cards in their starting hand:")

for card in dealer.hand:
    print(card)

print("We are about to calculate the starting hand value of the dealer.")
print("As the dealer is automated, we have assumed that the value of an Ace for the dealer is 11.")

dealer.starting_hand_value()

if dealer.hand_value <= 16:
    print("The hand value of the dealer is less than or equal to 16 and so the dealer will need to take another card")
    print("The dealer will continue to take a card one by one until their hand value is greater than or equal to 17")
    
    while dealer.hand_value <= 16:
        dealer.hit(new_game_deck.all_cards.pop())
    
    print("The hand value of the dealer is now greater than or equal to 17.\n")

print("As the hand value of the dealer is greater than or equal to 17, we will now check if the dealer has Bust")

if dealer.hand_value > 21:
    print("The dealer has Bust")
    
    for player in game_players:
        player.money = 2 * player.bet
        print(f"{player.position}, your money won is {player.money}.\n")
        print(f"{player.name}, Player {player.position}, you are through for this round")
        win_players.append(game_players.pop(game_players.index(player)))
        
else:
    
    if dealer.hand_value == 21:
        
        for player in game_players:
            
            if player.hand_value != 21:
                print(f"{player.name}, Player {player.position}, you have lost this round")
                loss_players.append(game_players.pop(game_players.index(player)))
    
    else:
        
        for player in game_players:
            
            if dealer.hand_value < player.hand_value:
                player.money = 2 * player.bet
                print(f"{player.position}, your money won is {player.money}.\n")
                print(f"{player.name}, Player {player.position}, you are through for this round")
                win_players.append(game_players.pop(game_players.index(player)))
            
            else:
                print(f"{player.name}, Player {player.position}, you have lost this round")
                loss_players.append(game_players.pop(game_players.index(player)))