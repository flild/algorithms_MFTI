def insert_sort(mass):
    '''
    Сортировка массива вставками по возрастанию
    :param mass:
        mass - Ссылка на массив
    :return:
        None, так как менеяет исходный массив
    '''
    for top in range(1, len(mass)):
        cur = top
        while cur > 0 and mass[cur] < mass[cur - 1]:
            mass[cur], mass[cur - 1] = mass[cur - 1], mass[cur]
            cur -= 1


def choise_sort(mass):
    '''
    Сортировка выбором по возрастанию
    :param mass:
        mass - ссылка на массив
    :return:
        None
        Меняет исходный массив
    '''
    for pos in range(0, len(mass) - 1):
        for el in range(pos + 1, len(mass)):
            if mass[el] < mass[pos]:
                mass[el], mass[pos] = mass[pos], mass[el]


def bubble_sort(mass):
    '''
    Сортировка методом пузырька по возрастанию
    :param mass:
        mass - ссылка на массив
    :return:
        None, меняет исходный массив
    '''
    for bypass in range(1, len(mass) - 1):
        for el2 in range(0, len(mass) - bypass):
            if mass[el2] > mass[el2 + 1]:
                mass[el2], mass[el2 + 1] = mass[el2 + 1], mass[el2]


def test1_insert_sort():
    mass = [4, 2, 5, 1, 3]
    insert_sort(mass)
    assert mass == [1, 2, 3, 4, 5]


def test2_choise_sort():
    mass = [4, 2, 5, 1, 3]
    choise_sort(mass)
    assert mass == [1, 2, 3, 4, 5]


def test3_bubble_sort():
    mass = [4, 2, 5, 1, 3]
    bubble_sort(mass)
    assert mass == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    pass
