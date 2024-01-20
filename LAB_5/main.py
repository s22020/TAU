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
        side = random.choice(['top', 'bottom', 'left', 'right'])
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
        self.finish = self._generate_edge_coords()
        self.player_position = self._generate_edge_coords()

        while self.finish == self.player_position:
            self.finish = self._generate_edge_coords()

        for i in range(min((self.rows * self.cols) // 5, 10)):
            obstacle = self._generate_obstacle_coords()

            while obstacle == self.finish or obstacle == self.player_position or obstacle in self.obstacles:
                obstacle = self._generate_obstacle_coords()
            self.obstacles.add(obstacle)

    def update_board_state(self):
        self.board = [[' ' for j in range(self.cols)] for i in range(self.rows)]
        self.board[self.finish[0]][self.finish[1]] = 'F'
        self.board[self.player_position[0]][self.player_position[1]] = '*'

        for obstacle in self.obstacles:
            self.board[obstacle[0]][obstacle[1]] = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
        print()

    def _is_valid_move(self, move):
        return 0 <= move[0] < self.rows and 0 <= move[1] < self.cols and (move[0], move[1]) not in self.obstacles

    def move(self, direction):
        if direction == 'up' and self._is_valid_move((self.player_position[0] - 1, self.player_position[1])):
            self.player_position = (self.player_position[0] - 1, self.player_position[1])
        elif direction == 'down' and self._is_valid_move((self.player_position[0] + 1, self.player_position[1])):
            self.player_position = (self.player_position[0] + 1, self.player_position[1])
        elif direction == 'left' and self._is_valid_move((self.player_position[0], self.player_position[1] - 1)):
            self.player_position = (self.player_position[0], self.player_position[1] - 1)
        elif direction == 'right' and self._is_valid_move((self.player_position[0], self.player_position[1] + 1)):
            self.player_position = (self.player_position[0], self.player_position[1] + 1)
        else:
            print("Invalid move")

if __name__ == '__main__':
    board_game = BoardGame(5, 5)
    while board_game.player_position != board_game.finish:
        board_game.update_board_state()
        board_game.print_board()
        print("Possible moves: up, down, left, right")
        chose_move = input("Enter your move: ")
        board_game.move(chose_move)

    print("The winner is you! \o/")