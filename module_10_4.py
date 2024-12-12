import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests: # добавляем в очередь гостей
            allocated = False #проверяем, есть ли гости в очереди
            for table in self.tables: #перебираем все столы в очереди
                if table.guest is None: # если стол свободен
                    table.guest = guest  #сажаем гостя за стол
                    guest.start() # запускаем гостя в отдельном потоке
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    allocated = True # стол свободен
                    break

            if not allocated:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while (not self.queue.empty()
               or any(table.guest is not None for table in self.tables)): # проверка на пустые столы
            for table in self.tables:
                if table.guest is not None: # если стол свободен
                    if not table.guest.is_alive(): # проверка состояния потока guest в очереди и его завершения работы в очереди
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                        if not self.queue.empty(): # если есть еще столы, то выбираем следующий стол из очереди
                            next_guest = self.queue.get() # получаем следующий стол из очереди
                            table.guest = next_guest # устанавливаем новый стол в очереди
                            next_guest.start() # запускаем поток guest в очереди
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()



