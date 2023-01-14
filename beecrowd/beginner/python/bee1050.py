# 1050 - DDD

def main():
    ddd = int(input())

    destinations = {
        61: 'Brasilia',
        71: 'Salvador',
        11: 'Sao Paulo',
        21: 'Rio de Janeiro',
        32: 'Juiz de Fora',
        19: 'Campinas',
        27: 'Vitoria',
        31: 'Belo Horizonte'
    }

    print(destinations.get(ddd, 'DDD nao cadastrado'))

if __name__ == '__main__':
    main()