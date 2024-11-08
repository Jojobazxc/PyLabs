import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageGrab, ImageEnhance, ImageOps, ImageTk
import pyautogui


class ScreenShotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ScreenShotApp")
        self.image = None
        self.current_image = None
        self.create_widgets()

    def create_widgets(self):
        self.screenshot_button = tk.Button(self.root, text="Сделать скриншот", command=self.take_screenshot)
        self.screenshot_button.pack(pady=10)

        self.brightness_label = tk.Label(self.root, text="Яркость")
        self.brightness_label.pack()
        self.brightness_slider = tk.Scale(self.root, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL,
                                          command=self.adjust_brightness)
        self.brightness_slider.set(1.0)
        self.brightness_slider.pack()

        self.rotate_label = tk.Label(self.root, text="Поворот")
        self.rotate_label.pack()
        self.rotate_slider = tk.Scale(self.root, from_=0, to=360, orient=tk.HORIZONTAL, command=self.rotate_image)
        self.rotate_slider.set(0)
        self.rotate_slider.pack()

        self.save_button = tk.Button(self.root, text="Сохранить", command=self.save_image)

        self.save_button.pack(pady=10)

        # Холст для отображения изображения

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

    def take_screenshot(self):
        screenshot = ImageGrab.grab()
        self.image = screenshot
        self.current_image = self.image.copy()

        self.display_image(self.current_image)

    def display_image(self, image):
        self.canvas.delete("all")
        image = image.resize((800, 600), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def adjust_brightness(self, value):
        if self.current_image:
            enhancer = ImageEnhance.Brightness(self.current_image)
            self.current_image = enhancer.enhance(float(value))
            self.display_image(self.current_image)

    def rotate_image(self, value):
        if self.current_image:
            angle = int(value)
            self.current_image = self.current_image.rotate(angle, expand=True)
            self.display_image(self.current_image)

    def save_image(self):
        if self.current_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.current_image.save(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenShotApp(root)
    root.mainloop()
