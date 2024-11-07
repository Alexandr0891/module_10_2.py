# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power



    def run(self):
        enemies_power = 100
        number_days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(enemies_power):
            if enemies_power > 0:
                enemies_power -= self.power
                number_days += 1
                sleep(1)
                print(f'{self.name} сражается {number_days} день(дня)..., осталось {enemies_power} войнов.')
                if enemies_power <= 0:
                    print(f'{self.name} одержал победу спустя {number_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')