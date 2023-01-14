# 1019 - Time Conversion

def main():
    time = int(input())

    hours = time // 3600
    time -= hours * 3600
    minutes = time // 60
    time -= minutes * 60
    seconds = time

    print(f'{hours}:{minutes}:{seconds}')

if __name__ == '__main__':
    main()