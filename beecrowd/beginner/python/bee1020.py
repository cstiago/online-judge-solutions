# 1020 - Age in Days

def main():
    age = int(input())

    years = age // 365
    age -= years * 365
    months = age // 30
    age -= months * 30
    days = age

    print(f'{years} ano(s)')
    print(f'{months} mes(es)')
    print(f'{days} dia(s)')

if __name__ == '__main__':
    main()