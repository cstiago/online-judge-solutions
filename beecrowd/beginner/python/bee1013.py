# 1013 - The Greatest

def greater(a, b):
    return int((a + b + abs(a - b)) / 2)

def main():
    v1, v2, v3 = input().split()
    v1 = int(v1)
    v2 = int(v2)
    v3 = int(v3)

    greatest = greater(v1, v2)
    greatest = greater(greatest, v3)

    print(f'{greatest} eh o maior')

if __name__ == '__main__':
    main()