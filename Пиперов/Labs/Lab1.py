from random import randint

#Написать функцию, которая принимает два
#целочисленных списка и возвращает True, если
#первые или последние элементы данных списков равны.
#Оба списка содержат 1 или более элементов
def is_last_equal(first_list: list[int], second_list: list[int]):
    if first_list[-1] == second_list[-1] or first_list[0] == second_list[0]:
        return True
    else:
        return False


result = False
while not result:
    length_of_list = int(input("Введите длину списка: "))
    if length_of_list == 0:
        print("Список не может быть пустым")
        continue
    list1 = []
    list2 = []

    for i in range(length_of_list):
        list1.append(randint(0, 10))
        list2.append(randint(0, 10))

    result = is_last_equal(list1, list2)
    print(f"Первый список: {list1}")
    print(f"Второй список: {list2}")
    print(result)

