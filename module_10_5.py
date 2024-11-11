import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

filenames = [f"./file {i}.txt" for i in range(1, 5)]

if __name__ == "__main__":

    start_time = datetime.datetime.now()
    for file in filenames:
        read_info(file)
    end_time = datetime.datetime.now()
    print(f"Линейное выполнение: {end_time - start_time}")


    with Pool() as pool:
        start_time = datetime.datetime.now()
        pool.map(read_info, filenames)
        end_time = datetime.datetime.now()
    print(f"Многопроцессное выполнение: {end_time-start_time}")
