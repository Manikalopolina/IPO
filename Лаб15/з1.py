import time
from functools import wraps
def timeit(method):
    @wraps(method)
    def timed(*args, **kw):
        ts = time.monotonic()
        result = method(*args, **kw)
        te = time.monotonic()
        ms = (te - ts) * 1000
        all_args = ', '.join(tuple(f'{a!r}' for a in args)
                             + tuple(f'{k}={v!r}' for k, v in kw.items()))
        print(f'{method.__name__}({all_args}): {ms:2.2f} ms')
        return result
    return timed
# использование:
@timeit
def slow_func(x, y, sleep):
    time.sleep(sleep)
    return x + y

 slow_func(10, 20, sleep=2) # slow_func выполняет сложение двух чисел x и y.
# Функция также имеет параметр sleep, который указывает время в секундах, на которое функция будет засыпать с использованием функции time.sleep, прежде чем выполнить сложение.
# Функция slow_func декорирована с помощью  @timeit, который измеряет время выполнения функции.
