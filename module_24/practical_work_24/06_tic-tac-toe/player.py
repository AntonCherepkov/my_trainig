class Player:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.num_win = 0
        self.history_move = []

    def make_move(self, board):
        print(f'Ходит игрок {self.name}')
        while True:
            player_move = int(input('Введите номер клетки: '))
            if board.change_state(player_move):
                board.cell[player_move].sym = board.cell[player_move].symbol[self.num]
                self.history_move.append(player_move)
                break
            else:
                print('Введите еще раз!')
    