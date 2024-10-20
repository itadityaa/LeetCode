import time

fib_number = int(input("What Fibonacci number would you like to know? "))


def fib_dp(fib_number):
    fib_array = []
    if fib_number <= 1:
        return fib_number
    else:
        for num in range(fib_number + 1):
            if num <= 1:
                fib_array.append(num)
            else:
                fib_array.append(fib_array[num - 1] + fib_array[num - 2])
        return fib_array[fib_number]


start = time.time()
print(fib_dp(fib_number))
end = time.time()
print(end - start)
