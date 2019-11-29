def producer(inp_data):
    """generator"""
    for val in inp_data:
        yield val


def coroutine_consumer():
    try:
        while True:
            op = (yield)  # yield on RHS is consumer
            print("Received", op)
    except GeneratorExit:
        print("Consumed all the data")


def send_receive(data_queue):
    gobj = producer(data_queue)
    consumer_queue = coroutine_consumer()
    next(consumer_queue)
    while True:
        try:
            produced_value = next(gobj)
            print("Sent", produced_value)
            consumer_queue.send(produced_value)
        except StopIteration:
            print("produced all the data")
            break


send_receive([1, 2, 3])
