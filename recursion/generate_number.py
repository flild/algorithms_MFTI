import pprint

def generate_number(N: int, M: int, prefix=None):
    '''
    Генерирует все варианты перестановок цифр до N (с лидирующими незначищами нулями)
    длины М
    :param N: Колическтво чисел для перестановки, N<10
    :param M: Длина чисел на выходе
    :param prefix: Нужен для рекурсивной генирации, изначально None
    :return: Список всех чисел
    '''
    prefix = prefix or []
    if M == 0:
        print(*prefix,sep='')
        return
    for digit in range(N):
        if digit in prefix:
            continue
        prefix.append(digit)
        generate_number(N,M-1,prefix)
        prefix.pop()

generate_number(3,3)