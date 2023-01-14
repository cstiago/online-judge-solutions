# 1045 - Triangle Types

def main():
    sort = [float(i) for i in input().split()]
    sort.sort(reverse = True)

    a, b, c = sort

    if a >= (b + c):
        print('NAO FORMA TRIANGULO')
        
    else:
        if (a ** 2) == ((b ** 2) + (c ** 2)):
            print('TRIANGULO RETANGULO')
            
        else:
            if (a ** 2) > ((b ** 2) + (c ** 2)):
                print('TRIANGULO OBTUSANGULO')
            elif (a ** 2) < ((b ** 2) + (c ** 2)):
                print('TRIANGULO ACUTANGULO')
            
            if a == b == c:
                print('TRIANGULO EQUILATERO')
            elif (a == b != c) or (a != b == c) or (a == c != b):
                print('TRIANGULO ISOSCELES')

if __name__ == '__main__':
    main()