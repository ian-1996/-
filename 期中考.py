import random
import timeit
import matplotlib.pyplot as plt


def binary_search(S, x):
    sorted(S)
    low, high = 0, len(S) - 1
    while low <= high:
        mid = (low + high) // 2
        if S[mid] == x:
            return True
        elif S[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
        return False

def linear_search(S, x):
    
    for i in range(len(S)):
        if S[i] == x:
            return True
    return False

def fibonacci_search(S, x):
    sorted(S)
    F = [1, 1]
    while F[-1] < len(S):
        F.append(F[-1] + F[-2])
        offset = 0
        while F:
            i = min(offset + F[-2], len(S) - 1)
            if x > S[i]:
                F.pop()
                offset = i
            elif x < S[i]:
                    F.pop(-2)
            else:
                        return True
            return False

binary_average_times = []
linear_average_times = []
fibonacci_average_times = []


for n in range(100, 10000, 10):  
    # 生成一個陣列S包含n個隨機整數
    S = [random.randint(100, 10000) for _ in range(n)]
    # 要查找的整數x
    x = random.randint(100, 10000)
    
    

    # Linear執行時間
    t_linear = timeit.timeit(lambda: [linear_search(S, x) for _ in range(5)], number=1)

    # Binary執行時間
    t_binary = timeit.timeit(lambda: [binary_search(S, x) for _ in range(5)], number=1)

    # Fibonacci 的執行時間
    t_fibonacci = timeit.timeit(lambda: [fibonacci_search(S, x) for _ in range(5)], number=1)
    # 計算平均執行時間
    average_time_linear = t_linear*1e3 / 5 
    average_time_binary = t_binary*1e3 / 5
    average_time_fibonacci = t_fibonacci*1e3  / 5  
    linear_average_times.append(average_time_linear)
    binary_average_times.append(average_time_binary)
    fibonacci_average_times.append(average_time_fibonacci)
    print(f"Average execution time of linear search: {average_time_linear:.6f} microseconds")
    print(f"Average execution time of binary search: {average_time_binary:.6f} microseconds")
    print(f"Average execution time of Fibonacci search: {average_time_fibonacci:.6f} microseconds")


#折線圖
plt.plot(range(len(binary_average_times)), binary_average_times, label='Binary Search')
plt.plot(range(len(linear_average_times)), linear_average_times, label='Linear Search')
plt.plot(range(len(fibonacci_average_times)), fibonacci_average_times, label='Fibonacci Search')
plt.xlabel('List Size (n)')
plt.ylabel('Average Execution Time (microseconds)')
plt.title('Binary vs Linear vs Fibonacci Search Performance')
plt.legend()
plt.show()



