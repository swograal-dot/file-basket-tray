from PIL import Image, ImageDraw
import pystray
import os
import winshell
import winreg
import sys
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

REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
APP_NAME = "FileBasket"

#Автозапуск
def is_autostart_enabled():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_READ)
        winreg.QueryValueEx(key, APP_NAME)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False


def toggle_autostart(icon, item):
    if is_autostart_enabled():
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(key, APP_NAME)
        winreg.CloseKey(key)
    else:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, APP_NAME, 0, winreg.REG_SZ, sys.executable)
        winreg.CloseKey(key)

#Меню
menu = pystray.Menu(
    pystray.MenuItem('Открыть корзину', open_basket),
    pystray.MenuItem('Очистить корзину', clear_basket),
    pystray.MenuItem(
        'Запускать при старте Windows',
        toggle_autostart,
        checked=lambda item: is_autostart_enabled(),
    ),
    pystray.MenuItem('Выход', on_quit)
    )

icon = pystray.Icon('Корзина', create_image(), 'Корзина', menu)
icon.run()