import threading
import time


def thread_process(name):
    print(f"Thread process started by thread {name}")
    time.sleep(2)
    print("Thread finished executing")


def main():
    print("Main thread started")
    t1 = threading.Thread(target=thread_process, args=("my_thread", ))
    print("Starting thread")
    t1.start()
    #t1.join()
    print("Main finished")


if __name__ == '__main__':
    main()