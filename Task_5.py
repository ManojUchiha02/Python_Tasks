import threading
import time
import queue
import sys


data_queue = queue.Queue()


def producer_thread(id):
    for i in range(1, 3):
        item = f"Item {id}-{i}"
        data_queue.put(item)
        print(f"Producer {id} produced {item}")
        time.sleep(1)


def consumer_thread(id):
    while True:
        try:
            item = data_queue.get(timeout=2)
            print(f"Consumer {id} consumed {item}")
            data_queue.task_done()
        except queue.Empty:
            print(f"Consumer {id} timed out.")
            break


def Mu_Pr_Cns():
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))

    producer_threads = []
    consumer_threads = []

    for i in range(1, num_producers+1):
        thread = threading.Thread(target=producer_thread, args=(i,))
        producer_threads.append(thread)
        thread.start()

    for i in range(1, num_consumers+1):
        thread = threading.Thread(target=consumer_thread, args=(i,))
        consumer_threads.append(thread)
        thread.start()

    for producer in producer_threads:
        producer.join()

    # Insert None values to signal consumers to stop
    for i in range(num_consumers):
        data_queue.put(None)

    for consumer in consumer_threads:
        consumer.join()


Mu_Pr_Cns()
