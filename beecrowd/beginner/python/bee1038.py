# 1038 - Snack

def main():
    x, y = [int(i) for i in input().split()]

    prices = (4.00, 4.50, 5.00, 2.00, 1.50)

    total = prices[x - 1] * y

    print(f'Total: R$ {total:.2f}')

if __name__ == '__main__':
    main()