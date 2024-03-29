import random

card_suits = ("Hearts", "Diamonds", "Spades", "Clubs")
card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
               "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


#   Creating the cards with the written values (e.g., Hearts Two ) in "deck" list. Creating the values as int elements in "deck_values" list.
#   Later we create a dict from these two lists. (deck_w_values)
def create_deck():
    deck_values = []
    deck = []
    for suits in card_suits:
        for cardkey, cardvalue in card_values.items():
            deck_values.append(cardvalue)
            deck.append(suits+" "+cardkey)
    return (deck_values, deck)


def create_main_deck_in_dict():
    deck = create_deck()
    deck_w_values = {deck[1][i]: deck[0][i] for i in range(len(deck[1]))}
    return deck_w_values


# Picking a random card from the main deck (deck_w_values).
def random_card():
    return random.choice(list(deck_w_values.items()))


# Deleting the picked card from the main deck. We use this in the newcard function.
def del_from_maindeck(deck_w_values):
    key = cards_ingame[0][0]
    val = cards_ingame[0][1]
    if val in deck_w_values.values() and key in deck_w_values.keys():
        del deck_w_values[key]
    return deck_w_values


def newcard(whoshand):
    newcard = random_card()
    cards_ingame.insert(0, newcard)
    del_from_maindeck(deck_w_values)
    whoshand.insert(0, newcard) # Insert the randomly picked card to the players or dealer's hand.
     # Checking if there is an Ace in his hand. If yes, we examine the values of the cards and giving to the ace the more preferred value.
    value_of_ace(whoshand) 
    return newcard


# We will use this function to print the picked card with its value.
def what_is_the_newcard(whoshand):
    theNewcard = str(len(whoshand)) + \
        ". lapja:", whoshand[0][0], "Értéke:", whoshand[0][1]
    return theNewcard


def draw_by(who):
    newcard(who)
    if who == players_hand:
        print("A játékos", *what_is_the_newcard(players_hand))
    elif who == dealers_hand:
        if len(dealers_hand) != 2:
            print("A dealer", *what_is_the_newcard(dealers_hand))


# The total value of the cards held in the player's hand or dealer's hand.
def value_of_cards(whoseCards):
    total_value = []
    for i in range(len(whoseCards)):
        valueOfcard = (whoseCards[i][1])
        total_value.append(valueOfcard)
    return(sum(total_value))


def value_of_ace(whosecards):
    for i in range(len(whosecards)):
        if "Ace" in whosecards[i][0] and value_of_cards(whosecards) > 21:
            whosecards[i] = whosecards[i][0], 1
            return whosecards[i]


def result(PlayerTotal, DealerTotal):
    if DealerTotal <= 21 and DealerTotal > PlayerTotal:
        return "A dealer nyert! Lapjainak értéke összesen: " + str(DealerTotal)
    elif PlayerTotal <= 21 and PlayerTotal > DealerTotal:
        return "A játékos nyert! Lapjainak értéke összesen: " + str(PlayerTotal) + " A dealer lapjai összesen: " + str(DealerTotal)
    elif PlayerTotal <= 21 and PlayerTotal == DealerTotal:
        return "Döntetlen!"
    elif DealerTotal > 21 and PlayerTotal <= 21:
        return "A dealer lapjainak értéke több, mint 21! A játékos nyert!"
    elif PlayerTotal > 21 and DealerTotal <= 21:
        return "A játékos lapjainak értéke több, mint 21! A dealer nyert! A dealer lapjainak össz értéke: " + str(DealerTotal)


while True:
    deck_w_values = create_main_deck_in_dict()
    cards_ingame = []   # We use this list to delete these cards from the main deck, so we can't use a card twice.
    players_hand = []   # The cards in the player's hand.
    dealers_hand = []   # The cards in the dealer's hand.
    draw_by(players_hand)
    draw_by(dealers_hand)
    draw_by(players_hand)
    print("Játékos kártyáinak össz értéke:", value_of_cards(players_hand))
    draw_by(dealers_hand)

    decision = "y"
    while decision == "y" and value_of_cards(players_hand) < 21:
        hit = input("Kérsz még lapot? i/n ")
        if hit.lower() == "i":
            draw_by(players_hand)
            print("Lapjainak össz értéke:", value_of_cards(players_hand))
        elif hit != "i":
            print("A játékos megállt! Lapjainak értéke:",
                  value_of_cards(players_hand))
            decision = "n"

    if value_of_cards(players_hand) < 21:
        while value_of_cards(dealers_hand) < 17:
            draw_by(dealers_hand)
            print("Lapjainak értéke összesen: ",
                  value_of_cards(dealers_hand))

    print(result(value_of_cards(players_hand), value_of_cards(dealers_hand)))

    print("Jöjjön még egy kör! Nyomj meg egy gombot...")
    input()
