import time


class Timer:
    def __init__(self, duration):
        self.duration = duration
        self.callbacks = []

    def attach_callback(self, callback):
        self.callbacks.append(callback)

    def run_timer(self):
        for i in range(self.duration):
            print(f"Tick...{i}")
            time.sleep(1)

        for callback in self.callbacks:
            callback(self)


def func_one(timer):
    print(f"Event handler 1 executing after {timer.duration} seconds")


def func_two(timer):
    print(f"Event handler 2 executing after {timer.duration} second")


def func_three(timer):
    print(f"Event handler 3 executing after {timer.duration} second")


def main():
    timer = Timer(5)
    timer.attach_callback(func_one)
    timer.attach_callback(func_two)
    timer.attach_callback(func_three)
    timer.run_timer()


if __name__ == '__main__':
    main()
