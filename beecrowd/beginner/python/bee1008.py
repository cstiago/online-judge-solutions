# 1008 - Salary

def main():
    number = int(input())
    hours = int(input())
    amount = float(input())

    salary = hours * amount

    print(f'NUMBER = {number}')
    print(f'SALARY = U$ {salary:.2f}')

if __name__ == '__main__':
    main()