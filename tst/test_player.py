from lib2048.play.player import Player
from lib2048.solve.simulator import Keys
from mock import Mock

SCORE = 123
GRID = [[2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2]]


def test_player():
    game_mock = Mock()
    game_mock.read_grid = Mock(return_value = GRID)
    game_mock.read_score = Mock(return_value = SCORE)
    solver_mock = Mock()
    solver_mock.solve = Mock(return_value = [Keys.UP])

    player = Player(game_mock, solver_mock)
    player.play()

    game_mock.finish.assert_called_with()
