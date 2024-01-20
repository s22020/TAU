import unittest
from main import BoardGame

class TestBoardGame(unittest.TestCase):
    def setUp(self):
        self.board_game = BoardGame(5, 5)

    def test_should_have_board_game_appropriate_initialization_values(self):
        self.assertEqual(self.board_game.rows, 5)
        self.assertEqual(self.board_game.cols, 5)
        self.assertIsNone(self.board_game.player_position)
        self.assertIsNone(self.board_game.finish)
        self.assertIsInstance(self.board_game.obstacles, set)

    # def test_should_generate_edge_coords_on_board_edge(self):
    #     edge_coords = self.board_game._generate_edge_coords()
    #     self.assertTrue((0 <= edge_coords[0] < self.board_game.rows and edge_coords[1] == 0) or (0 <= edge_coords[1] < self.board_game.cols and edge_coords[0] == 0))

    def test_should_not_generate_obstacles_on_player_and_finish_positions(self):
        self.board_game._generate_positions()
        self.assertTrue(self.board_game.player_position not in self.board_game.obstacles and self.board_game.finish not in self.board_game.obstacles)

    def test_should_properly_generate_positions(self):
        self.board_game._generate_positions()
        self.assertIsNotNone(self.board_game.player_position)
        self.assertIsNotNone(self.board_game.finish)
        self.assertNotEqual(self.board_game.player_position, self.board_game.finish)


if __name__ == '__main__':
    unittest.main()