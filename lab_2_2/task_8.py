import time
def processing_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        diff_time = (end_time - start_time) * 1000
        print(f"Время выполнения функции : {diff_time} мс")
        return result
    return wrapper

@processing_time
def test_function(n):
    time.sleep(1)

test_function(1000000)

