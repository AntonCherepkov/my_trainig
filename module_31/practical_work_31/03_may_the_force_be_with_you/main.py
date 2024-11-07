from ship_class import SWAPIInfo, print_info


if __name__ == '__main__':
    x_wing = SWAPIInfo()
    x_wing.ship = 'X-wing'

    print_info(x_wing.ship)
    x_wing.dump_file()

    print(SWAPIInfo.__doc__)