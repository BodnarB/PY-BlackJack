import random

card_suits = ("Hearts ", "Diamonds ", "Spades ", "Clubs ")
card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
               "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

while True:
    deck = []
    deck_values = []
    cards_ingame = []

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

    players_first_card = random.choice(list(deck_w_values.items()))
    print("A játékos első lapja:",
          players_first_card[0], "Értéke: ", players_first_card[1])
    cards_ingame.insert(0, players_first_card)
    del_from_list()

    dealer_card = random.choice(list(deck_w_values.items()))
    print("A dealer első lapja: ", dealer_card[0], "Értéke:", dealer_card[1])
    cards_ingame.insert(0, dealer_card)
    del_from_list()

    players_second_card = random.choice(list(deck_w_values.items()))
    print("A játékos második lapja: ",
          players_second_card[0], "Értéke:", players_second_card[1])
    player_cards_sum = players_first_card[1]+players_second_card[1]
    print("A játékos lapjainak összege: ", player_cards_sum)
    cards_ingame.insert(0, players_second_card)
    del_from_list()

    dealer_second_card = random.choice(list(deck_w_values.items()))
    dealer_cards_sum = dealer_card[1]+dealer_second_card[1]
    cards_ingame.insert(0, dealer_second_card)
    del_from_list()

    decision = "x"
    while decision == "x" and player_cards_sum < 21:
        hit = input("Kérsz még lapot? i/n ")
        if hit == "i":
            player_plus_card = random.choice(list(deck_w_values.items()))
            cards_ingame.insert(0, player_plus_card)
            del_from_list()
            print("A játékos lapot húzott!",
                  player_plus_card[0], "Értéke: ", player_plus_card[1])
            player_cards_sum += +player_plus_card[1]
            print("A játékos lapjainak értéke összesen: ",
                  player_cards_sum)
        elif hit != "i":
            print("A játékos megállt! Lapjainak értéke:", player_cards_sum)
            decision = "n"

    if player_cards_sum < 21:
        while dealer_cards_sum < 17:
            dealer_plus_card = random.choice(list(deck_w_values.items()))
            cards_ingame.insert(0, dealer_plus_card)
            del_from_list()
            dealer_cards_sum += dealer_plus_card[1]
            print("A dealer lapot húzott! Lapjainak értéke összesen: ",
                  dealer_cards_sum)

    if (dealer_cards_sum <= 21) and (dealer_cards_sum > player_cards_sum):
        print("A dealer nyert! Lapjainak értéke összesen: ", dealer_cards_sum)
    elif (player_cards_sum <= 21) and (player_cards_sum > dealer_cards_sum):
        print("A játékos nyert!")
    elif (player_cards_sum <= 21) and (player_cards_sum == dealer_cards_sum):
        print("Döntetlen!")
    elif (dealer_cards_sum > 21) and (player_cards_sum <= 21):
        print("A dealer lapjainak értéke több, mint 21! A játékos nyert!")
    elif (player_cards_sum > 21) and (dealer_cards_sum <= 21):
        print("A játékos lapjainak értéke több, mint 21! A dealer nyert!")

    print("Jöjjön még egy kör! Nyomj meg egy gombot...")
    input()
