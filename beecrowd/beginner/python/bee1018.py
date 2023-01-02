# 1018 - Banknotes

def output(quantity, banknote):
    return f'{quantity} nota(s) de R$ {banknote},00'

def main():
    banknotes = (100, 50, 20, 10, 5, 2, 1)
    quantity = {}
    value = int(input())

    print(value)

    for i in range(len(banknotes)):
        quantity[i] = value // banknotes[i]
        value -= quantity[i] * banknotes[i]
        
        print(output(quantity[i], banknotes[i]))

if __name__ == '__main__':
    main()