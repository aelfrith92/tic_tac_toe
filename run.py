import random
import time
from colorama import init, Fore
init()


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
        print(Fore.YELLOW + "\t     |     |")
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
        print(Fore.YELLOW + "\nEnter '1' to play with X\n")
        print("Enter '2' to play with O\n")
        print("Enter '3' to play with ★\n")
        symbol = input("Pick the symbol that you want to play with:\n")
        try:
            symbol = int(symbol)
            if symbol < 1 or symbol > 3:
                print(Fore.RED + '\nYou can choose options listed above only')
                raise ValueError(Fore.RED + 'Input out of range')
        except (ValueError, UnicodeDecodeError):
            print(Fore.RED + 'Try again. Choose 1, 2, or 3\n')
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
        print(Fore.YELLOW + 'Enter the cell number to play your turn\n')
        chosen_cell = input()
        try:
            chosen_cell = int(chosen_cell)
            if chosen_cell < 1 or chosen_cell > 9 or \
               self.moves[chosen_cell - 1] != ' ':
                print(Fore.RED + '\nInvalid input. Choose an empty cell, by',
                      'entering a number between 1 and 9')
                raise ValueError(Fore.RED + 'Input out of available range')
        except (ValueError, UnicodeDecodeError):
            print(Fore.RED + 'Try again. Choose an empty cell\n')
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
            print(Fore.YELLOW + '\nGAME MODE\n')
            gmode = int(input("\nEnter '1' for 1vPC and '2' for 1v1\n"))
            if gmode < 1 or gmode > 2:
                print(Fore.RED + '\nInvalid input. Choose a valid mode, by',
                      'entering 1 or 2')
                raise ValueError(Fore.RED + 'Input out of available range')
            else:
                break
        except (ValueError, UnicodeDecodeError):
            print(Fore.RED + 'Try again. Choose 1 or 2\n')
    return 'P' if gmode == 1 else 'H'


def game_loop(gmode):
    """
    Core function of the game
    """
    # --------- INTRODUCTORY PART OF THE MAIN CODE ---------

    # Player types can be H - human, G - grid, P - PC
    # The grid player is a special player, as this instance
    # shares a few methods and characteristics
    grid = Player('Grid', 'G', [])
    # The following variable keeps track of cells already played
    grid.moves = [' ' for i in range(9)]

    # player2 instance: the game mode determines its nature
    player2 = Player('P2', gmode, [])
    # player1 instance
    player1 = Player('P1', 'H', [])

    print(Fore.CYAN + '\nPLAYER 1')
    player1.symbol_pref()
    if player2.ptype == 'H':
        print(Fore.CYAN + '\nPLAYER2')
    player2.symbol_pref()
    while player2.preference == player1.preference:
        if player2.ptype == 'H':
            print(Fore.RED + '\nYou cannot choose the same symbol. Pick',
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
            print(Fore.CYAN + '\nPLAYER 2 TURN')
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
        else:
            print(Fore.CYAN + '\nPLAYER 1 TURN')
            played_cell = grid.play()
            grid.moves[played_cell - 1] = player1.preference
            player1.moves.append(played_cell)
            player1.moves.sort()

        check = ((player1 if (i + 1) % 2 != 0 else player2).check_win()
                 if i > 3 else False)
        if check:
            print(Fore.CYAN + f"The winner is:"
                  f"{' player1' if (i + 1) % 2 != 0 else ' player2'}")
            grid.print_grid()
            return (i + 1) % 2
        grid.print_grid()
        time.sleep(1.5)


def main():
    """
    Main function that triggers the game loop above
    """
    print(Fore.CYAN + "\nWelcome to Tic Tac Toe. Enter the grid numbers",
          "to play your move.\n")

    print("\n")
    print(Fore.YELLOW + "\t     |     |")
    print("\t  1  |  2  | 3")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  4  |  5  | 6")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  7  |  8  | 9")
    print("\t     |     |")
    print("\n")

    scoreboard = {
        'p1': 0,
        'p2': 0
    }
    outer_flag = True
    ptype = ptype_v()
    while outer_flag:
        score = game_loop(ptype)

        if score != 0:
            scoreboard['p1'] += 1
        else:
            scoreboard['p2'] += 1

        print(Fore.GREEN + '-------------- SCOREBOARD --------------')
        print('*                                      *')
        print(f"* PLAYER 1: {scoreboard['p1']}          ",
              '               *')
        print(f"* PLAYER 2: {scoreboard['p2']}          ",
              '               *')
        print('*                                      *')
        print('----------------------------------------')

        print(Fore.CYAN + "\nDo you wish to play again?")
        break_flag = True
        while break_flag:
            try:
                keep_playing = int(input(Fore.CYAN + "\nEnter '1' to keep"
                                         " playing and '0' to quit\n"))
                if keep_playing < 0 or keep_playing > 1:
                    print(Fore.RED + '\nInvalid input. Choose an action',
                          ' listed above, by entering 1 or 0')
                    raise ValueError(Fore.RED + 'Input out of available range')
                elif keep_playing == 1:
                    break_flag = False
                else:
                    break_flag = False
                    outer_flag = False
                    break
            except (ValueError, UnicodeDecodeError):
                print(Fore.RED + 'Try again. Choose 1 or 0\n')


main()
