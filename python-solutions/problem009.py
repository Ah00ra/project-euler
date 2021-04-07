def main():
    ONE_THOUSAND = 1000
    for a in range(1, ONE_THOUSAND+1):
        for b in range(a + 1,  ONE_THOUSAND+1):
            c = ONE_THOUSAND - a - b
            if a * a + b * b == c * c:
                return a * b * c


if __name__ == "__main__":
    print(main())
