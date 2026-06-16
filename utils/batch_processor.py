def batch_process(data,batch_size=10):

    for i in range(
        0,
        len(data),
        batch_size
    ):
        yield data[i:i+batch_size]