def main():
    answer = sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0))
    return answer


if __name__ == "__main__":
    print(main())
