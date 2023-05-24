import time
import random
import matplotlib.pyplot as plt

# Algorithm 1: Brute-Force Algorithm
def matrix_chain_multiplication_brute_force(P, i, j):
    if i == j:
        return 0, f'A{i}'
    
    min_cost = float('inf')
    best_order = ''
    
    for k in range(i, j):
        left_cost, left_order = matrix_chain_multiplication_brute_force(P, i, k)
        right_cost, right_order = matrix_chain_multiplication_brute_force(P, k + 1, j)
        cost = left_cost + right_cost + P[i-1] * P[k] * P[j]
        
        if cost < min_cost:
            min_cost = cost
            best_order = f'({left_order})({right_order})'
    
    return min_cost, best_order

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
    
    return m[0][n-1], construct_optimal_order(s, 1, n)

def construct_optimal_order(s, i, j):
    if i == j:
        return f'A{i}'
    else:
        k = s[i-1][j-1]
        return f'({construct_optimal_order(s, i, k)})({construct_optimal_order(s, k+1, j)})'

# Generate input sizes for testing
input_sizes = list(range(1, 21))
execution_times_brute_force = []
execution_times_dynamic = []
optimal_costs = []
optimal_orders = []

for n in input_sizes:
    P = [random.randint(1, 50) for _ in range(n + 1)]  # Generating random input
    
    # Brute-Force Algorithm
    start_time = time.time()
    cost, order = matrix_chain_multiplication_brute_force(P, 1, n)
    end_time = time.time()
    execution_time_brute_force = end_time - start_time
    execution_times_brute_force.append(execution_time_brute_force)
    optimal_costs.append(cost)
    optimal_orders.append(order)
    
    # Dynamic Programming Algorithm
    start_time = time.time()
    cost, order = matrix_chain_multiplication_dynamic(P)
    end_time = time.time()
    execution_time_dynamic = end_time - start_time
    execution_times_dynamic.append(execution_time_dynamic)

    # Printing optimal cost and order for each input size
    print(f"Input size: {n}")
    print(f"Optimal cost: {cost}")
    print(f"Optimal order: {order}")
    print()

# Plotting the execution times
plt.plot(input_sizes, execution_times_brute_force, label='Brute Force')
plt.plot(input_sizes, execution_times_dynamic, label='Dynamic Programming')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Comparison')
plt.legend()
plt.show()
