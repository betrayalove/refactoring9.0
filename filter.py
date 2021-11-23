import numpy as np
from PIL import Image


class Mozabrick:
    """ Класс, преобразующий картинку в черно-белую мозайку
            Тест размера блока
            >>> Mozabrick(np.array(Image.open('img2.jpg')), 10, 50).size
            10

            Тест значения градации изображения
            >>> Mozabrick(np.array(Image.open('img2.jpg')), 10, 50).grayscale
            5

            Тест размера картинки
            >>> Image.open('res.jpg').size
            (750, 750)

            Тест размера картинки полученного изображения
            >>> Mozabrick(np.array(Image.open('img2.jpg')), 10, 50).convert_image().size
            (750, 750)
    """

    def __init__(self, img, size, grayscale):
        self.img = img
        self.size = size
        self.grayscale = 255 // grayscale

    if __name__ == "__main__":
        import doctest
        doctest.testmod()

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
if size <= 0:
    raise ValueError("size must be > 0")
grayscale = int(input("Введите градацию серого: "))
if grayscale <= 0 or grayscale > 255:
    raise ValueError("grayscale must be > 0 and grayscale must be <= 255")
array = np.array(image)
result = Mozabrick(array, size, grayscale).convert_image()
result.save(input("Введите имя для сохранения : "))

# image = Image.open("img2.jpg")
# array = np.array(image)
# result = Mozabrick(array, size=10, grayscale=50).convert_image()
# result.save("res.jpg")
