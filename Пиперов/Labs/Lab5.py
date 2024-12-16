def get_longest_word(path):
    """
    Написать программу, которая принимает путь к файлу и возвращает наиболе длинное слово
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            words = file.read().split()
            longest_word = max(words, key=len)
            return longest_word
    except FileNotFoundError:
        return "Файл не найден"


file_path = "C:\\Users\\Student\\Desktop\\Пиперов\\Labs\\Lab5.txt"
print(get_longest_word(file_path))
