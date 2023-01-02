# 1040 - Average 3

def approved():
    return 'Aluno aprovado.'

def reproved():
    return 'Aluno reprovado.'

def main():
    n1, n2, n3, n4 = [float(i) for i in input().split()]

    average = round(((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10, 1)

    print(f'Media: {average}')

    if average >= 7.0:
        print(approved())
    elif average < 5.0:
        print(reproved())
    else:
        print('Aluno em exame.')
        
        exam = float(input())
        
        print(f'Nota do exame: {exam}')
        
        average = round((average + exam) / 2, 1)
        
        if average >= 5.0:
            print(approved())
        else:
            print(reproved())
        
        print(f'Media final: {average}')

if __name__ == '__main__':
    main()