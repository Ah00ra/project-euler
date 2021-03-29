def is_even(n):
    if n % 2 == 0:
        return True
    return False


def main():
    n1, n2 = 1, 2
    nth = n1 + n2
    summ = 0
    while n1 < 4000000:
            if is_even(n1):
                summ += n1
            n1, n2 = n2, nth
            nth = n1 + n2
    return summ


if __name__ == "__main__":
    print(main())
