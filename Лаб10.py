# Вводим значение N с клавиатуры
N = int(input("Введите количество целых чисел: "))# Вводим значение N с клавиатуры.
# Вводим целые числа с клавиатуры и записываем их в файл file1_NN.txt
with open(f"file1_NN.txt", "w") as file1:# Открываем файл file1_NN.txt в режиме записи.
    for i in range(N):# С помощью цикла for вводим целые числа с клавиатуры и записываем их в файл.
        num = int(input(f"Введите {i+1}-е число: ")) # Вводим целые числа с клавиатуры
        file1.write(f"{num}\n") # Записываем числа в файл file1_NN.txt

def is_perfect_number(num): # Определяем функцию is_perfect_number, которая проверяет число на совершенность.
    divisors_sum = 0
    for i in range(1, num):# Запускаем цикл от 1 до num
        if num % i == 0:# Если num делится на i без остатка
            divisors_sum += i# Добавляем i к сумме делителей
    if divisors_sum == num: # Если сумма делителей равна num
        return True# Возвращаем True
    return False# Возвращаем False

# Читаем числа из файла file1_NN.txt и записываем совершенные числа в файл file2_NN.txt
with open(f"file1_NN.txt", "r") as file1:# Открываем файл file1_NN.txt в режиме чтения
    num_list = file1.readlines()# Считываем все строки из файла
with open(f"file2_NN.txt", "w") as file2: # Открываем файл file2_NN.txt в режиме записи
    for i in range(len(num_list)):# Запускаем цикл от 0 до длины списка num_list
        num = int(num_list[i])# Преобразуем элемент списка в целое число
        if is_perfect_number(num):# Проверяем, является ли число совершенным
            file2.write(f"{num}\n")# Записываем совершенное число в файл file2_NN.txt