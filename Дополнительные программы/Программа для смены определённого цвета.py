from PIL import Image, ImageDraw
import os


def change_color(user_name, value, value2, warning):
    im = Image.open(f"Недоделанные сменна цвета/{user_name}")
    pixels = im.load()  # список с пикселями
    print(pixels)
    x, y = im.size  # ширина (x) и высота (y) изображения
    ro, go, bo = 0, 0, 0
    c = 0

    user_r = int(value[0])
    user_g = int(value[1])
    user_b = int(value[2])

    for i in range(x):
        for j in range(y):
            if warning == "да":
                r, g, b, a = pixels[i, j]
            else:
                r, g, b = pixels[i, j]
            # print(type(r), r)
            # print(type(g), g)
            # print(type(b), b)
            if r == user_r and g == user_g and b == user_b:
                r, g, b = int(value2[0]), int(value2[1]), int(value2[2])
            # elif r == 0 and g > value and b > value and g < value2 and b < value2:
            #     r, g, b = user_r, user_g, user_b
            # elif r > value and g == 0 and b > value and r < value2 and b < value2:
            #     r, g, b = user_r, user_g, user_b
            # elif r > value and g > value and b == 0 and r < value2 and g < value2:
            #     r, g, b = user_r, user_g, user_b

            pixels[i, j] = r, g, b
    im.save(f"Сделанные смена цвета/{user_name}")


user_value = input("Введите цвет который вы хотите изменить в формате rgb: ").split()
user_value1 = input("Введите цвет на который вы хотите изменить в формате rgb: ").split()
warning = input("Если фото открывалось в фотошопе напишите да: ")

os.chdir("Недоделаные смена фона")
tmp = os.getcwd()
test = os.listdir(tmp)
os.chdir("..")
for item in test:
    change_color(item, user_value, user_value1, warning)