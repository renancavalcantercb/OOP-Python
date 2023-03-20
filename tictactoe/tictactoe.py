class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.turn = 0
        self.player1 = Player(input('Enter name of player 1: '), 'X')
        self.player2 = Player(input('Enter name of player 2: '), 'O')
        self.current_player = self.player1
        self.winner = None

    def print_board(self):
        print('---------')
        for row in self.board:
            print('|', ' '.join(row), '|')
        print('---------')

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                self.winner = row[0]
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.winner = self.board[0][col]
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.board[0][0]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.board[0][2]
            return True
        return False

    def check_draw(self):
        return self.turn == 9 and not self.check_winner()

    def check_game_over(self):
        return self.check_winner() or self.check_draw()

    def play(self):
        while not self.check_game_over():
            self.print_board()
            while True:
                try:
                    row, col = map(int, input('Enter the coordinates(ex: 1 2): ').split())
                    if row not in range(1, 4) or col not in range(1, 4):
                        print('Coordinates should be from 1 to 3!')
                    elif self.board[row - 1][col - 1] != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        self.board[row - 1][col - 1] = self.current_player.symbol
                        self.turn += 1
                        self.current_player = self.player1 if self.current_player == self.player2 else self.player2
                        break
                except ValueError:
                    print('You should enter numbers!')
        self.print_board()
        if self.check_winner():
            print(f'{self.winner} wins')
        else:
            print('Draw')


if __name__ == '__main__':
    game = Board()
    game.play()
