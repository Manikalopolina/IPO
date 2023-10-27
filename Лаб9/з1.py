def natural_ch(num):
    '''
    Проверяет, является ли число простым.
    Аргументы:
    - num: int - число для проверки.
    Возвращает:
    - bool - True, если число простое, False в противном случае.'''
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def find_prime_palindromes(n):
    '''
    Находит все простые числа, не превосходящие n, двоичная запись которых является палиндромом.
    Аргументы:
    - n: int - максимальное число для проверки.
    Возвращает:
    - list[int] - список простых чисел, удовлетворяющих условию палиндрома.'''
    prime_palindromes = []
    for num in range(2, n + 1):
        b= bin(num)[2:]
        if b== b[::-1] and natural_ch(num):
            prime_palindromes.append(num)
    return prime_palindromes



