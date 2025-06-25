from collections.abc import Awaitable
import time
from collections import deque
import asyncio


# ------------------ Event Loop Intro


def eventloop_simulator():
    sleeping = []
    ready = deque()

    def schedule_task(task, delay):
        deadline = time.time() + delay
        sleeping.append((deadline, task))

    # Schedule tasks
    schedule_task(lambda: print("Task 1 executed after 6s"), 6)
    schedule_task(lambda: print("Task 2 executed after 2s "), 2)
    schedule_task(lambda: print("Task 3 executed after 3s"), 3)

    while ready or sleeping:
        time.sleep(1)
        print("iterating...")
        if not ready:
            deadline, task = sleeping.pop()
            print(f"Popped {task}")
            delta = deadline - time.time()
            if delta < 0:
                print(f"Added {task}")
                ready.append(task)
            else:
                sleeping.append((deadline, task))

        while ready:
            task = ready.popleft()
            task()


# ------------------ Asyncio module


# A coroutine that simulates a long-running task
async def fetch_data(delay):
    print("Fetching data!")
    await asyncio.sleep(delay)  # simulate an network latency
    print("Data fetched")
    return {"data": "Some data"}


# Main coroutine (entry point)
async def main():
    print("Start main coroutine function")

    # `fetch_data` only returns Coroutine, it DOES NOT execute coroutines
    # Coroutines does not execute until is awaited
    task = fetch_data(3)

    # Coroutine is executed when it is awaited
    result = await task  # waits for `fetch_data` to complete
    print(f"Received result: {result}")
    print("End main coroutine")


asyncio.run(main())


# ------------------ Tests

# eventloop_simulator()
