# 1014 - Consumption

def main():
    x = int(input())
    y = float(input())

    consumption = float(x / y)

    print(f'{consumption:.3f} km/l')

if __name__ == '__main__':
    main()