def gcd(a,b):
    '''
    Рекурсивно ищет НОД по алгоритму Евклида
    :param a: Первое число
    :param b: Второе число
    :return: НОД для обоих чисел
    '''
    if a == b:
        return a
    if a > b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)

#усовершенственный вид
def best_gcd(a,b):
    '''
    Рекурсивно ищет НОД по алгоритму Евклида
    :param a: Первое число
    :param b: Второе число
    :return: НОД для обоих чисел
    '''
    return a if b==0 else gcd(b,a%b)

def test1_gcd():
    assert gcd(15,9) == 3

def test2_gcd():
    assert gcd(17,121) == 1

def test3_gcd():
    assert gcd(20,10000) == 20

def test4_best_gcd():
    assert best_gcd(15,9) == 3

def test5_best_gcd():
    assert best_gcd(17,121) == 1

def test6_best_gcd():
    assert best_gcd(20,10000) == 20