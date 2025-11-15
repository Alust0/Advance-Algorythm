import threading
import time

# Factorial function
def factorial(n):
    result = 1               # 1 primitive operation (assignment)
    for i in range(1, n+1):  # Loop runs n times
        result = result * i  # 2 primitive operations (multiplication + assignment)
    return result            # 1 primitive operation



# Thread target wrapper that records its own start + end time
class FactorialThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.start_time = 0
        self.end_time = 0

    def run(self):
        # record when this thread starts its work
        self.start_time = time.time_ns()

        time.sleep(0.1)  # simulate waiting for I/O / network / disk
        factorial(self.n)

        # record when this thread finishes its work
        self.end_time = time.time_ns()


# Perform 10 rounds of timing
def multithread_factorial_test():
    rounds = 10
    times = []
    print("Mutlitreading")
    for r in range(1, rounds + 1):
        # Create threads for 50!, 100!, 200!
        t1 = FactorialThread(50)
        t2 = FactorialThread(100)
        t3 = FactorialThread(200)

        # Global start
        global_start = time.time_ns()

        # Start all threads
        t1.start()
        t2.start()
        t3.start()

        # Wait for completion
        t1.join()
        t2.join()
        t3.join()

        # Determine global end = last thread to finish
        global_end = max(t1.end_time, t2.end_time, t3.end_time)

        # Total time T for this round
        T = global_end - global_start
        times.append(T)

        print(f"Round {r}: Time Elapsed (T) = {T} ns")

    # Average time over 10 rounds
    avg_time = sum(times) / rounds
    print("\n-------------------------------------------")
    print("Average Time over 10 rounds:", avg_time, "ns")
    print("-------------------------------------------")


if __name__ == "__main__":
    multithread_factorial_test()
