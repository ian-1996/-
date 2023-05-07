import time

# Recursive
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Dynamic programming
def fib_dynamic(n):
    fib_table = [0] * (n+1)
    fib_table[1] = 1
    for i in range(2, n+1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
    return fib_table[n]

#  maximum value of n 
def find_max_n():
    n = 0
    while True:
        try:
            fib_recursive(n+1)
        except:
            return n
        n += 1


def check_dynamic_crash(n):
    try:
        fib_dynamic(n+1)
        return False
    except:
        return True


max_n = find_max_n()
print(f"The maximum value of n that causes the computer to crash is {max_n}")


if check_dynamic_crash(max_n):
    print("The computer will still crash using dynamic programming")
else:
    print("The computer will not crash using dynamic programming")

