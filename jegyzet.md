## Black Jack jegyzet

**~~Az ászok értéke még nincs lekezelve, így alapértelmezetten 11 az értéke.~~ /Az ászok értéke lekezelve./ **

Szükségünk van a francia kártya paklira, ami 52 lapból áll. (Jokerek nélkül.)

A kártykáknak vannak színei (card_suits) és értékei (card_values). Ezeket egy tuple-be és egy dictionary-be töltöttem fel.

Létrehoztam egy paklit (deck) és egy pakli értékei listát (deck_values), ezek még üres listák.

A pakli értékei (deck_values) listához hozzáadtam for ciklus segítségével mind az 52db kártya értékét. (Pl.: 3)

A pakli (deck) listához pedig ugyanabban a for ciklusban hozzáadtam az 52db kártyát színnel és névvel. (Pl.: 'Hearts Two')

Létrehoztam egy új szótárat **(deck_w_values)**, amiben a pakliban lévő kártyák mellé társítottam az értékeket. (Pl.: 'Spades Five': 5)

A játék során ebből a szótárból játszunk ("fő pakli").

Létrehoztam egy függvényt (del_from_list()), ami miután a játékos vagy a dealer lapot kapott/húzott, az adott kártya törlődik a fő pakliból, így az nem kerülhet mégegyszer játékba.

Ennek a működéséhez létrehoztam még egy listát, ami a játékban lévő kártyákat tartalmazza, alapértelmezetten üres és minden osztás/húzás után hozzáadódik a kártya a lista elejére. 

A *del_from_list()* függvény ennek a listának a segítségével hasonlítja össze a kártyákat a fő pakli (deck_w_values) tartalmával.

A játék első lépéseként a játékos kap egy random lapot a fő pakliból. Ez a kártya kiírásra kerül az értékével együtt, bekerül a játékban lévő kártyák listájába és törlődik a fő pakliból.

Ezután a dealer kap egy random lapot és ugyanaz történik, mint a játékos első lapjánál.

A játékos megkapja a második lapját, hasonlóan az elsőhöz. Annyi különbséggel, hogy itt már létrejön egy változó, ami tárolja a játékos kártyáinak össz értékét.

A dealer megkapja a második lapját, ez már nem kerül kiírásra.

Ezután a játékos dönthet, hogy húz még lapot vagy sem. Ez egy ciklusban van elhelyezve, ahol addig kérhet lapot, amíg nem lépi túl a 21-et. Amennyiben lapot kér, a már ismert folyamat történik, ha megáll a játékos, akkor a dealer következik.

A dealer csak akkor következik, ha előtte a játékos nem érte el a lapjaival a 21-et.

A dealer húzása is egy ciklusban van, ahol addig kell húznia, amíg lapjainak értéke 17 alatti.

Ezután feltételes utasításokkal eldől, hogy ki nyert. Itt összehasonlításra kerül a játékos és dealer lapjainak értéke.
