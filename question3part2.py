import time

# Factorial function
def factorial(n):
    result = 1               # 1 primitive operation (assignment)
    for i in range(1, n+1):  # Loop runs n times
        result = result * i  # 2 primitive operations (multiplication + assignment)
    return result            # 1 primitive operation



def singlethread_factorial_test():
    rounds = 10
    times = []
    print("Singlethreading")
    for r in range(1, rounds + 1):
        start = time.time_ns()

        time.sleep(0.1) # simulate waiting for I/O / network / disk
        factorial(50)

        time.sleep(0.1) # simulate waiting for I/O / network / disk
        factorial(100)

        time.sleep(0.1) # simulate waiting for I/O / network / disk
        factorial(200)

        end = time.time_ns()
        T = end - start
        times.append(T)

        print(f"Round {r}: Time Elapsed (T) = {T} ns")

    # Average time over 10 rounds
    avg_time = sum(times) / rounds
    print("\n-------------------------------------------")
    print("Average Time over 10 rounds:", avg_time, "ns")
    print("-------------------------------------------")


if __name__ == "__main__":
    singlethread_factorial_test()
