import os


def create_dirs_and_files(structure: list, base_path="вставить путь к корневую папку"):
    """
    Написать функцию, которая принимает список списков и создает структуры влоденных директорий и текстовых файлов
    относительно входящего спсика, где наименованием директории будет являться номер вложенного списка, а наименованием
    файла значение элемента списка.
    """
    for i, item in enumerate(structure):
        if type(item) is list:
            dir_path = os.path.join(base_path, str(i))
            os.mkdir(dir_path)
            for item_1 in item:
                file_name = f"{item_1}.txt"
                file_path = os.path.join(base_path, os.path.join(dir_path, file_name))
                new_file = open(file_path, "w")
                new_file.write(str(item_1))
                new_file.close()

        else:
            file_name = f"{item}.txt"
            file_path = os.path.join(base_path, file_name)
            new_file = open(file_path, "w")
            new_file.write(str(item))
            new_file.close()


example_list = [2, [4, 5], 4, [3, 8]]
create_dirs_and_files(example_list)
