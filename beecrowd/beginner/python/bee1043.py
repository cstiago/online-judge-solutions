# 1043 - Triangle

def main():
    a, b, c = [float(i) for i in input().split()]

    if (a + b) > c and (a + c) > b and (b + c) > a:
        perimetro = a + b + c
        
        print(f'Perimetro = {perimetro:.1f}')
    else:
        area = ((a + b) / 2) * c
        
        print(f'Area = {area:.1f}')

if __name__ == '__main__':
    main()