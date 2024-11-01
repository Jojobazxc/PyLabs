from PIL import Image
import os


def convert_to_ico(image_path):
    try:
        img = Image.open(image_path)

        base_path, _ = os.path.splitext(image_path)

        ico_path = base_path + ".ico"

        img.save(ico_path, format="ICO")

        print(f"Изображение успешно сохранено как {ico_path}")

    except FileNotFoundError:
        print("Файл не найден")


convert_to_ico("C:/Users/Student/Desktop/Пиперов/Labs/123.PNG")
