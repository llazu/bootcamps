import random

#logic to add
#player wager
#Shuffle a give a card to each player


deck = {
            "2hearts" : 2, 
            "3hearts" : 3, 
            "4hearts" : 4, 
            "5hearts" : 5, 
            "6hearts" : 6,
            "7hearts" : 7, 
            "8hearts" : 8, 
            "9hearts" : 9, 
            "10hearts" : 10, 
            "jackHearts" : 10, 
            "queenHearts" : 10, 
            "kingHearts" : 10,
            "aceHearts": 1
    }

class Dealer():

    def __init__(self, name, casino):
        self.name=name
        self.casino=casino
        self.card_1=None
        self.card_2=None
    
    def create_player(self, name):
        #players = [Player(i+1, None, None) for i in range(total_players)]
        player = Player(name, None, None)
        return player

    def deal_first_card(self, player):
        self.card_1 = random.choice(list(deck.keys()))
        #for player in players:
        player.card_1 = random.choice(list(deck.keys()))
        return player
    
    def deal_second_card(self, player):
        self.card_2 = random.choice(list(deck.keys()))
        #for player in players:
        player.card_2=random.choice(list(deck.keys()))
        return player
    
    def show_cards(self):
        return self.card_1

    def get_score(self):
        return deck[self.card_1] + deck[self.card_1]

class Player():
    max_card_index = 2
    def __init__(self, player_name, card_1, card_2):
        self.player_name = player_name
        self.card_1 = card_1
        self.card_2 = card_2

    def get_score(self):
        score = deck[self.card_1] + deck[self.card_2]
        return score
    
    def __str__(self):
        return f"Player {self.player_name}: {self.card_1}, {self.card_2}"

    def hit(self):
        new_card = random.choice(list(deck.keys()))
        setattr(self, f"card_{self.max_card_index}", new_card)
        self.max_card_index += 1
        return new_card
    
def main():
    #total_players = int(input("How many players?\n")) - 1
    
    name = input("What's your name? ")

    dealer = Dealer("The House", "MGM")

    # create players
    player = dealer.create_player(name)
    print(player)

    # Deal first round
    #dealer.deal_first_card()
    dealer.deal_first_card(player)

    # Deal second round
    #dealer.deal_second_card()
    dealer.deal_second_card(player)

    print("The house first card ", dealer.show_cards())

    print(f"{name}'s cards", player.card_1, player.card_2)

    print(f"{name}'s score", player.get_score())

    #print(f"{name} your score is {player.get_score()}. Would you like to h )
    
    hit_input = input("Would you like to hit? ")
    if hit_input == "yes":
        print(player.hit())

if __name__ == "__main__":
    main()