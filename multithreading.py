# Creating multiple threads
import threading
def thread_task(task):
    # Do some work here
    print("Task processed:", task)
if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threads = []
    for task in tasks:
        thread = threading.Thread(target=thread_task, args=(task,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Using a lock to synchronize access to shared resources
import threading
def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter += 1
        lock.release()
if __name__ == '__main__':
    counter = 0
    lock = threading.Lock()
    threads = []
    for i in range(2):
        thread = threading.Thread(target=increment, args=(counter, lock))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print("Counter value:", counter)