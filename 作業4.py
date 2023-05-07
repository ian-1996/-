import time

#Recursive 
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Dynamic Programming 
def fib_dynamic(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_dynamic(n-1, memo) + fib_dynamic(n-2, memo)
    return memo[n]

# execution time
n_values = list(range(10, 101, 10))
recursive_times = []
dynamic_times = []

for n in n_values:
    #  recursive time
    start_time = time.time()
    fib_recursive(n)
    end_time = time.time()
    recursive_times.append(end_time - start_time)

    # dynamic programming time
    start_time = time.time()
    fib_dynamic(n)
    end_time = time.time()
    dynamic_times.append(end_time - start_time)

#results
import matplotlib.pyplot as plt

plt.plot(n_values, recursive_times, label='Pure Recursive')
plt.plot(n_values, dynamic_times, label='Dynamic Programming')
plt.xlabel('n')
plt.ylabel('Execution Time (Seconds)')
plt.title('Execution Time for Calculating Fibonacci Numbers')
plt.legend()
plt.show()
