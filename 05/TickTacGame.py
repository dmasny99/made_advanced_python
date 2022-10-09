import CustomExceptions

class TickTacGame:
    def __init__(self):
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
        self.last_elem = None

    def show_board(self):
        print('\n')
        for elem in self.board:
            print(*elem)
        print('\n')
    
    def input_validation(self):
        data = input().split()
        if len(data) != 3:
            raise CustomExceptions.WrongNumberParamsException
        elem, x, y = data
        if x not in ['0', '1', '2'] or y not in ['0', '1', '2'] or elem not in ['X', '0']:
            raise ValueError
        if self.board[int(x)][int(y)] != '.':
            raise CustomExceptions.FilledPostitionException
        if elem == self.last_elem:
            raise CustomExceptions.WrongStepOrderException
        return elem, x, y

    def fill_cell(self, elem, x, y):
        self.board[int(x)][int(y)] = elem

    def play(self):
        for _ in range(9):
            try:
                elem, x, y = self.input_validation()
            except CustomExceptions.WrongNumberParamsException:
                print('Wrong numner of params: must be char, x, y')
                continue
            except ValueError:
                print('Incorrect input: x and y lie in [0;2], element can be only X or 0')
                continue
            except CustomExceptions.FilledPostitionException:
                print(f'This cell is already filled by {self.board[x][y]}')
                continue
            except CustomExceptions.WrongStepOrderException:
                print('This step should be done by another player!')
                continue
            self.fill_cell(elem, x, y)
            self.last_elem = elem
            self.show_board()
            winner = self.check_winner()
            if winner == 'Draw':
                print('Draw')
                return None
            elif winner in ['X', '0']:
                print(f'Winner is {winner}')
                return None

    def clear_board(self):
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]

    def check_winner(self):
        #горизонтально
        for row in self.board:
            if len(set(row)) == 1:
                if row[0] != '.':
                    return row[0]
        #вертикально
        for column in range(3):
            if self.board[0][column] == self.board[1][column] \
                and self.board[1][column] == self.board[2][column]:
                if self.board[0][column] != '.':
                    return self.board[0][column]
        # проверка диагоналей
        if self.board[0][0] == self.board[1][1] and  self.board[1][1] == self.board[2][2]:
            if self.board[0][0] != '.':
                return self.board[0][0]

        if self.board[2][0] == self.board[1][1] and  self.board[1][1] == self.board[0][2]:
            if self.board[2][0] != '.':
                return self.board[2][0]
        #ничья, если не осталось свободных клеток
        cnt = 0
        for row in self.board:
            for elem in row:
                if elem == '.':
                    cnt += 1
        if cnt == 0 :
            return 'draw'
        return None

