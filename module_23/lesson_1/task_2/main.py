class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60


class Headphone:
    name = 'Sony'
    sensetivity = 108
    micro = True


monitor_1 = Monitor()
monitor_2 = Monitor()
monitor_3 = Monitor()
monitor_4 = Monitor()

monitor_2.freq, monitor_3.freq = 144, 70

headphone_1 = Headphone()
headphone_2 = Headphone()
headphone_3 = Headphone()

headphone_1.micro = False

print('Это мы вручную вписали в каждый экземпляр соответствующие атрибуты:')
print(monitor_1.freq, monitor_2.freq, monitor_3.freq, monitor_4.freq)
print(headphone_1.micro, headphone_2.micro, headphone_3.micro)

monitors = [Monitor() for _ in range(4)]
headphones = [Headphone() for _ in range(3)]

for index, num in enumerate([60, 144, 70, 60]):
    monitors[index].freq = num

headphones[0].micro = False

print('Это мы создали списоки из экземпляров классов и обратились к этим спискам через индекс')
print(monitors[0].freq, monitors[1].freq, monitors[2].freq, monitors[3].freq)
print(headphones[0].micro, headphones[1].micro, headphones[2].micro)
