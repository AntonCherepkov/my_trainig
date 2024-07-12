class Coordinate:
    __count = 0

    def __init__(self, coord_x=0, coord_y=0):
        self.set_coord(coord_x, coord_y)
        self.__count += 1

    def get_count(self,):
        return self.__count

    def get_coord(self):
        return self.__coord_x, self.__coord_y

    def set_coord(self, coord_x, coord_y):
        if not all([isinstance(coord_x, (int, float)), isinstance(coord_y, (int, float))]):
            raise TypeError('Координаты должны быть числом!')
        else:
            self.__coord_x = coord_x
            self.__coord_y = coord_y

    def __str__(self):
        return f'Координата X: {self.__coord_x},\nКоордината Y: {self.__coord_y},\nТочек всего: {self.__count}'


point_1 = Coordinate(1, 3)
print(point_1)
