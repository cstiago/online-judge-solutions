# 1042 - Simple Sort

def main():
    sort = [int(i) for i in input().split()]
    numbers = list(sort)

    for i in range(len(sort)):
        for j in range(len(sort) - 1):
            if sort[j] > sort[j + 1]:
                sort[j] += sort[j + 1]
                sort[j + 1] = sort[j] - sort[j + 1]
                sort[j] -= sort[j + 1]

    for i in sort:
        print(i)

    print()

    for i in numbers:
        print(i)

if __name__ == '__main__':
    main()