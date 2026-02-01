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
        self.first_card=None
        self.second_card=None
    
    def create_players(self, total_players):
        players = [Player(i+1, None, None) for i in range(total_players)]
        return players

    def deal_first_card(self, players):
        self.first_card = random.choice(list(deck.keys()))
        for player in players:
            player.first_card = random.choice(list(deck.keys()))
        return players
    
    def deal_second_card(self, players):
        self.second_card = random.choice(list(deck.keys()))
        for player in players:
            player.second_card=random.choice(list(deck.keys()))
        return players

    def get_score(self):
        return deck[self.first_card] + deck[self.second_card]

class Player():
    def __init__(self, player_number, first_card, second_card):
        self.player_number = player_number
        self.first_card = first_card
        self.second_card = second_card

    def get_score(self):
        score = deck[self.first_card] + deck[self.second_card]
        return score
    
    def __str__(self):
        return f"Player {self.player_number}: {self.first_card}, {self.second_card}"

    def hit():
        pass

    def passing(self):
        pass

def main():
    total_players = int(input("How many players?\n")) - 1
    
    dealer = Dealer("The House", "MGM")

    # create players
    players = dealer.create_players(2)

    # Deal first round
    dealer.deal_first_card(players)

    # Deal second round
    dealer.deal_second_card(players)

    for player in players:
        print(player)

    print("Player 1 score:", players[0].get_score())
    print("Player 2 score:", players[1].get_score())  
    
if __name__ == "__main__":
    main()