def smallest_prime_factor(n):
    for i in range(2, int(n**0.5)+1):
    	if n % i == 0:
            return i
    return n


def find_largest_prime_factor(number):
    while True:
        smallest_factor = smallest_prime_factor(number)

        if smallest_factor < number:
            number //= smallest_factor
        else:
            return number


print(find_largest_prime_factor(600851475143))
