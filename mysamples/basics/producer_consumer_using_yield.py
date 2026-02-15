"""
Pipeline pattern:
1. Producer : To generate data
2. Coroutine: Receive data and send to the consumer
3. Consumer: Receives data from 2nd step
"""


def producer(inp_data):
    """Producer generator ONLY Send"""
    for val in inp_data:
        yield val


def coroutine(data_queue):
    """Send and Receive"""
    producer_obj = producer(data_queue)
    consumer_queue = consumer()
    next(consumer_queue)    #Priming the generator
    while True:
        try:
            produced_value = next(producer_obj)
            print("Sent", produced_value)
            consumer_queue.send(produced_value)
        except StopIteration:
            print("produced all the data")
            break


def consumer():
    """ONLY Receive"""
    try:
        while True:
            op = (yield)  # yield on RHS is consumer
            print("Received", op)
    except GeneratorExit:
        print("Consumed all the data")


coroutine([1, 2, 3])
