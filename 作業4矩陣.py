import time
import matplotlib.pyplot as plt

# Algorithm 1: Brute-Force Algorithm
def matrix_chain_multiplication_brute_force(P, i, j):
    if i == j:
        return 0
    
    min_cost = float('inf')
    
    for k in range(i, j):
        cost = matrix_chain_multiplication_brute_force(P, i, k) + \
               matrix_chain_multiplication_brute_force(P, k + 1, j) + \
               P[i-1] * P[k] * P[j]
        
        min_cost = min(min_cost, cost)
    
    return min_cost

# Algorithm 2: Dynamic Programming Algorithm
def matrix_chain_multiplication_dynamic(P):
    n = len(P) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i-1][j-1] = float('inf')
            
            for k in range(i, j):
                cost = m[i-1][k-1] + m[k][j-1] + P[i-1] * P[k] * P[j]
                
                if cost < m[i-1][j-1]:
                    m[i-1][j-1] = cost
                    s[i-1][j-1] = k
    
    return m[0][n-1], s

# Generate input sizes for testing
input_sizes = list(range(1, 21))
execution_times_brute_force = []
execution_times_dynamic = []

for n in input_sizes:
    P = [10] * (n + 1)  # Generating a simple input where all dimensions are 10
    start_time = time.time()
    matrix_chain_multiplication_brute_force(P, 1, n)
    end_time = time.time()
    execution_time_brute_force = end_time - start_time
    execution_times_brute_force.append(execution_time_brute_force)
    
    start_time = time.time()
    matrix_chain_multiplication_dynamic(P)
    end_time = time.time()
    execution_time_dynamic = end_time - start_time
    execution_times_dynamic.append(execution_time_dynamic)

# Plotting the execution times
plt.plot(input_sizes, execution_times_brute_force, label='Brute Force')
plt.plot(input_sizes, execution_times_dynamic, label='Dynamic Programming')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Comparison')
plt.legend()
plt.show()

