import time
import numpy as np


# pip install numpy


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_function():
    # pass
    total = sum(range(15_000_000))
    print("Sum is", total)


@measure_time
def my_function_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is", suma)


@measure_time
def my_function_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is", total)


my_function()
my_function_sum()
my_function_np()
# Sum is 112499992500000
# Czas wykonania funkcji my_function: 0.5918505191802979
# Sum is 112499992500000
# Czas wykonania funkcji my_function_sum: 0.7966742515563965
# Sum is 112499992500000
# Czas wykonania funkcji my_function_np: 0.033097267150878906
