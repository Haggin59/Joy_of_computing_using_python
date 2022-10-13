def factorial(n):
    if n == 1:
        return n
    elif n>1:
        return n*factorial(n-1)
    else:
        print("not defined")

print(factorial(6))