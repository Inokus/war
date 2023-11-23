import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    suits = ("♣", "♦", "♥", "♠")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(Card(suit, rank))

    # Might not need this
    @classmethod
    def get_deck(cls):
        return cls.deck1

    @classmethod
    def shuffle(cls):
        random.shuffle(cls.deck)

    @classmethod
    def split_in_half(cls):
        split_point = len(cls.deck) // 2
        half1 = cls.deck[:split_point]
        half2 = cls.deck[split_point:]
        return half1, half2


class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards


class Game:
    def __init__(self, player1, player2):
        self.card_values = {
            "2": 0,
            "3": 1,
            "4": 2,
            "5": 3,
            "6": 4,
            "7": 5,
            "8": 6,
            "9": 7,
            "10": 8,
            "J": 9,
            "Q": 10,
            "K": 11,
            "A": 12,
        }

        self.player1 = player1
        self.player2 = player2
        self.player1_card_count = len(self.player1.cards)
        self.player2_card_count = len(self.player2.cards)

    def compare_cards(self, card1, card2):
        # print(f"{card1} vs {card2}")

        if self.card_values[card1.rank] > self.card_values[card2.rank]:
            return 1
        elif self.card_values[card1.rank] < self.card_values[card2.rank]:
            return -1
        else:
            return 0

    # Should we shuffle cards? Whose cards goes first if not?
    def take_cards(self, winning_player, losing_player, index):
        winning_player.cards = (
            winning_player.cards[index + 1 :]
            + winning_player.cards[0 : index + 1]
            + losing_player.cards[0 : index + 1]
        )
        losing_player.cards = losing_player.cards[index + 1 :]


    def print_board(self, idx):
        print(f"{self.player1.name} | {self.player1_card_count} | ", end="")
        for i in range(idx + 1):
            if i % 2 == 0:
                print(f"{self.player1.cards[i]}", end="")
            else:
                print("##", end="")
        print(" vs ", end="")
        for i in range(idx, -1, -1):
            if i % 2 == 0:
                print(f"{self.player2.cards[i]}", end="")
            else:
                print("##", end="")
        print(f" | {self.player2_card_count} | {self.player2.name}")


    def play(self):
        mode = "step_by_step"

        while self.player1_card_count > 0 and self.player2_card_count > 0:
            current_index = 0
            if mode == "step_by_step":
                user_input = input()
                if user_input:
                    mode = "conitinous"
            while True:
                comparison_evaluation = self.compare_cards(
                    self.player1.cards[current_index], self.player2.cards[current_index]
                )
                self.print_board(current_index)
                # Add and subtract from player_card_counts
                if comparison_evaluation == 1:
                    self.take_cards(self.player1, self.player2, current_index)
                    self.player1_card_count += current_index + 1
                    self.player2_card_count -= current_index + 1
                    break
                elif comparison_evaluation == -1:
                    self.take_cards(self.player2, self.player1, current_index)
                    self.player2_card_count += current_index + 1
                    self.player1_card_count -= current_index + 1
                    break
                else:
                    # Need to check if both sides has enough cards left to go to war
                    current_index += 2
                    if self.player1_card_count < current_index + 1:
                        return f"{self.player2.name} wins!"
                    elif self.player2_card_count < current_index + 1:
                        return f"{self.player1.name} wins!"

        if self.player1_card_count == 0:
            return f"{self.player2.name} wins!"
        else:
            return f"{self.player1.name} wins!"


def get_names():
    player1_name = input("Enter player1 name: ")
    player2_name = input("Enter player2 name: ")
    if player1_name == "":
        player1_name = "Josh"
    if player2_name == "":
        player2_name = "Alice"
    return player1_name, player2_name


def main():
    player1_name, player2_name = get_names()

    # Initialize the deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Split shuffled deck in two and assign cards to both players
    half1, half2 = deck.split_in_half()
    player1 = Player(player1_name, half1)
    player2 = Player(player2_name, half2)

    game = Game(player1, player2)
    print(game.play())


if __name__ == "__main__":
    main()
