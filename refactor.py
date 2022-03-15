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
        print("\nEnter '1' to play with X\n")
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
        It returns the symbol chosen and assigns it to the objects
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
            # PC or Human
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
        # The loop checks whether the self.preference is set
        while self.preference == '':
            self.preference = self.symbol_func()

    def pc_move(self):
        """
        This function determines the pc move by checking
        already-filled cells in the object grid.moves
        """
        random_index = random.randint(0, 8)
        while self.moves[random_index] != ' ':
            random_index = random.randint(0, 8)
        return random_index

    def validate_play(self):
        """
        This function validates the input once started playing
        """
        chosen_cell = input('Enter the cell number to play your turn\n')
        try:
            chosen_cell = int(chosen_cell)
            if chosen_cell < 1 or chosen_cell > 9 or \
               self.moves[chosen_cell - 1] != ' ':
                print('\nInvalid input. Choose an empty cell, by',
                      'entering a number between 1 and 9')
                raise ValueError('Input out of available range')
        except ValueError:
            print('Try again. Choose an empty cell\n')
            return [False, '']
        return [True, chosen_cell]

    def play(self):
        """
        This function lets players play their turn. First
        action is inputting the cell number. Validation straight after
        """
        # The following loop is for an actual player, not PC
        while True:
            valid = self.validate_play()
            if valid[0]:
                valid_choice = valid[1]
                break
        return valid_choice

    def check_win(self):
        """
        This function checks whether the calling object
        has won
        """
        winning_combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                                (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

        for i in winning_combinations:
            check_list = [True if self.moves[x] in i else False
                          for x in range(len(self.moves))]
            print(f'Tuple checked: {i}\n{self.whois} checklist is:',
                  f'{check_list}')
            if check_list.count(True) == 3:
                return True
            else:
                continue
        return False


def ptype_v():
    """
    This function defines and validates the game mode input.
    It returns the player type (ptype) for the object player2
    """
    while True:
        try:
            print('\nGAME MODE\n')
            mode = int(input("\nEnter '1' for 1vPC and '2' for 1v1\n"))
            if mode < 1 or mode > 2:
                print('\nInvalid input. Choose a valid mode, by',
                      'entering 1 or 2')
                raise ValueError('Input out of available range')
            else:
                break
        except ValueError:
            print('Try again. Choose 1 or 2\n')
    return 'P' if mode == 1 else 'H'


def main():
    """
    Core function of the game
    """
    # --------- INTRODUCTORY PART OF THE MAIN CODE ---------
    print("\nWelcome to Tic Tac Toe. Enter the grid numbers",
          "to play your move.\n")

    # Player types can be H - human, G - grid, P - PC
    # The grid player is a special player, as this instance
    # shares a few methods and characteristics
    grid = Player('Grid', 'G', [])
    # The following variable keeps track of cells already played
    grid.moves = [(i+1) for i in range(9)]
    grid.print_grid()
    grid.moves = [' ' for i in range(9)]

    # player2 instance
    player2 = Player('P2', ptype_v(), [])
    # player1 instance
    player1 = Player('P1', 'H', [])

    print('PLAYER 1\n')
    player1.symbol_pref()
    print('PLAYER 2\n')
    player2.symbol_pref()
    while player2.preference == player1.preference:
        if player2.ptype == 'H':
            print('\nYou cannot choose the same symbol. Pick',
                  'a different option. Player1\'s choice is:\n',
                  f'{player1.preference}')
        player2.preference = ''
        player2.symbol_pref()

    print(f'\nPlayer1 preference is {player1.preference}')
    print(f'Player2 preference is {player2.preference}')

    # ---------------- ACTUAL GAME LOOP ----------------
    grid.print_grid()
    # The following loop runs 9 times, which is the number of cells
    # that can be filled.
    for i in range(9):
        # Each time, player1 and player 2 lists store each
        # player's moves.
        if (i + 1) % 2 == 0:
            print('\nPLAYER 2 TURN')
            # If the player2 nature is PC, it randomly fills cells
            if player2.ptype == 'P':
                pc_index = grid.pc_move()
                grid.moves[pc_index] = player2.preference
                player2.moves.append(pc_index + 1)
            else:
                played_cell = grid.play()
                grid.moves[played_cell - 1] = player2.preference
                player2.moves.append(played_cell)
            player2.moves.sort()
            if i > 4:
                check = player2.check_win()
                if check:
                    print("The winner is Player2")
                    grid.print_grid()
                    break
        else:
            print('\nPLAYER 1 TURN')
            played_cell = grid.play()
            grid.moves[played_cell - 1] = player1.preference
            player1.moves.append(played_cell)
            player1.moves.sort()
            if i > 4:
                check = player1.check_win()
                if check:
                    print("The winner is Player1")
                    grid.print_grid()
                    break
        grid.print_grid()


main()
