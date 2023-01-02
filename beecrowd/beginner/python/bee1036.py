# 1036 - Bhaskara's Formula

import math

def main():
    a, b, c = [float(i) for i in input().split()]

    try:
        d = math.sqrt((b ** 2) - (4 * a * c))
        
        r1 = (-b + d) / (2 * a)
        r2 = (-b - d) / (2 * a)
        
        print(f'r1 = {r1:.5f}')
        print(f'r2 = {r2:.5f}')
        
    except:
        print('Impossivel calcular')

if __name__ == '__main__':
    main()