from email import generator
import threading
from concurrent.futures import ThreadPoolExecutor, thread
import requests

# ------------------ Using threading.Thread


def print_numbers(num):
    for i in range(num):
        print(f"Thread {threading.get_ident()} is printing {i}")


def start_thread():
    print(f"Main thread: {threading.get_ident()}")

    # New thread takes:
    #   - target: The callable object to be invoked by run() which is called internally
    #   - args: List/tuple of arguments to be passed to the target
    t = threading.Thread(
        target=print_numbers,
        args=[
            3,
        ],
    )  # create new thread

    t.start()  # start the thread
    t.join()  # join the thread when the task is done


# ------------------ Subclassing Thread


class MyThread(threading.Thread):
    def run(self):
        print(f"Running in thread: {threading.get_ident()}")


def start_mythread():
    t = MyThread()
    t.start()
    t.join()


# ------------------ Using concurrent.futures.ThreadPoolExecutor


def squares(n):
    print(f"Running in thread: {threading.get_ident()} for {n}")
    return n * n


def start_thread_with_threadpoolexecutor():
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(squares, [1, 2, 3, 4, 5])
        print(list(results))


# ------------------ I/O bound operations vs CPU bound operations


# ----- I/O bound operations


# When HTTP request is made, the HTTP request calls down into C code (libcurl) that doesn't use
# Python objects, so the GIL is released while waiting for the server's response.
# Meanwhile, other threads can acquire the GIL and execute Python code.
def get_statuscode():
    print(f"Main thread: {threading.get_ident()}")
    urls = ["https://www.kemper-amps.com/"]

    def fetch(url):
        print(f"fetch running in thread {threading.get_ident()}")
        return requests.get(url).status_code

    with ThreadPoolExecutor() as executor:
        results = executor.map(fetch, urls)
        print(list(results))


# ----- CPU bound operations


def compute(thread_num):
    print(f"Thread number: {thread_num} running in thread: {threading.get_ident()}")
    res = sum(i * i for i in range(10**5))
    print(f"Thread number {thread_num} result: {res}")


def run_multiplethreads():
    threads = [threading.Thread(target=compute, args=(i,)) for i in range(4)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


# ------------------ Tests


# start_thread()
# start_mythread()
# start_thread_with_threadpoolexecutor()

get_statuscode()
# run_multiplethreads()
