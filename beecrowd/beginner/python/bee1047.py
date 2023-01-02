# 1047 - Game Time with Minutes

def main():
    ih, im, fh, fm = [int(i) for i in input().split()]

    if ih == fh:
        hours = 24
        if im < fm:
            hours = 0
    elif ih < fh:
        hours = fh - ih
    elif ih > fh:
        hours = (24 - ih) + fh

    if im == fm:
        minutes = 0
    elif im < fm:
        minutes = fm - im
    elif im > fm:
        minutes = (60 - im) + fm
        hours -= 1

    print(f'O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)')

if __name__ == '__main__':
    main()