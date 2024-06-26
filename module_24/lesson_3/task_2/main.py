class Coordinate:
    count_points = 0

    def __init__(self, point_x=0, point_y=0):
        self.point_x = point_x
        self.point_y = point_y
        Coordinate.count_points += 1

    def print_info(self):
        print('Coordinate x: {}\nCoordinate y: {}\nCoordinates of everything: {:d}'.format(
            self.point_x, self.point_y, self.count_points
        ))


coor_1 = Coordinate()
coor_1.print_info()

for x, y in [(2, 3), (4, 5), (6, 7)]:
    coor_1 = Coordinate(x, y)
    coor_1.print_info()
    