from PIL import Image, ImageDraw
import pystray
import os
import winshell

#Картинка для иконки
def create_image(filled=False):
    image = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    outline = (20, 20, 20)
    body_fill = (210, 210, 215)
    lid_fill = (170, 170, 175)

    #Крышка
    draw.rectangle([6, 10, 58, 20], fill=lid_fill, outline=outline, width=3)

    #Ручка на крышке
    draw.rectangle([22, 2, 42, 11], fill=lid_fill, outline=outline, width=3)

    #Тело корзины
    draw.polygon(
        [(10, 22), (54, 22), (48, 62), (16, 62)],
        fill=body_fill,
        outline=outline,
    )
    draw.line([(10, 22), (54, 22), (48, 62), (16, 62), (10, 22)], fill=outline, width=3)

    #Рёбра
    draw.line([(20, 28), (17, 58)], fill=outline, width=4)
    draw.line([(32, 28), (32, 59)], fill=outline, width=4)
    draw.line([(44, 28), (47, 58)], fill=outline, width=4)

    return image

#Функция 'Выход'
def on_quit(icon, item):
    icon.stop()

#Открытие корзины
def open_basket(icon, item):
    os.startfile("shell:RecycleBinFolder")

#Удаление файлов корзины
def clear_basket(icon, item):
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

#Меню
menu = pystray.Menu(
    pystray.MenuItem('Открыть корзину', open_basket),
    pystray.MenuItem('Очистить корзину', clear_basket),
    pystray.MenuItem('Выход', on_quit)
    )

icon = pystray.Icon('Корзина', create_image(), 'Корзина', menu)
icon.run()