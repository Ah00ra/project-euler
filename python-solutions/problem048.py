def main():
    summ = 0
    for i in range(1, 1001):
        summ += i ** i
    last_ten_digits = str(summ)[-10:]
    return last_ten_digits
    

if __name__ == "__main__":
    print(main())