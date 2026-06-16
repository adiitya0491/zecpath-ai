"""
Day 60
Memory Optimization
"""


def memory_efficient_processing(
    data_stream
):
    """
    Generator-based processing.
    """

    for item in data_stream:
        yield item * 2


if __name__ == "__main__":

    data = [1, 2, 3, 4]

    for item in memory_efficient_processing(data):
        print(item)