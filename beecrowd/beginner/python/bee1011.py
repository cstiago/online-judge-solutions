# 1011 - Sphere

def main():
    PI = 3.14159

    r = float(input())

    v = float(4/3) * PI * (r ** 3)

    print(f'VOLUME = {v:.3f}')

if __name__ == '__main__':
    main()