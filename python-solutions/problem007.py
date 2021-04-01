def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    last_prime = 0
    num = 2
    counter = 1
    while counter <= 10001:
        if is_prime(num):
            last_prime = num
            counter += 1
        num += 1
    return last_prime


print(main())
