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


# eventloop_simulator()

# ------------------ Asyncio module


# A coroutine that simulates a long-running task
async def fetch_data(id, delay):
    print("Fetching data!")
    await asyncio.sleep(delay)  # simulate an network latency
    print(f"Data fetched, id: {id}")
    return {"id": {id}, "data": f"Data from coroutine {id}"}


# ----- Create coroutine


async def create_coroutine_execute_synchronously():
    print("Start main coroutine function")

    # `fetch_data` only returns Coroutine, it DOES NOT execute coroutines
    # Coroutines does not execute until is awaited
    # Coroutine is executed when it is awaited
    coroutine1 = fetch_data(1, 2)
    coroutine2 = fetch_data(2, 2)

    # These coroutines are executed synchronously
    result1 = await coroutine1  # waits for `fetch_data` to complete
    print(f"Received result: {result1}")

    # This coroutine is ONLY executed only when `coroutine1` completes
    result2 = await coroutine2  # waits for `fetch_data` to complete
    print(f"Received result: {result2}")

    print("End main coroutine")


# asyncio.run(create_coroutine_execute_synchronously())


# ----- Create task


async def create_task_execute_concurrently():
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    # All of the tasks are executed concurrently unlike coroutines
    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)


# asyncio.run(create_task_execute_concurrently())

# ----- Using gather()


async def execute_concurrently_gather_values():
    # Run coroutines concurrently and gather their return values
    # Instead of creating task to run them concurrently, use `gather`
    # `gather` automatically runs the coroutine concurrently and gathers
    # the return values in the order the coroutines are passed
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    for result in results:
        print(f"Received result: {result}")


asyncio.run(execute_concurrently_gather_values())
