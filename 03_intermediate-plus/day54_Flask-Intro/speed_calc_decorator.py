import time


def speed_calc_decorator(function):
    def time_diff_calc():
        start_time = time.time()
        function()
        end_time = time.time()

        print(f"{function.__name__} run speed: {end_time - start_time}s")

    return time_diff_calc


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        var = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        var = i * i


if __name__ == '__main__':
    current_time = time.time()
    print(current_time)  # seconds since Jan 1st, 1970

    fast_function()
    slow_function()
