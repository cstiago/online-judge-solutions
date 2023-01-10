# 1021 - Banknotes and Coins

def output(quantity, value, currency):
    return f'{int(quantity)} {"nota" if currency else "moeda"}(s) de R$ {value:.2f}'

def main():
    notes = (100, 50, 20, 10, 5, 2)
    coins = (1, 0.50, 0.25, 0.10, 0.05, 0.01)

    notes_qty, coins_qty = {}, {}

    value = float(input())

    print('NOTAS:')

    for i in range(len(notes)):
        notes_qty[i] = value // notes[i]
        value -= notes_qty[i] * notes[i]
    
        print(output(notes_qty[i], notes[i], 1))
        
    print('MOEDAS:')

    for i in range(len(coins)):
        coins_qty[i] = value / coins[i]
        value -= int(coins_qty[i]) * coins[i]
        
        print(output(round(coins_qty[i], 2), coins[i], 0))

if __name__ == '__main__':
    main()