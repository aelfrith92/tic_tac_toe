import random


def print_grid(values):
    """
    Function to print Tic Tac Toe
    """
    print("\n")
    print("\t     |     |")
    print(f"\t  {values[0]}  |  {values[1]}  | ",
          f"{values[2]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {values[3]}  |  {values[4]}  | ",
          f"{values[5]}")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print(f"\t  {values[6]}  |  {values[7]}  | ",
          f"{values[8]}")
    print("\t     |     |")
    print("\n")


def return_choice(s_choice):
    """
    This function returns the player's choice
    """
    if s_choice == 1:
        return 'X'
    elif s_choice == 2:
        return 'O'
    else:
        return '★'


def validation():
    """
    It validates the input. The func returns a list which allows
    symbol_func both to break the validation in the while loop
    and store the correct iniput for the player.
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


def symbol_func(mode, p1_has_chosen):
    """
    It assigns a symbol to the dictionary 'preferences'
    """
    while True and not p1_has_chosen:
        # The following variable receives a list from
        # func validation() above.
        symbol_list = validation()
        if symbol_list[0]:
            symbol = symbol_list[1]
            break

    # This block executes only if no errors have been raised.
    # Next action is: filling the preferences dict with each
    # player's choice. In case of a PC player, a random choice
    # is given.

    # it makes sense to create a function, as the symbol choice
    # is an opportunity for both players -> DRY
    if not p1_has_chosen:
        return return_choice(symbol)
    else:
        # At this point, the code should check whether player 2 is
        # human or PC. If P2 is human, repeats the symbol choice and
        # assigns it, otherwise random assignment to preferences['p2']
        if mode == 'PC':
            if p1_has_chosen == 'O':
                return random.choice(['X', '★'])
            elif p1_has_chosen == 'X':
                return random.choice(['O', '★'])
            else:
                return random.choice(['O', 'X'])
        else:
            while True:
                # The following variable receives a list from
                # func validation() above.
                symbol_list = validation()
                if symbol_list[0] and \
                   return_choice(symbol_list[1]) != p1_has_chosen:
                    symbol = symbol_list[1]
                    break
                else:
                    print('\nPlayer2 must choose a different symbol to play.',
                          'Please, choose another option.\nPlayer1 has picked',
                          f'{p1_has_chosen} already.\n')
            return return_choice(symbol)


def validate_play(cells):
    """
    This function validates the input once started playing
    """
    chosen_cell = input('Enter the cell number to play your turn\n')
    try:
        chosen_cell = int(chosen_cell)
        if chosen_cell < 1 or chosen_cell > 9 or cells[chosen_cell - 1] != ' ':
            print('\nInvalid input. Choose an empty cell, by',
                  'entering a number between 1 and 9')
            raise ValueError('Input out of available range')
    except ValueError:
        print('Try again. Choose an empty cell\n')
        return [False, '']
    return [True, chosen_cell]


def play(cells_taken):
    """
    This function lets players play their turn. First
    action is inputting the cell number and validation
    """
    # The following loop is for an actual player, not PC
    while True:
        valid = validate_play(cells_taken)
        if valid[0]:
            valid_choice = valid[1]
            break
    return valid_choice


def pc_move(cells):
    """
    This function determines the pc move by checking
    already-filled cells.
    """
    random_index = random.randint(0, 8)
    while cells[random_index] != ' ':
        random_index = random.randint(0, 8)
    return random_index


def define_gmode():
    """
    This function defines and validates the game mode input
    """
    while True:
        try:
            print('\nGAME MODE\n')
            mode = int(input("Enter '1' for 1vPC and '2' for 1v1\n"))
            if mode < 1 or mode > 2:
                print('\nInvalid input. Choose a valid mode, by',
                      'entering 1 or 2')
                raise ValueError('Input out of available range')
            else:
                break
        except ValueError:
            print('Try again. Choose 1 or 2\n')
    return 'PC' if mode == 1 else 'H'


def check_win(p1, p2):
    """
    This function checks whether someone has won
    """
    winning_combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                            (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    for i in winning_combinations:
        check_list_p1 = [True if p1[x] in i else False for x in range(len(p1))]
        check_list_p2 = [True if p2[x] in i else False for x in range(len(p2))]
        print(f'Tuple checked: {i}\nP1 checklist is:',
              f'{check_list_p1}\nP2 checklist is: {check_list_p2}')
        if check_list_p1.count(True) == 3:
            return ['p1', True]
        elif check_list_p2.count(True) == 3:
            return ['p2', True]
        else:
            continue
    return ['', False]


def main():
    """
    Core function of the game
    """
    print("\nWelcome to Tic Tac Toe. Enter the grid numbers",
          "to play your move.")
    # The following variable keeps track of cells already played
    grid_values = [(i+1) for i in range(9)]
    print_grid(grid_values)
    grid_values = [' ' for i in range(9)]
    # The following variable stores player1's moves
    player1 = []
    # The following variable stores player2's moves
    player2 = []
    # The user has the chance to set a few options when the game loop
    # starts for the first time or it actually ends
    # The following variable stores the Player2 nature: human VS PC
    # Enter game mode: 1v1 or 1vPC.
    p2_nature = define_gmode()
    # The following dictionary determines which symbol the player has
    # chosen to play with
    preferences = {
        'p1': '',
        'p2': ''
    }
    while preferences['p1'] == '' or preferences['p2'] == '':
        if preferences['p1'] == '':
            preferences['p1'] = symbol_func(p2_nature, False)
        else:
            preferences['p2'] = symbol_func(p2_nature, preferences['p1'])
    print(f"\nPlayer1 symbol is: {preferences['p1']}, Player2",
          f"symbol is: {preferences['p2']}")

    # The following loop runs 9 times, which is the number of cells
    # that can be filled.
    print_grid(grid_values)
    for i in range(9):
        # Each time, player1 and player 2 lists store each
        # player's moves.
        if (i + 1) % 2 == 0:
            print('player 2 turn')
            # If the player2 nature is PC, it randomly fills
            # cells via grid_values
            if p2_nature == 'PC':
                pc_index = pc_move(grid_values)
                grid_values[pc_index] = preferences['p2']
                player2.append(pc_index + 1)
            else:
                played_cell = play(grid_values)
                grid_values[played_cell - 1] = preferences['p2']
                player2.append(played_cell)
            player2.sort()
        else:
            print('player 1 turn')
            played_cell = play(grid_values)
            grid_values[played_cell - 1] = preferences['p1']
            player1.append(played_cell)
            player1.sort()
        print_grid(grid_values)
        if i > 4:
            check = check_win(player1, player2)
            if check[1]:
                print("The winner is",
                      f"{'Player1' if check[0] == 'p1' else 'Player2'}")
                break
        print(f'Player1 has played {player1} so far...\nPlayer2 has played',
              f'{player2} so far...\nOverall grid: {grid_values}')


main()
