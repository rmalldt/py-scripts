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


# ----- Using gather()


async def execute_concurrently_gather_values():
    # Run coroutines concurrently and gather their return values
    # Instead of creating task to run them concurrently, use `gather`
    # `gather` automatically runs the coroutine concurrently and gathers
    # the return values in the order the coroutines are passed.

    # `gather` does not handle Errors.
    # It does not cancel other coroutines if one of the coroutines fail.
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    for result in results:
        print(f"Received result: {result}")


# ----- Using TaskGroup


async def using_taskgroup():
    tasks = []

    # `asyncio.TaskGroup` is `Asynchronous context manager`
    # It executes all tasks in the TaskGroup and waits/blocks until their completion.
    async with asyncio.TaskGroup() as tg:
        for i, delay in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, delay))  # create task
            tasks.append(task)

    # Resume after all tasks in TaskGroup have completed
    print("All tasks completed")
    results = [task.result() for task in tasks]
    for result in results:
        print(f"Received result: {result}")


# ----- Using Futures


async def set_future_result(future, value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"Set future result to: {value}")


async def using_future():
    # Future is the placeholder for the future result of an asynchronous operation
    loop = asyncio.get_running_loop()  # get Event Loop
    future = loop.create_future()  # create future object

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future Result"))

    # Wait for future result
    result = await future
    print(f"Received future result: {result}")


# ----- Using Synchronization

# A shared variable
shared_resource = 0

# An asyncio Lock (mutex)
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource

    """
    `lock` is the `Asynchronous context manager`
       - It ensures that the `lock` is acquired and released automatically.
    
       - The critical section is the section that references the shared resource.
         Only one coroutine at a time should be allowed to execute crtical section
         meaning after a coroutine finishes executing the critical section only then
         other coroutine gets to execute the critical section.
    
       - This is done to prevent `Race condition` which happens when multiple
         coroutines execute the critical section which makes the state of
         shared resource indeterminate.
    """
    # Acquire lock
    async with lock:
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1  # modify the shared resource
        await asyncio.sleep(1)  # simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends
    # Release the lock


async def using_synchronization():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


# ----- Using Semaphore with Synchronization


async def access_resource(semaphore, resource_id):
    async with semaphore:
        print(f"Accessing resource: {resource_id}")
        await asyncio.sleep(1)  # simulate an IO operation
        print(f"Releasing resource: {resource_id}")


async def using_semaphore_synchronization():
    # Semaphore allows multiple coroutines to have access to the same object
    # at the same time.
    semaphore = asyncio.Semaphore(2)  # allow 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))


# ------------------ Tests


# eventloop_simulator()

# asyncio.run(create_coroutine_execute_synchronously())
# asyncio.run(create_task_execute_concurrently())

# asyncio.run(execute_concurrently_gather_values())
# asyncio.run(using_taskgroup())

# asyncio.run(using_future())

# asyncio.run(using_synchronization())
# asyncio.run(using_semaphore_synchronization())
