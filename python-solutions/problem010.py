from math import sqrt


def main():
    def is_prime(n):
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
        else:
            return True


    return sum(i for i in range(2, 2000001) if is_prime(i))


if __name__ == '__main__':
    print(main())
