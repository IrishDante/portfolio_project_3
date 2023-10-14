# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# generate board objects for both players
# populate ships
# determine starting player
# take user input
# return results

"""These constants are used for the game output"""
SHIP = "@"
EMPTY = "."
HIT = "X"
MISS = "*"


class GameBoard:
    """Creates a game board object"""

    def __init__(self, board_dimension):
        """Initialises Game Board object based on dimensions provided taking board dimension allow dynamic boards"""

        self.board_dimension = board_dimension
        self.grid = [0 for i in range(self.board_dimension * self.board_dimension)]
        print(self.grid)

    def print_game_board(self):
        """Prints the current game board to the console"""

        for row in (range(self.board_dimension)):
            print()
            for column in (range(self.board_dimension)):
                grid_location = row * self.board_dimension + column
                print(self.grid[grid_location], end=" ")
        print()

    def update_game_board(self, row, column, new_value):
        """Updates a value at a specific coordinate on the game board"""

        row -= 1
        if row <= 1:
            self.grid[row * self.board_dimension + column - 1] = new_value
        else:
            self.grid[(row * self.board_dimension) + column - 1] = new_value
        print(self.grid)

    def place_ship(self, starting_row, starting_column, end_row, end_column):
        """
        stores inputs as a list of lists
        ensures the largest row or column is last in the list
        all ships are at least 2 units long so one will always have a greater value.
        """

        ship = [[starting_row, starting_column], [end_row, end_column]]
        if ship[0][0] > ship[1][0]:
            ship[0], ship[1] = ship[1], ship[0]
        elif ship[1][0] > ship[1][1]:
            ship[0], ship[1] = ship[1], ship[0]
            #  Now the ship list is ordered with the second list being place at index [1]

        ship_length = ship[1][0] - ship[0][0] + ship[1][1] - ship[0][1]
        #  the matching pair negate so the difference between the unique values is found
        if ship[0][1] != ship[0][0]:
            while ship_length > 0:
                self.update_game_board(ship[0][0], ship[0][1] - ship_length, SHIP)
                ship_length -= 1
        else:
            while ship_length > 0:
                self.update_game_board(ship[1][1] - ship_length, ship[1][0], SHIP)
                ship_length -= 1


class Player:
    """Creates a player object, a player object owns a GameBoard."""

    def __init__(self, name):
        self.name = name
        self.myBoard = GameBoard(5)


def main():
    """Operates the battleship game"""

    player1 = Player("test name one")
    player2 = Player("test opponent")
