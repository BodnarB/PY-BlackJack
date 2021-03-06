import random

card_suits = ("Hearts", "Diamonds", "Spades", "Clubs")
card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
               "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


while True:
    cards_ingame = []  # We use this list to delete these cards from the main deck, so we can't use a card twice.
    players_hand = []  # The cards in the player's hand.
    dealers_hand = []  # The cards in the dealer's hand.

    #   Creating the cards with the written values (e.g., Hearts Two ) in "deck" list. Creating the values as int elements in "deck_values" list.
    #   Later we create a dict from these two lists. (deck_w_values)
    def create_deck(card_suits, card_values):
        deck_values = []
        deck = []
        for suits in card_suits:
            for cardkey, cardvalue in card_values.items():
                deck_values.append(cardvalue)
                deck.append(suits+" "+cardkey)
        return (deck_values, deck)

    deck_w_values = {create_deck(card_suits, card_values)[1][i]:
                     create_deck(card_suits, card_values)[0][i] for i in range(len(create_deck(card_suits, card_values)[1]))}


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
        # Insert the randomly picked card to the players or dealer's hand.
        whoshand.insert(0, newcard)
        # Checking if there is an Ace in his hand. If yes, we examine the values of the cards and giving to the ace the more preferred value.
        valueOfAce(whoshand)
        return newcard


    # We will use this function to print the picked card with its value.
    def whatIsTheNewcard(whoshand):
        theNewcard = str(len(whoshand)) + \
            ". lapja:", whoshand[0][0], "??rt??ke:", whoshand[0][1]
        return theNewcard


    def draw_by(who):
        newcard(who)
        if who == players_hand:
            print("A j??t??kos", *whatIsTheNewcard(players_hand))
        elif who == dealers_hand:
            if len(dealers_hand) != 2:
                print("A dealer", *whatIsTheNewcard(dealers_hand))


    # The total value of the cards held in the player's hand or dealer's hand.
    def valueOfCards(whoseCards):
        totalValue = []
        for i in range(len(whoseCards)):
            valueOfcard = (whoseCards[i][1])
            totalValue.append(valueOfcard)
        return(sum(totalValue))


    def valueOfAce(whosecards):
        for i in range(len(whosecards)):
            if "Ace" in whosecards[i][0] and valueOfCards(whosecards) > 21:
                whosecards[i] = whosecards[i][0], 1
                return whosecards[i]


    draw_by(players_hand)
    draw_by(dealers_hand)
    draw_by(players_hand)
    print("J??t??kos k??rty??inak ??ssz ??rt??ke:", valueOfCards(players_hand))
    draw_by(dealers_hand)

    decision = "y"
    while decision == "y" and valueOfCards(players_hand) < 21:
        hit = input("K??rsz m??g lapot? i/n ")
        if hit.lower() == "i":
            draw_by(players_hand)
            print("Lapjainak ??ssz ??rt??ke:", valueOfCards(players_hand))
        elif hit != "i":
            print("A j??t??kos meg??llt! Lapjainak ??rt??ke:",
                  valueOfCards(players_hand))
            decision = "n"

    if valueOfCards(players_hand) < 21:
        while valueOfCards(dealers_hand) < 17:
            draw_by(dealers_hand)
            print("Lapjainak ??rt??ke ??sszesen: ",
                  valueOfCards(dealers_hand))

    def result(PlayerTotal, DealerTotal):
        if DealerTotal <= 21 and DealerTotal > PlayerTotal:
            return "A dealer nyert! Lapjainak ??rt??ke ??sszesen: " + str(DealerTotal)
        elif PlayerTotal <= 21 and PlayerTotal > DealerTotal:
            return "A j??t??kos nyert! Lapjainak ??rt??ke ??sszesen: " + str(PlayerTotal) + " A dealer lapjai ??sszesen: " + str(DealerTotal)
        elif PlayerTotal <= 21 and PlayerTotal == DealerTotal:
            return "D??ntetlen!"
        elif DealerTotal > 21 and PlayerTotal <= 21:
            return "A dealer lapjainak ??rt??ke t??bb, mint 21! A j??t??kos nyert!"
        elif PlayerTotal > 21 and DealerTotal <= 21:
            return "A j??t??kos lapjainak ??rt??ke t??bb, mint 21! A dealer nyert! A dealer lapjainak ??ssz ??rt??ke: " + str(DealerTotal)

    print(result(valueOfCards(players_hand), valueOfCards(dealers_hand)))

    print("J??jj??n m??g egy k??r! Nyomj meg egy gombot...")
    input()
