# Задача 1

#Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
#Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
#Входные данные - строка из чисел, разделенная пробелами.
#Выходные данные - количество пар.
#Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.
numbers_string = input("Введите строку разделенную пробелами:")
def pairs(numbers_string):
    pairs = 0
    numbers_string = (numbers_string.split())
    numbers_string.sort()
    for i in range(len(numbers_string)):
        for j in range(i + 1, len(numbers_string)):
            if numbers_string[i] == numbers_string[j]:
                pairs += 1
    return pairs
pairs(numbers_string)

# Задача 2

#Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
#Элементы нужно выводить в том порядке, в котором они встречаются в списке.
array = [str(i).strip() for i in input("Введите элементы списка:").split()]
def uniques(array):
    array_ = []
    for i in range(len(array)):
        one = array[0]
        if array[i] not in array_:
            array_.append(array[i])
    for i in range(1, len(array)):
        if one == array[i]:
            array_.pop(0)
            break
    uniques = array_
    return uniques
uniques(array)

# Задача 3

# Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
# Верните полученный список.
# Задача не проходит тест. Такой вариант решения мог бы быть, но всего с одним исправлением - item == 0 (см ответы)
array = [int(i) for i in input("Введите элементы списка:").split()]
def ordered_list(array):
    for i in range(len(array)):
        if array[i]==0:
            array.append(array[i])
            array.pop(i)
            print(array)
    return array
ordered_list(array)

# Задача 4

#Возмите кортеж `('a', 'b', 'c')`, И сделайте из него список.
in_tuple = tuple(input("Введите значения кортежа:"))
def tuple_to_list(in_tuple):
    print(in_tuple)
    lst = []
    lst = list(in_tuple)
    return lst
tuple_to_list(in_tuple)

# Задача 5

#Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию). can't call itself

a = int(input("Введите число а:"))
b = int(input("Введите число b:"))
def euclid(a,b):
    if a == 0 and b != 0:
        del_= 0
        del_f = b
    elif a != 0 and b == 0:
        del_=0
        del_f = a
    elif a > b:
        del_ = b
    elif b > a:
        del_ = a
    for i in range(1, del_ + 1):
        if (a % i == 0) and (b % i == 0):
            del_f = i
    return del_f
euclid(a,b)

# Задача 6

#Dictionaries
 #Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
    #Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
    #Входные данные
    #Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
    #В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    #Выходные данные
    #Для каждого из запроса выведите название страны, в котором находится данный город.
    #Пример данных:
    #Входные данные
    #2
    #Russia Moscow Petersburg Novgorod Kaluga
    #Ukraine Kiev Donetsk Odessa
    #3
    #Odessa
    #Moscow
    #Novgorod
    #Выходные данные
    #Ukraine
    #Russia
    #Russia
    #input_string = "2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Donetsk Odessa\n3\nOdessa\nMoscow\nNovgorod"
    #output_string = 'Ukraine\nRussia\nRussia'
    #country_map={}
    
input_string = int(input("Введите количество стран: "))
def cities(input_string):
    N = input_string
    country_map = {}
    citylist = []
    output_string = ""
    output_string = str(output_string)
    for i in range(N):
        country_city = input("Введите страну и ее города: ").split()
        country_map[country_city[0]] = country_city[1:]
    M = int(input("Введите количество городов: "))
    for j in range(M):
         citylist.append(input('Введите список городов: '))
    for city in citylist:
        for key in country_map: 
            if city in country_map[key]:
                output_string = output_string + key + "\n"
    return str(output_string)
cities(input_string)

# Задача 7
 
#Sets
    #Языки
    #Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
    #Входные данные
    #Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    #Пример входных данных:
    #3 # N количество школьников
    #2 # M1 количество языков первого школьника
    #Russian # языки первого школьника
    #English
    #3 # M2 количество языков второго школьника
    #Russian
    #Belarusian
    #English
    #3
    #Russian
    #Italian
    #French
    #Выходные данные
    #В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
    #Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
    #input_string = "3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench"
    #output_string = '1\nRussian\n5\nRussian\nFrench\nItalian\nEnglish\nBelarusian'
input_string = int(input("Введите количество школьников:"))
lst_set = []
def languages(input_string):
    N = input_string
    for i in range(1, N+1):
        lang_set = set()
        M = int(input(f"Количество языков которые знает {i}  школьник:"))
        for j in range(1, M+1):
            lang_set.add(str(input(f"Введите {j} язык {i} школьника :")))
        lst_set.append(lang_set)
    all_stud = set.intersection(*lst_set) #языки которые знают все ученики
    one_stud = set.union(*lst_set) # языки которые знает хотя бы одинученик
    print("Количество языков, которые знают все школьники", len(all_stud))
    all_stud = str(all_stud).strip("{}")
    print("Список таких языков", all_stud)
    print("Количество языков, которые знает хотя бы один школьник", len(one_stud))
    one_stud = str(all_stud).strip("{}")
    print("Список таких языков", one_stud)
    a = str(len(all_stud))
    b = str(len(one_stud))
    return a + "\n" + all_stud + "\n" + b + "\n" + one_stud
languages(input_string)

# Задача 8

#Generators
    #Генераторы списков
    #Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']. из ['x','y'] & ['y','z','v']
arr1 = list(str(input("Введите элементы списка:")).split()) 
arr2 = list(str(input("Введите элементы списка:")).split()) 
def list_gen(arr1, arr2):
    result = [(i+j) for i in arr1 for j in arr2]
    return result
list_gen(arr1, arr2)

# Задача 9

#Генераторы словарей
#Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до N, а значениями кубы этих чисел.

N = int(input("Введите максимальное значение ключа словаря:"))
def dict_gen(N):
    result = {int(el): el**3 for el in range(1, N + 1)}
    print(result)
    return result
dict_gen(N)

# Задача 10

#Кортежи
#Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.

N = int(input("Введите заданное число:"))
def multiplication_table(N):
    nums, table = [[f'{i*j}\t' for i in range(1, N+1)]  for j in range(1, N+1)], "" 
    for line in nums: table += ''.join(line) + '\n'
    print(table)
    return str(table)
multiplication_table(N)