# 1012 - Area

def triangle(a, c):
    return (a * c) / 2

def circle(PI, c):
    return PI * (c ** 2)

def trapezium(a, b, c):
    return ((a + b) / 2) * c

def square(b):
    return b ** 2

def rectangle(a, b):
    return a * b

def main():
    PI = 3.14159

    a, b, c = input().split()
    a = float(a)
    b = float(b)
    c = float(c)

    print(f'TRIANGULO: {triangle(a, c):.3f}')
    print(f'CIRCULO: {circle(PI, c):.3f}')
    print(f'TRAPEZIO: {trapezium(a, b, c):.3f}')
    print(f'QUADRADO: {square(b):.3f}')
    print(f'RETANGULO: {rectangle(a, b):.3f}')

if __name__ == '__main__':
    main()