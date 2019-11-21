# Synchronously running

# Concurrency: CPU tasks and IO tasks can be running at the same time

# Using thread is not actually running the code of different tasks at the same time
# Using thread you can run the code without waiting for IO tasks are completed

# Some program may run slower when using threading because of the cost when create and destroy different threads
# If the task is CPU bound, we may want using multi processing and run it in parallel instead
#
# Manual way: using threading module
import threading
# More easier and efficient way (Python > 3.2): using threads pool executor
import concurrent.futures
    


import time

# Performance counter for benchmarking
start1 = time.perf_counter()

def do_something(seconds):
    time.sleep(seconds)
    return f"Done sleeping in {seconds} second(s) ..."

# Round1: Basic test
t1 = threading.Thread(target=do_something, args=[1.5])
t2 = threading.Thread(target=do_something, args=[1.5])
t1.start()
t2.start()

# Make threads complete before execute codes below
t1.join()
t2.join()
finish1 = time.perf_counter()

print(f"Round1: Finished in {round(finish1-start1, 2)} second(s)")

# Round2: Testing with loop
threads = []
start2 = time.perf_counter()
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish2 = time.perf_counter()
print(f"Round2: Finished in {round(finish2-start2, 2)} second(s)")

# Round3: Using concurrent.futures
start3 = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    # You can use futures Object to check if it's running or it's done and it's result
    secs = [5,4,3,2,1]
    # Using list comprehension and submit method to run a loop of threads
    # Submit method return a future object
    results1 = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results1):
        print(f.result())

    # Using map() method, it return the result
    # map() method auto join our threads
    # And we will have a list of results in order of it started
    results2 = executor.map(do_something, secs)

    for result in results2:
        print(result)

finish3 = time.perf_counter()
print(f"Round3: Finished in {round(finish3-start3, 2)} second(s)")