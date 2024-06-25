class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def show_info(self):
        print('Color car: {}\nPrice car: {}\nMaximal speed: {}\nCurrent speed: {}\n'.format(
            self.color,
            self.price,
            self.max_speed,
            self.current_speed
        ))

    def change_speed(self, new_speed):
        try:
            if new_speed <= self.max_speed:
                self.current_speed = new_speed
            else:
                raise ValueError('The current speed cannot exceed the maximum')

        except ValueError as speed_error:
            print('Error: ', speed_error)
            self.current_speed = self.max_speed


first_car = Toyota()
first_car.show_info()

first_car.change_speed(130)
first_car.show_info()

first_car.change_speed(350)
first_car.show_info()
