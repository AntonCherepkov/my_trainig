class Toyota:
    def __init__(self, color='red', price='1000000', null_speed='0', max_speed=200):
        self.color = color
        self.price = price
        self.current_speed = null_speed
        self.max_speed = max_speed
    
    def out_info_car(self):
        print('Color car: {}\nPrice car: {}\nCurrent speed: {}\nMax speed: {}'.format(
            self.color, self.price, self.current_speed, self.max_speed)
            )
    
car_1 = Toyota(null_speed=50)
car_1.out_info_car()
