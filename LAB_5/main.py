class BoardGame:
    '''
     | | | | 
     | | | | 
     | | | | 
     | | | | 
     | | | | 
    '''

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for j in range(cols)] for i in range(rows)]
        self.finish = None
        self.player_position = None
        # create obstacles set
        self.obstacles = set()

    def print_board(self):
        print("- " * 5)
        for row in self.board:
            print('|'.join(row))
        print()

board_game = BoardGame(5, 5)
board_game.print_board()