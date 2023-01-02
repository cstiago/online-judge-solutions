# 1017 - Fuel Spent

def main():
    time = int(input())
    speed = int(input())

    distance = time * speed
    liters = distance / 12

    print(f'{liters:.3f}')

if __name__ == '__main__':
    main()