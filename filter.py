from PIL import Image
import numpy as np


class Mozabrick:

    def __init__(self, img, size, grayscale):
        self.img = img
        self.size = size
        self.grayscale = 255 // grayscale

    def convert_image(self):
        height = len(self.img)
        width = len(self.img[1])
        for i in range(0, height, self.size):
            for j in range(0, width, self.size):
                brightness = self.get_brightness(i, j)
                self.set_grayscale(brightness, i, j)
        return Image.fromarray(self.img)

    def set_grayscale(self, brightness, i, j):
        self.img[i:i + self.size, j:j + self.size] = int(brightness // self.grayscale) * self.grayscale / 3

    def get_brightness(self, i, j):
        return int((self.img[i:i + self.size, j:j + self.size].sum()) // (self.size * self.size))


image = Image.open(input("Введите имя изображения: "))
size = int(input("Введите размер мозайки: "))
grayscale = int(input("Введите градацию серого: "))
array = np.array(image)
result = Mozabrick(array, size, grayscale).convert_image()
result.save(input("Введите имя для сохранения : "))