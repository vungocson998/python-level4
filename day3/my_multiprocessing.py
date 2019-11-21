import multiprocessing
import concurrent.futures #Easier to switch between multithreading and multiprocessing
import time

# Performance counter for benchmarking
start1 = time.perf_counter()

def do_something(seconds):
    time.sleep(seconds)
    return f"Done sleeping in {seconds} second(s) ..."

# Round1: Basic test
p1 = multiprocessing.Process(target=do_something, args=[1.5])
p2 = multiprocessing.Process(target=do_something, args=[1.5])
p1.start()
p2.start()

# Make processes complete before execute codes below
p1.join()
p2.join()
finish1 = time.perf_counter()
print(f"Round1: Finished in {round(finish1-start1, 2)} second(s)")

# Round2: Testing with loop
processes = []
start2 = time.perf_counter()
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish2 = time.perf_counter()
print(f"Round2: Finished in {round(finish2-start2, 2)} second(s)")

# Round3: Using concurrent.futures
start3 = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
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