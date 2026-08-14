# File Basket

Трей-приложение для Windows: открывает и очищает Корзину Windows одним кликом из системного трея, без лишних окон.

![tray icon](icon.ico)

## Возможности

- Иконка-корзина в системном трее
- Открыть Корзину Windows через меню
- Очистить Корзину без подтверждающих окон
- Работает как отдельный `.exe`, без установки Python

## Технологии

- Python 3
- [pystray](https://github.com/moses-palmer/pystray) — иконка и меню в трее
- [Pillow](https://python-pillow.org/) — отрисовка иконки
- [winshell](https://pypi.org/project/winshell/) — работа с Корзиной Windows
- [PyInstaller](https://pyinstaller.org/) — сборка в `.exe`

## Установка и запуск

### Готовый .exe

Скачай `FileBasket.exe` из [Releases](../../releases) и запусти — Python не требуется.

### Из исходников

```bash
git clone https://github.com/swogral-dot/file-basket-tray.git
cd file-basket-tray
pip install -r requirements.txt
python app.py
```

## Сборка своего .exe

```bash
python make_icon.py
pyinstaller --onefile --windowed --icon=icon.ico --name=FileBasket app.py
```

Готовый файл появится в папке `dist`.

## Планы на будущее

- Индикатор заполненности Корзины прямо на иконке
- Автозапуск вместе с Windows
