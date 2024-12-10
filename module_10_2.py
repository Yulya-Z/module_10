import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def battle(self, enemies):
        while enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            self.days +=1

            if self.enemies < 0:
                self.enemies = 0
                break
            print(f'{self.name} сражается {self.days} день..., осталось {self.enemies} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle(self.enemies)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
# Вывод строки об окончании сражения
first_knight.join()
second_knight.join()
print('Все битвы закончились!')