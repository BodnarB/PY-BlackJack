import random

card_suits = ("Hearts ", "Diamonds ", "Spades ", "Clubs ")
card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
               "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

while True:
    deck = []
    deck_values = []
    cards_ingame = []
    players_hand = []
    dealers_hand = []

    for suits in card_suits:
        for cardkey, cardvalue in card_values.items():
            deck_values.append(cardvalue)
            deck.append(suits+cardkey)

    deck_w_values = {deck[i]: deck_values[i] for i in range(len(deck))}

    def del_from_list():
        key = cards_ingame[0][0]
        val = cards_ingame[0][1]
        if val in deck_w_values.values() and key in deck_w_values.keys():
            del deck_w_values[key]

    def in_players_hands():
        players_hand.insert(0, random.choice(list(deck_w_values.items())))
        cards_ingame.insert(0, players_hand[0])
        del_from_list()
        print("A játékos", str(len(players_hand))+". lapja:",
              players_hand[0][0], "Értéke:", players_hand[0][1])

    def in_dealers_hands():
        dealers_hand.insert(0, random.choice(list(deck_w_values.items())))
        cards_ingame.insert(0, dealers_hand[0])
        del_from_list()
        if len(dealers_hand) != 2:
            print("A dealer", str(len(dealers_hand))+". lapja:",
                  dealers_hand[0][0], "Értéke:", dealers_hand[0][1])

    in_players_hands()

    in_dealers_hands()

    in_players_hands()

    player_cards_sum = players_hand[0][1]+players_hand[1][1]
    print("Játékos kártyáinak össz értéke:", player_cards_sum)

    in_dealers_hands()
    dealer_cards_sum = dealers_hand[0][1]+dealers_hand[1][1]

    decision = "x"
    while decision == "x" and player_cards_sum < 21:
        hit = input("Kérsz még lapot? i/n ")
        if hit.lower() == "i":
            in_players_hands()
            player_cards_sum += players_hand[0][1]
            print("Lapjainak össz értéke:", player_cards_sum)
        elif hit != "i":
            print("A játékos megállt! Lapjainak értéke:", player_cards_sum)
            decision = "n"

    if player_cards_sum < 21:
        while dealer_cards_sum < 17:
            in_dealers_hands()
            dealer_cards_sum += dealers_hand[0][1]
            print("Lapjainak értéke összesen: ",
                  dealer_cards_sum)

    if (dealer_cards_sum <= 21) and (dealer_cards_sum > player_cards_sum):
        print("A dealer nyert! Lapjainak értéke összesen: ", dealer_cards_sum)
    elif (player_cards_sum <= 21) and (player_cards_sum > dealer_cards_sum):
        print("A játékos nyert! A dealer lapjainak össz értéke:", dealer_cards_sum)
    elif (player_cards_sum <= 21) and (player_cards_sum == dealer_cards_sum):
        print("Döntetlen!")
    elif (dealer_cards_sum > 21) and (player_cards_sum <= 21):
        print("A dealer lapjainak értéke több, mint 21! A játékos nyert!")
    elif (player_cards_sum > 21) and (dealer_cards_sum <= 21):
        print("A játékos lapjainak értéke több, mint 21! A dealer nyert! A dealer lapjainak össz értéke:", dealer_cards_sum)

    print("Jöjjön még egy kör! Nyomj meg egy gombot...")
    input()
