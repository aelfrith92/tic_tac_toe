import random


class Player:
    """
    This class returns player objects.
    It stores data like type of player (PC vs H),
    list of moves, symbol preference, print of
    the turn just played.
    """
    def __init__(self, whois, ptype, moves):
        self.whois = whois
        self.ptype = ptype
        self.moves = moves
        self.preference = ''

    def print_grid(self):
        """
        Function to print Tic Tac Toe
        """

        print("\n")
        print("\t     |     |")
        print(f"\t  {self.moves[0]}  |  {self.moves[1]}  | ",
              f"{self.moves[2]}")
        print('\t_____|_____|_____')

        print("\t     |     |")
        print(f"\t  {self.moves[3]}  |  {self.moves[4]}  | ",
              f"{self.moves[5]}")
        print('\t_____|_____|_____')

        print("\t     |     |")

        print(f"\t  {self.moves[6]}  |  {self.moves[7]}  | ",
              f"{self.moves[8]}")
        print("\t     |     |")
        print("\n")

    def return_choice(self, s_choice):
        """
        This function returns the player's choice
        """
        if s_choice == 1:
            return 'X'
        elif s_choice == 2:
            return 'O'
        else:
            return '★'

    def validation(self):
        """
        It validates the input. The func returns a list which allows
        symbol_func both to break the validation loop and store the
        correct input for the player.
        """
        print("Enter '1' to play with X\n")
        print("Enter '2' to play with O\n")
        print("Enter '3' to play with ★\n")
        symbol = input("Pick the symbol that you want to play with:\n")
        try:
            symbol = int(symbol)
            if symbol < 1 or symbol > 3:
                print('\nYou can choose options listed above only')
                raise ValueError('Input out of range')
        except ValueError:
            print('Try again. Choose 1, 2, or 3\n')
            return [False, None]
        return [True, symbol]

    def symbol_func(self):
        """
        It assigns a symbol to the dictionary 'preferences'
        """

        if self.whois == 'P1':
            while True:
                # The following variable receives a list from
                # func validation() above.
                symbol_list = self.validation()
                if symbol_list[0]:
                    symbol = symbol_list[1]
                    break
            return self.return_choice(symbol)
        else:
            # At this point, the code should check whether player 2 is
            if self.ptype == 'P':
                return random.choice(['X', '★', 'O'])
            else:
                while True:
                    # The following variable receives a list from
                    # func validation() above.
                    symbol_list = self.validation()
                    if symbol_list[0]:
                        symbol = symbol_list[1]
                        break
                return self.return_choice(symbol)

    def symbol_pref(self):
        """
        This function determines symbol preferences before starting
        the game.
        """
        # The loop checks whether the dictionary values are set
        while self.preference == '':
            self.preference = self.symbol_func()


def main():
    """
    Core function of the game
    """
    print("\nWelcome to Tic Tac Toe. Enter the grid numbers",
          "to play your move.\n")

    # Player types can be H - human, G - grid, P - PC
    # The grid player is a special player, as the instance
    # just needs the shared methods to - for example - print
    # up-to-date grids
    grid = Player('Grid', 'G', [])
    # The following variable keeps track of cells already played
    grid.moves = [(i+1) for i in range(9)]
    grid.print_grid()
    grid.moves = [' ' for i in range(9)]

    # player1 instance
    player1 = Player('P1', 'H', [])
    # player2 instance
    player2 = Player('P2', 'P', [])

    player1.symbol_pref()
    player2.symbol_pref()
    while player2.preference == player1.preference:
        print('\nYou cannot choose the same symbol. Pick',
              'a different option. Player1\' choice is:\n',
              f'{player1.preference}')
        player2.preference = ''
        player2.symbol_pref()

    print(f'Player1 preference is {player1.preference}')
    print(f'Player2 preference is {player2.preference}')


main()
