# 1048 - Salary Increase

def main():
    salary = float(input())

    if salary >= 0 and salary <= 400.00:
        rate = 0.15
    elif salary > 400.00 and salary <= 800.00:
        rate = 0.12
    elif salary > 800.00 and salary <= 1200.00:
        rate = 0.10
    elif salary > 1200.00 and salary <= 2000.00:
        rate = 0.07
    elif salary > 2000.00:
        rate = 0.04

    increase = salary * rate
    new_salary = salary + increase

    print(f'Novo salario: {new_salary:.2f}')
    print(f'Reajuste ganho: {increase:.2f}')
    print(f'Em percentual: {int(rate * 100)} %')

if __name__ == '__main__':
    main()