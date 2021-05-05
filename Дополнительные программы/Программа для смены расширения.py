from PIL import Image, ImageDraw
import os


def change_jpg(user_name, ras):
    im = Image.open(f"Недоделаные смена расширения/{user_name}")
    tmp = user_name.split(".")
    tmp2 = ".".join(tmp[:-1])
    im.save(f"Сделаные смена расширения/{tmp2}{ras}")


a = input("Введите на какое расширение хотите поменять например .png: ")
os.chdir("Недоделаные смена расширения")
tmp = os.getcwd()
test = os.listdir(tmp)
os.chdir("..")
for item in test:
    change_jpg(item, a)
