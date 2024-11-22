import random

#logic to add
#player wager
#Shuffle a give a card to each player

class Dealer():
    #deck = ["2hearts", "3hearts", "4hearts", "5hearts", "6hearts",
        #"7hearts", "8hearts", "9hearts", "10hearts", "jackHearts", "queenHearts", "kingHearts", 
        #"aceHearts"]
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
    total_players = int(input("How many players?\n")) - 1
    def __init__(self, name, casino):
        self.name=name
        self.casino=casino
        self.first_card=None
        self.second_card=None

    def first_deal(self, total_players):
        global players
        self.first_card = random.choice(list(Dealer.deck.keys()))
        print(self.first_card)
        players = [Player(i+1, random.choice(list(Dealer.deck.keys())), None) for i in range(total_players)]
        return players
    
    def second_deal(self):
        self.second_card = random.choice(list(Dealer.deck.keys()))
        for player in players:
            player.second_card=random.choice(list(Dealer.deck.keys()))
        return players

    def get_score(self):
        return Dealer.deck[self.first_card] + Dealer.deck[self.second_card]

class Player(Dealer):
    def __init__(self, player_number, first_card, second_card):
        self.player_number = player_number
        self.first_card = first_card
        self.second_card = second_card

    def get_score(self):
        return Dealer.deck[players[0].first_card] + Dealer.deck[players[1].second_card]
    
    def hit():
        pass

    def passing(self):
        pass

def main():
    the_house = Dealer("The House", "MGM", )

    print("First deal")
    print("player_1 first card: ", the_house.first_deal(2)[0].first_card) #second_card = the_house.second_card()
    print("player_2 first card: ", the_house.first_deal(2)[1].first_card)
    print("Dealers first card: ", the_house.first_card)

    print("Second deal")
    print("player_1 first card: ", the_house.second_deal()[0].second_card) 
    print("player_2 first card: ", the_house.second_deal()[1].second_card)
    print("The dealer's second card:", the_house.second_card)
    
    print("Player's 1 score", players[0].get_score())
    print("Player's 2 score", players[1].get_score())
    print("Dealer's score: ", the_house.get_score())


def test1():
    deck1 = {
            "2hearts" : 2, 
            "3hearts" : 3, 
            "4hearts" :4, 
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
    print(list(deck1.keys()))
    print(random.choice(list(deck1.keys())))
    
if __name__ == "__main__":
    main()