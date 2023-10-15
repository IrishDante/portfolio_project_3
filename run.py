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
    grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def __init__(self, board_dimension):
        """Initialises Game Board object based on dimensions provided taking board dimension allow dynamic boards"""

        self.board_dimension = board_dimension
        #  self.grid = [EMPTY for i in range(self.board_dimension ** 2)]
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
        coordinate = self.get_coordinate(row, column)
        self.grid[coordinate] = new_value

    def place_ship(self, starting_row, starting_column, end_row, end_column):
        """
        stores inputs as a list of lists
        ensures the largest row or column is last in the list
        all ships are at least 2 units long so one will always have a greater value
        expects values as low as 1 and as high as board dimension
        """
        ship = [[starting_row, starting_column], [end_row, end_column]]
        ship = self.order_ship_highest_last(ship)
        ship_length = ship[1][0] - ship[0][0] + ship[1][1] - ship[0][1]
        #  the matching pair negate so the difference between the unique values is found
        self.place_ship_on_game_board(ship, ship_length)

    @staticmethod
    def order_ship_highest_last(ship_to_examine):
        """
        Compares a list of two coordinates and determines the coordinate with the greatest value
        the places it last in the list
        """
        ship = ship_to_examine
        if ship[0][0] > ship[1][0] or ship[0][1] > ship[1][1]:
            returned_ship = [ship[1], ship[0]]
        else:
            returned_ship = ship
        return returned_ship

    def place_ship_on_game_board(self, ship, ship_length):
        """Places a ship on the player's game board"""

        ship_column_short = ship[0][1]
        ship_row_long = ship[1][0]
        ship_column_long = ship[1][1]
        if ship_column_short != ship_column_long:  # check if ship columns are different
            while ship_length >= 0:
                self.update_game_board(ship_row_long, ship_column_long-ship_length, SHIP)
                ship_length -= 1
        else:  # applies if rows are different
            while ship_length >= 0:
                self.update_game_board(ship_row_long-ship_length, ship_column_long, SHIP)
                ship_length -= 1

    def check_if_legal_ship(self):
        return None

    def check_if_hit(self, row, column):
        """
        Takes coordinates and checks if that location is a HIT, MISS or has already been selected
        updates location as appropriate
        """
        coordinate = self.get_coordinate(row, column)
        if self.grid[coordinate] == SHIP:
            self.grid[coordinate] = HIT
            print(f"Hit at {row},{column}")
            return "Hit"
        elif self.grid[coordinate] == HIT or self.grid[coordinate] == MISS:
            return "Already chosen"
        elif self.grid[coordinate] == EMPTY:
            self.grid[coordinate] = MISS
            print(f"Miss at {row},{column}")
            return "Miss"
        else:
            return "Error in coordinate provided"

    def get_coordinate(self, row, column):
        """Returns the location of the coordinate for [row][column] in the 1D list"""
        row -= 1
        column -= 1
        return row + self.board_dimension * column


class Player:
    """Creates a player object, a player object owns a GameBoard."""

    def __init__(self, name):
        self.name = name
        self.myBoard = GameBoard(4)
        self.myBoard.place_ship(1, 4, 1, 2)


def main():
    """Operates the battleship game"""

    player1 = Player("test name one")
    player2 = Player("test opponent")
    player1.myBoard.print_game_board()
    player2.myBoard.print_game_board()


main()
