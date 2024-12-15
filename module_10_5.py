import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding = 'utf-8') as file:
        file.readline()
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы

filenames = [f'C:\\Users\\Юлия\\PycharmProjects\\NewProject\\file {number}.txt' for number in range(1, 5)]

#Линейный вызов
#time_start = time.time()
#for i in filenames:
    #read_info(i)
#time_end = time.time()
#print(f'{time_end - time_start} линейный')

#многопроцессный
if __name__ == '__main__':
        time_start = time.time()
        with multiprocessing.Pool(processes=len(filenames)) as pool:
            pool.map(read_info, filenames)
        time_end = time.time()
        print(f'{time_end - time_start} многопроцессный')


