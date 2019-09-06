def fibonacci():
    size = int(input("Enter the number of Fibonacci numbers to generate: "))
    i = 1

    if size == 1:
        fib = [1]
    elif size == 2:
        fib = [1,1]
    elif size > 2:
        fib = [1,1]
        while i < size - 1:
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib



print(fibonacci())
