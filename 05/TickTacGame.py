class TickTacGame:
    def __init__(self):
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
        self.last_elem = None

    def show_board(self):
        for elem in self.board:
            print(*elem)
        print('\n')

    def make_step(self, elem, x, y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Invalid input: x and y lie in [0; 2]')
            return
        if self.last_elem == elem:
            if elem == '0':
                print('It is now your turn now! This turn is for X')
                return
            elif elem == 'X':
                print('It is now your turn now! This turn is for 0')
                return
        if elem not in ['X', '0']:
            print('Invalid char: only X and 0 are allowed')
            return
        if self.board[x][y] == '.': # если поле свободно
            self.board[x][y] = elem
            self.last_elem = elem
            self.check_winner() # проверка выигрыша
        else:
            print(f'This cell is already filled by {self.board[x][y]}, try another one!')
    def clear_board(self):
        self.__init__()

    def check_winner(self):
        for row in self.board:
            if len(set(row)) == 1:
                if row[0] == '.':
                    return
                else:
                    # TODO проверка на ничью
                    # self.check_draw()
                    print(f'Winner is {row[0]}')
                    
        for column in range(3):
            if self.board[0][column] == self.board[1][column] \
                and self.board[1][column] == self.board[2][column]:
                if self.board[0][column] == '.':
                    return
                else:
                    # TODO проверка на ничью
                    # self.check_draw()
                    print(f'Winner is {self.board[0][column]}')
    
    def check_draw(self):
        pass

if __name__ == '__main__':
    game = TickTacGame()
    game.show_board()
    game.make_step('X', 0, 0)
    game.make_step('0', 0, 1)
    game.make_step('X', 1, 0)
    game.make_step('0', 0, 2)
    game.make_step('X', 2, 0)

    game.show_board()