class Family:
    name = 'Common'
    fund = 100000
    having_a_house = False

    def print_info(self):
        print('Family name: {}\n'
              'Family budget: {}\n'
              'Presence of house: {}\n'. format(
            self.name, self.fund, self.having_a_house
        ))

    def add_earning(self, earn):
        self.fund += earn

    def buy_house(self, price_house, discount=0):
        price_house -= price_house // 100 * discount
        if price_house <= self.fund:
            print('The purchase of the house has been completed!')
            self.fund -= price_house
            self.having_a_house = True
        else:
            print('The purchase cannot be completed, there are not enough funds')


my_family = Family()
my_family.name = 'Cherepkovi'
my_family.buy_house(1000000)
 
my_family.print_info()

my_family.add_earning(800000)
my_family.print_info()

my_family.buy_house(1000000, 10)
my_family.print_info()
