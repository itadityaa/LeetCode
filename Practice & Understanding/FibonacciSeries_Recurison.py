import time

fib_number = int(input("What Fibonacci number would you like to know? "))


def fibrecurison(fibo_number):
    if fibo_number == 0 or fibo_number == 1:
        return fibo_number
    else:
        return fibrecurison(fibo_number - 2) + fibrecurison(fibo_number - 1)


start = time.time()
print(fibrecurison(fib_number))
end = time.time()
print(end - start)