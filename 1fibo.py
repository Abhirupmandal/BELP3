# Recursive Fibonacci using Memoization
def recursive_fib_memo(n, memo):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = recursive_fib_memo(n-1, memo) + recursive_fib_memo(n-2, memo)
    return memo[n]


# Simple Recursive Fibonacci
def recursive_fib(n):
    if n <= 1:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)


# Iterative Fibonacci
def non_recursive_fib(n):
    a, b = 0, 1
    print("\nNon-Recursive Method:")
    for _ in range(n):
        print(a, end="  ")
        a, b = b, a+b


n = int(input("Enter number of terms: "))
memo = {}

# Display menu
print("\n1. Non Recursive Method")
print("2. Recursive Method")
print("3. Recursive Method (Memoization)")
print("4. Exit")

while True:
    choice = int(input("\nEnter Choice: "))

    if choice == 1:
        non_recursive_fib(n)

    elif choice == 2:
        print("\nRecursive Method:")
        for i in range(n):
            print(recursive_fib(i), end="  ")

    elif choice == 3:
        print("\nRecursive Method (Memoization):")
        for i in range(n):
            print(recursive_fib_memo(i, memo), end="  ")

    elif choice == 4:
        print("Program Exited.")
        break

    else:
        print("Invalid Choice!")
        