import unittest
import CustomExceptions
from TickTacGame import TickTacGame
from unittest.mock import patch


class TestGame(unittest.TestCase):
    #проверка, что бросит исключение, если число параметров не 3
    def test_number_of_args(self):
        with patch('builtins.input') as inpt:
            inpt.side_effect = ['X 0 0 0', 'X 0', '0', '0 0 0 0 0 0']
            game = TickTacGame()
            for _ in range(4):
                with self.assertRaises(CustomExceptions.WrongNumberParamsException):
                    game.input_validation()

    # проверка, что вводятся нужные символы и что позиции адекватные
    def test_input_content(self):
        with patch('builtins.input') as inpt:
            inpt.side_effect = ['X 0 -1', '( 0 0', '0 3 3', '0 3 4', '-0 0 0']
            game = TickTacGame()
            for _ in range(5):
                with self.assertRaises(ValueError):
                    game.input_validation()

    # тест на вставку в занятую позицию
    def test_filled_position(self):
        with patch('builtins.input') as inpt:
            inpt.side_effect = ['0 0 0', 'X 0 1', '0 2 2', 'X 1 1', '0 1 1']
            game = TickTacGame()
            game.board = [['X', '0', '.'],
                          ['.', '0', '.'],
                          ['.', '.', 'X']]
            for _ in range(5):
                with self.assertRaises(CustomExceptions.FilledPostitionException):
                    game.input_validation()

    # тест на ход подряд одним и тем же игроком
    def test_step_order(self):
        with patch('builtins.input') as inpt:
            inpt.return_value = 'X 0 0'
            game = TickTacGame()
            game.last_elem = 'X'
            with self.assertRaises(CustomExceptions.WrongStepOrderException):
                game.input_validation()
            
            inpt.return_value = '0 0 0'
            game.last_elem = '0'
            with self.assertRaises(CustomExceptions.WrongStepOrderException):
                game.input_validation()
    
    # тест на ход (что доска поменялась)
    def test_board_step(self):
        game = TickTacGame()
        valid_board = [['X', '.', '.'],
                       ['.', '.', '.'],
                       ['.', '.', '.']]
        game.fill_cell('X', '0', '0')
        self.assertEqual(game.board, valid_board)

        game = TickTacGame()
        valid_board = [['X', '0', '.'],
                       ['.', '.', '.'],
                       ['.', '.', '.']]
        game.fill_cell('X', '0', '0')
        game.fill_cell('0', '0', '1')
        self.assertEqual(game.board, valid_board)

        game = TickTacGame()
        valid_board = [['X', '0', '.'],
                       ['.', 'X', '.'],
                       ['.', '.', '0']]
        game.fill_cell('X', '0', '0')
        game.fill_cell('0', '0', '1')
        game.fill_cell('X', '1', '1')
        game.fill_cell('0', '2', '2')
        self.assertEqual(game.board, valid_board)  
    #проверки на победу
    def test_win(self):
        # вертикально для Х
        game = TickTacGame()
        game.board = [['X', '0', '.'],
                      ['X', '.', '0'],
                      ['X', '.', '.']]
        self.assertEqual(game.check_winner(), 'X')

        game.board = [['0', 'X', '.'],
                      ['.', 'X', '0'],
                      ['.', 'X', '.']]
        self.assertEqual(game.check_winner(), 'X')

        game.board = [['.', '.', 'X'],
                      ['.', '0', 'X'],
                      ['0', '.', 'X']]
        self.assertEqual(game.check_winner(), 'X')
        # вертикально для 0
        game.board = [['0', 'X', '.'],
                      ['0', '.', 'X'],
                      ['0', '.', '.']]
        self.assertEqual(game.check_winner(), '0')

        game.board = [['X', '0', '.'],
                      ['.', '0', 'X'],
                      ['.', '0', '.']]
        self.assertEqual(game.check_winner(), '0')

        game.board = [['.', '.', '0'],
                      ['.', 'X', '0'],
                      ['X', '.', '0']]
        self.assertEqual(game.check_winner(), '0')
        # горизонтально для X
        game.board = [['X', 'X', 'X'],
                      ['0', '.', '0'],
                      ['.', '.', '.']]
        self.assertEqual(game.check_winner(), 'X')

        game.board = [['0', '.', '.'],
                      ['X', 'X', 'X'],
                      ['.', '0', '.']]
        self.assertEqual(game.check_winner(), 'X')

        game.board = [['.', '.', '.'],
                      ['.', '0', '0'],
                      ['X', 'X', 'X']]
        self.assertEqual(game.check_winner(), 'X')
         # горизонтально для 0
        game.board = [['0', '0', '0'],
                      ['X', '.', 'X'],
                      ['.', '.', '.']]
        self.assertEqual(game.check_winner(), '0')

        game.board = [['X', '.', '.'],
                      ['0', '0', '0'],
                      ['.', 'X', '.']]
        self.assertEqual(game.check_winner(), '0')

        game.board = [['.', '.', '.'],
                      ['.', 'X', 'X'],
                      ['0', '0', '0']]
        self.assertEqual(game.check_winner(), '0')
        #диагонали Х
        game.board = [['X', '.', '.'],
                      ['.', 'X', '0'],
                      ['0', '0', 'X']]
        self.assertEqual(game.check_winner(), 'X')

        game.board = [['0', '.', 'X'],
                      ['.', 'X', '0'],
                      ['X', '0', '.']]
        self.assertEqual(game.check_winner(), 'X')
        #диагонали 0
        game.board = [['0', '.', '.'],
                      ['.', '0', 'X'],
                      ['X', 'X', '0']]
        self.assertEqual(game.check_winner(), '0')

        game.board = [['X', '.', '0'],
                      ['.', '0', 'X'],
                      ['0', 'X', '.']]
        self.assertEqual(game.check_winner(), '0')

    #проверка на ничью
    def test_draw(self):
        game = TickTacGame()
        game.board = [['X', '0', '0'],
                      ['0', 'X', 'X'],
                      ['0', 'X', '0']]
        self.assertEqual(game.check_winner(), 'draw')

        game.board = [['0', 'X', 'X'],
                      ['X', '0', '0'],
                      ['X', '0', 'X']]
        self.assertEqual(game.check_winner(), 'draw')

if __name__ == '__main__':
    unittest.main()