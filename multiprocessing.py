# Creating a pool of worker processes
from multiprocessing import Pool
def process_task(task):
    # Do some work here
    print("Task processed:", task)
if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)

# Using a queue to communicate between processes
def producer(queue):
    for i in range(10):
        queue.put(i)
def consumer(queue):
    while True:
        item = queue.get()
        print(item)
queue = multiprocessing.Queue()
p1 = multiprocessing.Process(target=producer, args=(queue,))
p2 = multiprocessing.Process(target=consumer, args=(queue,))
p1.start()
p2.start()

# Using a lock to synchronize access to shared resources
def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter.value += 1
        lock.release()
if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=increment, args=(counter, lock))
    p2 = multiprocessing.Process(target=increment, args=(counter, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Counter value:", counter.value)