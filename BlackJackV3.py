import random

card_suits = ("Hearts ", "Diamonds ", "Spades ", "Clubs ")
card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
               "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


def del_from_list():
    key = cards_ingame[0][0]
    val = cards_ingame[0][1]
    if val in deck_w_values.values() and key in deck_w_values.keys():
        del deck_w_values[key]


def in_players_hands():
    in_handANDcards_in(players_hand, player_cards_sum)
    del_from_list()
    print("A játékos", str(len(players_hand))+". lapja:",
          players_hand[0][0], "Értéke:", players_hand[0][1])
    sumP()


def in_dealers_hands():
    in_handANDcards_in(dealers_hand, dealer_cards_sum)
    del_from_list()
    if len(dealers_hand) != 2:
        print("A dealer", str(len(dealers_hand))+". lapja:",
              dealers_hand[0][0], "Értéke:", dealers_hand[0][1])
    sumD()


def create_deck():
    for suits in card_suits:
        for cardkey, cardvalue in card_values.items():
            deck_values.append(cardvalue)
            deck.append(suits+cardkey)


def in_handANDcards_in(whoshand, holding):
    newcard = random.choice(list(deck_w_values.items()))
    if len(whoshand) > 0 and (newcard[1] == 11 and holding > 10):
        newcard = newcard[0], 1
    whoshand.insert(0, newcard)
    cards_ingame.insert(0, newcard)


def sumP():
    global player_cards_sum
    player_cards_sum += players_hand[0][1]


def sumD():
    global dealer_cards_sum
    dealer_cards_sum += dealers_hand[0][1]


while True:
    deck = []
    deck_values = []
    cards_ingame = []
    players_hand = []
    dealers_hand = []
    player_cards_sum = 0
    dealer_cards_sum = 0

    create_deck()
    deck_w_values = {deck[i]: deck_values[i] for i in range(len(deck))}
    in_players_hands()
    in_dealers_hands()
    in_players_hands()
    print("Játékos kártyáinak össz értéke:", player_cards_sum)
    in_dealers_hands()

    decision = "x"
    while decision == "x" and player_cards_sum < 21:
        hit = input("Kérsz még lapot? i/n ")
        if hit.lower() == "i":
            in_players_hands()

            print("Lapjainak össz értéke:", player_cards_sum)
        elif hit != "i":
            print("A játékos megállt! Lapjainak értéke:", player_cards_sum)
            decision = "n"

    if player_cards_sum < 21:
        while dealer_cards_sum < 17:
            in_dealers_hands()
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
