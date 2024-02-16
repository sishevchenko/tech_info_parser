---
Author: sishevchenko
GitHub: https://github.com/sishevchenko
telegram: https://t.me/s_i_shevchenko
---

# Парсер информации из pdf файлов  

## Задача  
Написать парсер для pdf документов, который будет брать данные из таблицы и записывать их в sqlite  

### Запуск  
- открыть терминал или консоль разработчика из папки скрипта
- установить виртуальное окружение `python3 -m venv venv`  
- включить виртуальное окружение 
    - linux: `source venv/bin/activate`
    - Windows: `venv\scripts\activate`
- установить зависимости `pip install -r requirements.txt`  
- запустить `python3 main.py`  

### Что ожидаем получить на выходе:  
- файл с базой данных SQLite с табличной информацией из pdf файла  
