def is_even(n):
    return n % 2 == 0


def count_chain(num):
    count = 1
    while num != 1:
        if is_even(num):
            num /= 2
            count += 1
        else:
            num = 3 * num + 1
            count += 1
    return count


def main():
    bigger_chain = 0
    answer = 0
    for n in range(1, 1000001):
        if count_chain(n) > bigger_chain:
            bigger_chain = count_chain(n)
            answer = n 
    return answer


print(main())