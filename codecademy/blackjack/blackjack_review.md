# Code Review & Refactoring Log: blackjack.py

## 1. Antipattern Removed: Dynamic Variable Creation (setattr)
**What was changed:** 
Removed `card_1`, `card_2`, and the `setattr` logic inside the `Player` and `Dealer` classes. Replaced them with a single `self.cards = []` list.

**Why (The Antipattern):** 
Using `setattr` to dynamically create `self.card_3`, `self.card_4`, etc., when a player hits is an antipattern because:
1. **It breaks predictability:** An object should have a predictable structure. Code interacting with a `Player` shouldn't have to guess if `card_5` exists.
2. **It makes loops and math difficult:** The `get_score()` method had no easy way to know how many cards existed to add them up. It was hardcoded to only add `card_1` and `card_2`, ignoring any cards drawn during a "hit".
3. **Reinventing the wheel:** Python lists are specifically designed to hold a growing sequence of items. By using a list and `.append()`, scoring becomes a simple loop.

## 2. Refactored Score Calculation
**What was changed:** 
Both `Dealer.get_score()` and `Player.get_score()` were updated to use `sum(deck[card] for card in self.cards)`.

**Why:** 
*   **Dealer Bug Fix:** The original dealer score had a bug where it added `card_1` to itself (`deck[self.card_1] + deck[self.card_1]`).
*   **Player Bug Fix:** The original player score only added the first two cards, even if the player hit. The new approach accurately sums all cards currently in the `self.cards` list, regardless of how many times the player hits.

## 3. Improved Initialization
**What was changed:** 
Removed `card_1` and `card_2` from the `__init__` parameters of `Player`.

**Why:** 
When a player sits at the table, they don't have cards yet. It makes more sense logically to initialize a player with an empty hand (`self.cards = []`) and then deal cards to them afterward, rather than requiring the dealer to pass `None` into the constructor.

## 4. Class Syntax and Input Validation
**What was changed:** 
*   Changed `class Player():` to `class Player:`.
*   Changed `if hit_input == "yes":` to `if hit_input.lower().strip() in ["yes", "y"]:`.

**Why:** 
*   In Python 3, parentheses are only needed if a class is inheriting from another class.
*   The original input check would fail if the user typed "Yes", " YES ", or "y". Normalizing the input makes the CLI much more user-friendly.

## 5. Better Formatting for Display
**What was changed:** 
Updated `__str__` in Player and print statements in `main()` to use `", ".join(self.cards)`.

**Why:** 
Printing a list of cards dynamically is much cleaner with string joining, ensuring it formats correctly whether the player has 2 cards or 5 cards.

---

## Future Improvements (Pending)
*   **Without Replacement:** The current code still draws cards *with replacement* (`random.choice(list(deck.keys()))`). In a real game, cards should be popped from the deck so the same card (e.g., "2hearts") isn't drawn twice.
*   **Game Rules:** The game still needs logic to handle busting (going over 21), aces being worth 11, and determining a winner by comparing the player's final score to the dealer's final score.