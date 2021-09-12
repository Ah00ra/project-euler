def main(a, b):
    ans = a ** b
    summ = 0
    for i in str(ans):
        summ += int(i)
    return summ


print(main(2, 1000))
