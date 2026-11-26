import decimal
import random

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
            "aceHearts": (1,11)
    }

class Dealer:
    def __init__(self, name, casino):
        self.name = name
        self.casino = casino
        self.cards = []
    
    def create_player(self, name):
        return Player(name)

    def deal_card(self, player):
        # 'self' is the sticky note for the Dealer. 'player' is the sticky note for the Player.
        # Both objects have their own .cards list, so we can interact with them identically!
        self.cards.append(random.choice(list(deck.keys())))
        
        # Encapsulation: We ask the player to receive the card rather than modifying their list directly.
        player.receive_card(random.choice(list(deck.keys())))
    
    def show_first_card(self):
        if self.cards:
            return self.cards[0]
        return None

    def get_score(self):
        score = 0
        aces = 0
        for card in self.cards:
            val = deck[card]
            if isinstance(val, tuple):
                score += 11
                aces += 1
            else:
                score += val
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score


class Player:
    # We use 'name' instead of 'player_name' to avoid redundant "stuttering" (e.g. player.name)
    def __init__(self, name):
        self.name = name
        self.cards = []

    # The object manages its own state
    def receive_card(self, card):
        self.cards.append(card)

    def get_score(self):
        score = 0
        aces = 0
        for card in self.cards:
            val = deck[card]
            if isinstance(val, tuple):
                score += 11
                aces += 1
            else:
                score += val
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score
    
    def __str__(self):
        return f"Player {self.name}: {', '.join(self.cards)}"

    def hit(self):
        new_card = random.choice(list(deck.keys()))
        self.receive_card(new_card)
        return new_card
    
    def stay(self):
        pass

def main():
    name = input("What's your name? ")

    dealer = Dealer("The House", "MGM")

    # Create player
    player = dealer.create_player(name)
    print(f"Welcome, {player.name}!")

    # Deal first round
    dealer.deal_card(player)

    # Deal second round
    dealer.deal_card(player)

    print("The house first card is:", dealer.show_first_card())

    print(f"{name}'s cards:", ", ".join(player.cards))
    print(f"{name}'s score:", player.get_score())
    
    # Player's turn
    while True:
        if player.get_score() > 21:
            print(f"\n{name} busted with a score of {player.get_score()}!")
            break
        elif player.get_score() == 21:
            print(f"\n{name} got 21!")
            break

        hit_input = input("Would you like to hit? (y/n): ")
        if hit_input.lower().strip() in ["yes", "y"]:
            new_card = player.hit()
            print(f"You drew a {new_card}!")
            print(f"{name}'s new cards:", ", ".join(player.cards))
            print(f"{name}'s new score:", player.get_score())
        else:
            break

    player_score = player.get_score()

    # Dealer's turn (only if player didn't bust)
    if player_score <= 21:
        print(f"\n{dealer.name}'s cards: {', '.join(dealer.cards)}")
        print(f"{dealer.name}'s score: {dealer.get_score()}")

        while dealer.get_score() < 17:
            new_card = random.choice(list(deck.keys()))
            dealer.cards.append(new_card)
            print(f"{dealer.name} drew a {new_card}!")
            print(f"{dealer.name}'s new score: {dealer.get_score()}")

    dealer_score = dealer.get_score()

    # Determine winner
    print("\n--- Final Results ---")
    print(f"{player.name}: {player_score}")
    print(f"{dealer.name}: {dealer_score}")

    if player_score > 21:
        print(f"The house {dealer.name} has Won!")
    elif dealer_score > 21:
        print(f"The house busted! The player {player.name} has Won!")
    elif player_score > dealer_score:
        print(f"The player {player.name} has Won!")
    elif dealer_score > player_score:
        print(f"The house {dealer.name} has Won!")
    else:
        print("It's a tie!")
    


if __name__ == "__main__":
    main()
