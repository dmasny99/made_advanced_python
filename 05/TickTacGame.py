class TickTacGame:
    def __init__(self):
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']]
    def show_board(self):
        for elem in self.board:
            print(*elem)
    

if __name__ == '__main__':
    game = TickTacGame()
    game.show_board()