import time

def time_this(num_runs):
    def decorator(func):
        def wrap(*args, **kvargs):
            start = time.time()
            for r in range(num_runs):
                func(*args, **kvargs)
            avg_time = (time.time() - start) / num_runs
            print('Выполнение заняло %.5f секунд' % avg_time)
        return wrap
    return decorator

class TimeThis:
    def __init__(self, num_runs=1):
        self.num_runs = num_runs

    def _start(self):
        self.start = time.time()

    def _stop(self):
        avg_time = (time.time() - self.start) / self.num_runs
        print('Выполнение заняло %.5f секунд' % avg_time)

    def __enter__(self):
        self.num_runs = 1
        self._start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._stop()

    def __call__(self, func):
        def wrap(*args, **kvargs):
            self._start()
            for r in range(self.num_runs):
                func(*args, **kvargs)
            self._stop()
        return wrap



@time_this(5)
def f1(a, b, c):
    print("f1")
    for j in range(10000000):
        pass

@TimeThis(10)
def f2(a, b, c):
    print("f2")
    for j in range(10000000):
        pass

def f3(a, b, c):
    print("f3")
    for j in range(10000000):
        pass

if __name__ == '__main__':
    f1(1, 2, 3)
    f2(1, 2, 3)
    with TimeThis() as t:
        f3(1, 2, 3)
