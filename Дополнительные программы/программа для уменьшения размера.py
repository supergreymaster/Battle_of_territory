from PIL import Image
import os


def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        print("Не существует картинки")
        raise SystemExit

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)


a = int(input("Насколько изменить размер избражений: "))

os.chdir("Недоделаные смена фона")
tmp = os.getcwd()
test = os.listdir(tmp)
os.chdir("..")
for item in test:
    scale_image(input_image_path=f'Недоделаные смена фона/{item}',
                output_image_path=f'Сделаные смена фона/{item}',
                width=a)