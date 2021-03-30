import math


def main():
    answer = 1
    for i in range(1, 21):
        # math.lcm is available in python3.9+
        answer = math.lcm(answer, i)
        # you can use this in python3.x
        # answer *= i // math.gcd(i, answer)

    return answer


if __name__ == "__main__":
    print(main())
