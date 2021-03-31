# shotest way
# a = sum(i for i in range(1, 101))
# b = sum(i**2 for i in range(1, 101))
# print(a**2 - b)

def sum_of_squares(n):
    sum_squares = 0
    for i in range(1, n+1):
        sum_squares += i ** 2
    return sum_squares


def square_of_sum(n):
    simple_sum = 0
    for i in range(1, n+1):
        simple_sum += i
    return simple_sum ** 2


answer = square_of_sum(100) - sum_of_squares(100)
print(answer)
