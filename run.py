# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# generate board objects for both players
# populate ships
# determine starting player
# take user input
# return results

class GameBoard:
    """Creates a game board object"""

    def __init__(self, board_dimension):
        """initialises Game Board object based on dimensions provided"""
        self.board_dimension = board_dimension
        self.grid = [0 for i in range(self.board_dimension * self.board_dimension)]
        print(self.grid)

    def print_game_board(self):
        """prints the current game board to the console"""
        for row in (range(self.board_dimension)):
            print()
            for column in (range(self.board_dimension)):
                grid_location = row * self.board_dimension + column
                print(self.grid[grid_location], end=" ")
        print()

    def update_game_board(self, row, column, new_value):
        """updates a value at a specific co-ordiante on the game board"""
        row -= 1
        if row <= 1:
            self.grid[row * self.board_dimension + column - 1] = new_value
        else:
            self.grid[(row * (self.board_dimension)) + column - 1] = new_value
        print(self.grid)


game = GameBoard(3)
game.update_game_board(1, 3, "new data1")
game.print_game_board()
