import time
import concurrent.futures
import multiprocessing
import os

COUNT = 50000000


class CPUBound(multiprocessing.Process):

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self) -> None:
        print("Process ID:", os.getpid())
        while self.n > 0:
            self.n -= 1


def class_process():
    cpu_count = multiprocessing.cpu_count()
    processes = [CPUBound(COUNT//cpu_count) for i in range(cpu_count)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()


def countdown(n):
    print("Process ID:", os.getpid())
    while n > 0:
        n -= 1


def process_individual():
    t1 = multiprocessing.Process(target=countdown, args=(COUNT // 2,))
    t2 = multiprocessing.Process(target=countdown, args=(COUNT // 2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def process_pool():
    with multiprocessing.Pool() as pool:
        pool.map(countdown, [COUNT//3, COUNT//3, COUNT//3])


def main():
    print("CPU Count:", multiprocessing.cpu_count())

    start = time.time()
    class_process()
    duration = time.time() - start
    print(f"Counting down to {COUNT} took {duration: .2f} seconds")


if __name__ == '__main__':
    main()