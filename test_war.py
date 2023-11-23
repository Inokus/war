from war import Card, Deck, Player, Game


def test_card_creation():
    card = Card("♣", "A")
    assert card.suit == "♣"
    assert card.rank == "A"
    assert str(card) == "A♣"


def test_deck_creation():
    deck = Deck()
    assert len(deck.deck) == 52
    assert type(deck.deck[0]) == Card


def test_deck_shuffle():
    deck = Deck()
    original_deck = deck.deck.copy()
    deck.shuffle()
    assert deck.deck != original_deck


def test_deck_split_in_half():
    deck = Deck()
    half1, half2 = deck.split_in_half()
    assert len(half1) == len(half2) == 26


def test_player_creation():
    cards = [Card("♣", "A"), Card("♦", "K")]
    player = Player("TestPlayer", cards)
    assert player.name == "TestPlayer"
    assert player.cards == cards


def test_game_compare_cards():
    game = Game(Player("TestPlayer1", []), Player("TestPlayer2", []))
    card1 = Card("♣", "A")
    card2 = Card("♦", "K")
    assert game.compare_cards(card1, card2) == 1

    card3 = Card("♠", "2")
    card4 = Card("♥", "Q")
    assert game.compare_cards(card3, card4) == -1

    card5 = Card("♣", "7")
    card6 = Card("♦", "7")
    assert game.compare_cards(card5, card6) == 0


def test_take_cards():
    cards1 = [Card("♣", "A"), Card("♦", "K"), Card("♠", "2")]
    cards2 = [Card("♦", "7"), Card("♥", "8"), Card("♣", "J")]
    player1 = Player("TestPlayer1", cards1)
    player2 = Player("TestPlayer2", cards2)
    game = Game(player1, player2)

    game.take_cards(player1, player2, 2)
    assert len(player1.cards) == 6
    assert len(player2.cards) == 0

    game.take_cards(player2, player1, 0)
    assert len(player1.cards) == 5
    assert len(player2.cards) == 1
