from board import Board
from player import Player

class Game:
    def __init__(self):
        self.players_lst = [
            Player(input('Введите имя игрока: '), num + 1)
            for num in range(2)
        ]
        self.board = Board()
        self.state_game = True
    
    def start_move(self, player: Player):
        player.make_move(self.board)
        self.board.show_board()

    def start_game(self):
        for move in range(9):
            player = self.players_lst[0] if move % 2 != 0 else self.players_lst[1]
            self.start_move(player)
            if move > 3 and self.board.is_end_game(player.history_move):
                print(f'Игра закончена! Победил игрок: {player.name}')
                player.num_win += 1
                break
        else:
            print(f'Игра завершилась с результатом "ничья"')

        self.rollback_to_origin()

    def start_competition(self):
        while self.state_game:
            self.start_game()
            print('Текущий счет игры:\n\t{}:{:d}\n\t{}:{:d}'.format(
                self.players_lst[0].name,
                self.players_lst[0].num_win,
                self.players_lst[1].name,
                self.players_lst[1].num_win
            ))

            print('Желаете продолжить игру?')
            choice = input('Введите [Y] для выхода: ')
            if choice == 'Y':
                self.stat_game = False
        else:
            print('Game over!')

    def rollback_to_origin(self):
        for player in self.players_lst:
            player.history_move = []
        self.board.__init__()
