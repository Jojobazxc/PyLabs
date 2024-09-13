import random


def length_generate(number: int):
    """
    Написать функцию, которая принимает целое число
    и спомощью генераторного выражения создает и
    возвращает новый список случайных чисел с длиной
    входящего числа
    """
    length_number = int(len(str(number)))
    mixed_list = [random.choice([random.randint(0, 100), random.uniform(0, 100)]) for _ in range(length_number)]
    return mixed_list


random_list = length_generate(554437)
print(random_list)
