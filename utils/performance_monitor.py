import time
import psutil
import os


def measure_performance(func, *args, **kwargs):
    process = psutil.Process(os.getpid())

    start_memory = process.memory_info().rss / 1024 / 1024
    start_time = time.perf_counter()

    result = func(*args, **kwargs)

    end_time = time.perf_counter()
    end_memory = process.memory_info().rss / 1024 / 1024

    return {
        "result": result,
        "execution_time": round(end_time - start_time, 3),
        "memory_usage": round(end_memory - start_memory, 2)
    }