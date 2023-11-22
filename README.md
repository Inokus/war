# war

Card game War is played by two players using a standard 52-card deck. The objective of the game is to collect all the cards.

Card ranks from lowest to highest: "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A".

1. Initialize a deck of 52 cards and shuffle it
2. Divide a deck into two equal piles
3. Implement this game loop:
   - first card from both piles gets revealed
   - both cards are compared
   - if ranks are not equal:
     - Side that had higher rank card adds both cards to the bottom their pile
   - if ranks are equal:
     - It's considered a war. Players place the next card from their pile face down and then another card face-up, the owner
       of the higher face-up card wins the war and adds all the cards used in the round to the bottom of their pile. If there's
       another tie the process is repeated until someone wins
4. A player loses when they have no cards remaining or when they go to war without having enough cards for "reinforcements"

At the start of the game user should be prompted to enter player names, if names are not entered they should be set to preset
values. At the beginning program should inform user about possible input options. Program should show player names and number
of cards held by each player. When user presses "enter" key for the first time (inputs empty string) cards are revealed, after
pressing "enter" again those cards gets added to the winners pile and new cards are revealed. If war occurs we should show user
all cards that has been revealed and face down cards as "#" between them. Since game is quite long there should be an option to
fast-forward to the end by entering some specific input.
