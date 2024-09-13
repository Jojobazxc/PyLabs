def get_types_of_numbers(numbers: list) -> list:
    """Написать функцию, которая принимает
    список, состоящий из n элементов,
    и возвращает количество целых чисел
    и чисел с плавающей точкой"""
    count_float = 0
    count_int = 0
    for number in numbers:
        if type(number) is float:
            count_float += 1
        if type(number) is int:
            count_int += 1
    return [count_float, count_int]


numbers = [1, 1.1, 5, 5.5, 4, 3]
types_of_numbers = get_types_of_numbers(numbers)
print(f"Количество float: {types_of_numbers[0]}, Количество int: {types_of_numbers[1]}")