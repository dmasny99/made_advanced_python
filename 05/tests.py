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