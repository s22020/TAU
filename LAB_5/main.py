import random

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
        self._generate_positions()

    def _generate_edge_coords(self):
        side = random.choice(['top', 'right', 'left', 'bottom'])
        if side == 'top':
            return 0, random.randint(0, self.cols - 1)
        elif side == 'bottom':
            return self.rows - 1, random.randint(0, self.cols - 1)
        elif side == 'left':
            return random.randint(0, self.rows - 1), 0
        elif side == 'right':
            return random.randint(0, self.rows - 1), self.cols - 1

    def _generate_obstacle_coords(self):
        return random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)

    def _generate_positions(self):
        self.player_position = self._generate_edge_coords()
        self.finish = self._generate_edge_coords()

        while self.finish == self.player_position:
            self.finish = self._generate_edge_coords()

        for i in range(min(self.rows * self.cols // 5, 10)):
            obstacle = self._generate_obstacle_coords()

            while obstacle == self.finish or obstacle == self.player_position or obstacle in self.obstacles:
                obstacle = self._generate_obstacle_coords()
            
            self.obstacles.add(obstacle)

    def print_board(self):
        print("- " * 5)
        for row in self.board:
            print('|'.join(row))
        print()



board_game = BoardGame(5, 5)
board_game.print_board()