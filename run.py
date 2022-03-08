def print_tic_tac_toe(values):
    """
    Function to print Tic Tac Toe
    """
    print("\n")
    print("\t     |     |")
    print(f"\t  {values[0]}  |  {values[1]}  |  \
{values[2]}")
    print('\t_____|_____|_____')

    print("\t     |     |")
    print(f"\t  {values[3]}  |  {values[4]}  |  \
{values[5]}")
    print('\t_____|_____|_____')

    print("\t     |     |")

    print(f"\t  {values[6]}  |  {values[7]}  |  \
{values[8]}")
    print("\t     |     |")
    print("\n")


def main():
    """
    Core function of the game
    """
    print("\nWelcome to Tic Tac Toe. The numbers \
in the grid indicate the cell that the player \
will enter their symbol into")
    grid_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_tic_tac_toe(grid_values)
    print("Please enter your preferences below \
before starting the game.")
    # to be implemented: 1v1 and 1vPC choice


main()
