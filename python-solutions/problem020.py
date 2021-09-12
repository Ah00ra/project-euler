def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def main(n):
    summ = 0
    for i in str(factorial(n)):
        summ += int(i)
    return summ


print(main(100))
