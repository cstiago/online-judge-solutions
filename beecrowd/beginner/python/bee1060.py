# 1060 - Positive Numbers

def main():
    numbers = []
    positive = 0

    for i in range(6):
        numbers.append(float(input()))
        
        if numbers[i] > 0:
            positive += 1

    print(f'{positive} valores positivos')

if __name__ == '__main__':
    main()