---
Author: sishevchenko
GitHub: https://github.com/sishevchenko
telegram: https://t.me/s_i_shevchenko
---

# Парсер информации из pdf файлов  

## Задача  
Написать парсер для pdf документов, который будет брать данные из таблицы и записывать их в sqlite  

### Запуск  
- для корректной работы скрипта используйте `Python 3.11.5`  
- добавьте все спецификации в папку `specifications`  
- откройте терминал или консоль разработчика из папки скрипта  
- установите виртуальное окружение:  
    - linux: `python3 -m venv venv`  
    - Windows: `python -m venv venv`  
- активируйте виртуальное окружение:  
    - linux: `source venv/bin/activate`  
    - Windows: `venv\scripts\activate`  
- установите зависимости `pip install -r requirements.txt`  
- запустите скрипт:  
    - linux: `python3 main.py`  
    - Windows: `python main.py`  

### Что ожидаем получить на выходе:  
- файл с базой данных SQLite с табличной информацией из pdf файла  
