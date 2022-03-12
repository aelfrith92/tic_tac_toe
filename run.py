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


def symbol_func(p1_has_chosen):
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
        if p1_has_chosen == 'O':
            return random.choice(['X', '★'])
        elif p1_has_chosen == 'X':
            return random.choice(['O', '★'])
        else:
            return random.choice(['O', 'X'])


def main():
    """
    Core function of the game
    """
    print("\nWelcome to Tic Tac Toe. Enter the grid numbrs",
          "to play your move.")
    grid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_grid(grid_values)
    grid_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # The following variable stores player1's moves
    player1 = []
    # The following variable stores player2's moves
    player2 = []
    # The following variable stores the Player2 nature: human VS PC
    # Default is PC, unless differently specified later in the process
    p2_nature = 'PC'
    # The following dictionary determines which symbol the player has
    # chosen to play with
    preferences = {
        'p1': '',
        'p2': ''
    }
    # The user has the chance to set a few options when the game loop
    # starts for the first time or it actually ends
    # Enter game mode: 1v1 or 1vPC. For the time being, the main game
    # loop is going to be designed first. Default mode: 1vPC
    # print("Game Mode\nEnter '1' for 1vPC and '2' for 1v1")
    # gmode = input("Default game mode: 1\n")
    while preferences['p1'] == '' or preferences['p2'] == '':
        if preferences['p1'] == '':
            preferences['p1'] = symbol_func(False)
        else:
            preferences['p2'] = symbol_func(preferences['p1'])
    print(f"\nPlayer1 symbol is: {preferences['p1']}, Player2",
          f"symbol is: {preferences['p2']}")

    # The following loop runs 9 times, which is the number of cells
    # that can be filled.
    for i in range(9):
        # Each time, player1 and player 2 lists store each
        # player's moves.
        print_grid(grid_values)
        if (i + 1) % 2 == 0:
            print('player 2 turn')
        else:
            print('player 1 turn')


main()
