# Урок  8 
########################### Задание 1#####################
#Написать функцию, которая умножает все элементы в произвольном списке .

massiv = [1, 2, 3, 4, 5]

def umnojenie(massiv):
    rez = 1
    for i in massiv:
        rez*=i
    print(rez)
umnojenie(massiv)
print('\n\n')


########################### Задание 2#####################
#Написать функцию для удаления всех дубликатов в произвольном массиве.

massiv = [1, 2, 3, 4, 5, 5, 5]
print(set(massiv))
print('\n\n')

########################### Задание 2#####################
#Написать функцию, которая берет 2 списка сравнивает их и если у них есть хотя бы один общей компонент, то выводит надпись TRUE.


def sravnenie():
    massiv1 = [1, 2, 3, 4, 5]
    massiv2 = [7, 6]

    massiv1.extend(massiv2)
    all = len(massiv1)
    end_all = len(set(massiv1))
    if all > end_all:
        return True
    else:
        return False


print(sravnenie())