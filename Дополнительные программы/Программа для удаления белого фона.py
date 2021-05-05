from PIL import Image, ImageDraw
import os


def change_color(user_name, user_value, value):
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
            if r > value and g > value and b > value:
                r, g, b = user_r, user_g, user_b
            pixels[i, j] = r, g, b
    im.save(f"Сделаные смена фона/{user_name}")


value = int(input("Введите число которое он будет отрезать: "))
user_value = input("Введите цвет в формате rgb: ").split()

os.chdir("Недоделаные смена фона")
tmp = os.getcwd()
test = os.listdir(tmp)
os.chdir("..")
for item in test:
    change_color(item, user_value, value)
# newcol = (0, 0, 0)
# im = Image.new("RGB", (x, y), newcol)
# r, g, b = newcol
# dram = ImageDraw.Draw(im)
# for i in range(y):
#     for j in range(x):
#
#     dram.line((i, 0, i, 200), fill=(r, g, b), width=2)
# im.save("res.png")
