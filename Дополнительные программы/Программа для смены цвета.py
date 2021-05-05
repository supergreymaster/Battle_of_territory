from PIL import Image, ImageDraw
import os


def change_color(user_name, user_value, value, value2):
    im = Image.open(f"Недоделаные смена фона/{user_name}")
    pixels = im.load()  # список с пикселями
    print(pixels)
    x, y = im.size  # ширина (x) и высота (y) изображения
    ro, go, bo = 0, 0, 0
    c = 0

    user_r = int(user_value[0])
    user_g = int(user_value[1])
    user_b = int(user_value[2])

    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
            # print(type(r), r)
            # print(type(g), g)
            # print(type(b), b)
            if r > value and g > value and b > value and r < value2 and g < value2 and b < value2:
                r, g, b = user_r, user_g, user_b
            # elif r == 0 and g > value and b > value and g < value2 and b < value2:
            #     r, g, b = user_r, user_g, user_b
            # elif r > value and g == 0 and b > value and r < value2 and b < value2:
            #     r, g, b = user_r, user_g, user_b
            # elif r > value and g > value and b == 0 and r < value2 and g < value2:
            #     r, g, b = user_r, user_g, user_b

            pixels[i, j] = r, g, b
    im.save(f"Сделаные смена фона/{user_name}")


value = int(input("Введите число которое начало промежутка: "))
value1 = int(input("Введите 2 число которое конец промежутка промежутка: "))
user_value = input("Введите цвет в формате rgb: ").split()

os.chdir("Недоделаные смена фона")
tmp = os.getcwd()
test = os.listdir(tmp)
os.chdir("..")
for item in test:
    change_color(item, user_value, value, value1)