from math import sqrt

def rotation(n):
    n = str(n)
    output = []
    for i in range(len(n)):
        output.append(n[i:] + n[:i])
    return output



def is_prime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def is_circular_prime(n):
    n = str(n)
    flag = True
    for r in rotation(n):
        if not is_prime(r):
            flag = False
    return flag


count = 0
for i in range(2, 1000000):
    if is_circular_prime(i):
        count += 1

print(count)



