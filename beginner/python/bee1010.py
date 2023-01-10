# 1010 - Simple Calculate

def main():
    product = list()

    for i in range(0, 2):
        code, units, price = input().split()
        product.append([int(code), int(units), float(price)])

    value = (product[0][1] * product[0][2]) + (product[1][1] * product[1][2])

    print(f'VALOR A PAGAR: R$ {value:.2f}')

if __name__ == '__main__':
    main()