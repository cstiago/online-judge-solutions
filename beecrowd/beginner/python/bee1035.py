# 1035 - Selection Test 1

def main():
    a, b, c, d = [int(i) for i in input().split()]

    if b > c and d > a and (c + d) > (a + b) and (c, d > 0) and (a % 2) == 0:
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')

if __name__ == '__main__':
    main()