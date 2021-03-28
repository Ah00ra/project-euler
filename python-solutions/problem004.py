def is_palindromic(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False


def main():
    lst = [i for i in range(100, 1000)]
    counter = 0
    answer = 0
    ans = 0
    while lst[counter] < 999:
        for index in range(len(lst)):
            ans = lst[counter] * lst[index]

            if is_palindromic(ans):
                if ans > answer:
                    answer = ans
        counter += 1
    return answer


if __name__ == "__main__":
    print(main())
