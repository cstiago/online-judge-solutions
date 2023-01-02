# 1009 - Salary with Bonus

def main():
    name = input()
    salary = float(input())
    sale = float(input())

    total = salary + (sale * 0.15)

    print(f'TOTAL = R$ {total:.2f}')

if __name__ == '__main__':
    main()