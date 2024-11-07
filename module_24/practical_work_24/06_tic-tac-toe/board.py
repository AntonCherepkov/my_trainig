from cell import Cell
from my_error import CellNumberError

class Board:
    def __init__(self):
        self.cell = [Cell(num) for num in range(9)]

    def show_board(self):
        count_cell = 0
        for row in range(1, 8, 1):
            print('|', end='')
            if row % 2 == 0:
                for _ in range(3):
                    print(f"{self.cell[count_cell].sym:^3}|", end='')
                    count_cell += 1
            else:
                print(f"{'---|' * 3}", end='')
            print()

    def is_end_game(self, arg_list: list):
        arg_sort = sorted(arg_list[-3:], reverse=True)
        x, y, z = arg_sort
        if (x - y == y - z):
            return True
        else:
            return False

    def change_state(self, cell_num):
        try:
            if self.cell[cell_num].condition:
                raise CellNumberError('Клетка недоступна')
            self.cell[cell_num].condition = True
            return True

        except CellNumberError:
            return False
