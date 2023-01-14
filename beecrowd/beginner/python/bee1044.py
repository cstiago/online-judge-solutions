# 1044 - Multiples

def main():
    a, b = [int(i) for i in input().split()]

    if (a % b) == 0 or (b % a) == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if __name__ == '__main__':
    main()