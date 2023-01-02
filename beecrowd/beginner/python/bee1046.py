# 1046 - Game Time

def main():
    start, end = [int(i) for i in input().split()]

    if start == end:
        duration = 24
    elif start < end:
        duration = end - start
    elif start > end:
        duration = (24 - start) + end

    print(f'O JOGO DUROU {duration} HORA(S)')

if __name__ == '__main__':
    main()