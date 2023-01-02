# 1051 - Taxes

def main():
    salary = float(input())

    if not (salary >= 0.00 and salary <= 2000.00):
        if salary > 2000.00 and salary <= 3000.00:
            taxes = 0.08
            value = (salary - 2000.00) * taxes
        
        elif salary > 3000.00 and salary <= 4500.00:
            taxes = 0.18
            value = ((salary - 3000.00) * taxes) + 80.00
            
        elif salary > 4500.00:
            taxes = 0.28
            value = ((salary - 4500.00) * taxes) + 350.00

        print(f'R$ {value:.2f}')

    else:
        print('Isento')

if __name__ == '__main__':
    main()