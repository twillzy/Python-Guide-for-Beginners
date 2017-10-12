# Fibonacci Number is equal to 1 minus itself plus 2 minus itself:
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def fib_efficient(n):
    F = [0, 1]
    if n <= 1:
        return F[n]
    else:
        for i in range(2, n + 1):
            F.append(F[i-1] + F[i-2])
        return F[n]

# Showing the first 10 in the sequence
for i in range(10):
    print(fib(i))
