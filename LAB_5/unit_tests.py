import unittest
from main import BoardGame
from unittest.mock import patch
from io import StringIO

unittest.TestLoader.sortTestMethodsUsing = None

class TestBoardGame(unittest.TestCase):
    def setUp(self):
        self.board_game = BoardGame(5, 5)

    def test_should_have_board_game_appropriate_initialization_values(self):
        self.assertEqual(self.board_game.rows, 5)
        self.assertEqual(self.board_game.cols, 5)
        self.assertIsNotNone(self.board_game.player_position)
        self.assertIsNotNone(self.board_game.finish)
        self.assertIsInstance(self.board_game.obstacles, set)

    def test_should_generate_edge_coords_on_board_edge(self):
        edge_coords = self.board_game._generate_edge_coords()
        top_edge_coords = edge_coords[0] == 0
        bottom_edge_coords = edge_coords[0] == self.board_game.rows - 1
        left_edge_coords = edge_coords[1] == 0
        right_edge__coords = edge_coords[1] == self.board_game.cols - 1
        self.assertTrue(top_edge_coords or bottom_edge_coords or left_edge_coords or right_edge__coords)
        
    def test_should_initialize_obstacle_coords_properly(self):
        obstacle_coords = self.board_game._generate_obstacle_coords()
        self.assertTrue(0 <= obstacle_coords[0] < self.board_game.rows)
        self.assertTrue(0 <= obstacle_coords[1] < self.board_game.cols)

    def test_should_generate_positions_properly(self):
        self.assertIsNotNone(self.board_game.player_position)
        self.assertIsNotNone(self.board_game.finish)
        self.assertNotEqual(self.board_game.player_position, self.board_game.finish)

    def test_should_not_generate_obstacles_on_player_and_finish_positions(self):
        self.assertTrue((self.board_game.player_position not in self.board_game.obstacles) and (self.board_game.finish not in self.board_game.obstacles))

    def test_should_update_board_state_properly(self):
        self.board_game.update_board_state()
        self.assertEqual(self.board_game.board[self.board_game.finish[0]][self.board_game.finish[1]], 'F')
        self.assertEqual(self.board_game.board[self.board_game.player_position[0]][self.board_game.player_position[1]], '*')
        for obstacle in self.board_game.obstacles:
            self.assertEqual(self.board_game.board[obstacle[0]][obstacle[1]], 'X')

    def test_should_not_move_player_on_invalid_move_command(self):
        initial_position = self.board_game.player_position
        self.board_game.move('test')
        self.assertEqual(self.board_game.player_position, initial_position)

    def test_should_indicate_move_is_invalid(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.board_game.move('test')
            printed_output = mock_stdout.getvalue().strip()
            self.assertIn("Invalid move", printed_output)
            

if __name__ == '__main__':
    unittest.main()