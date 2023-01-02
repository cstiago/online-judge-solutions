# 1049 - Animal

def main():
    filters = []
    search = ''

    classes = (
        ('vertebrado',
        'invertebrado'),
        ('ave',
        'mamifero',
        'inseto',
        'anelideo'),
        ('carnivoro',
        'onivoro',
        'herbivoro',
        'hematofago')
    )

    animals = {
        '000': 'aguia',
        '001': 'pomba',
        '011': 'homem',
        '012': 'vaca',
        '123': 'pulga',
        '122': 'lagarta',
        '133': 'sanguessuga',
        '131': 'minhoca'
    }

    for i in range(3):
        filters.append(input())

    for iteration, item in enumerate(classes):
        i = item.index(filters[iteration])
        search += str(i)
    
    print(animals[search])

if __name__ == '__main__':
    main()