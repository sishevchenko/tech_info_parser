import os
from pathlib import Path
import sqlite3

import pandas as pd
import pdfplumber

BASE_DIR = Path(__file__).resolve().parent

# Получаем пути ко всем pdf файлам в текущей директории
PDF_FILES = list(map(lambda file: BASE_DIR / file, filter(lambda file: file.endswith(".pdf"), os.listdir(BASE_DIR))))


def parse_pdf(pdf_files: list) -> list:
    tables = []
    for file in pdf_files:
        with pdfplumber.open(file) as pdf:
            page = pdf.pages[0]
            table = page.extract_table() 
        tables.append(list(filter(lambda row: all(row), table[1:-1])))
    return tables

def update_db():
    tables = parse_pdf(PDF_FILES)
    for table in tables:
        df = pd.DataFrame(table[1:], columns=table[0])
        with sqlite3.connect('product_information.db') as conn:
            df.to_sql(name="product_information", con=conn, if_exists="replace")

def main():
    with sqlite3.connect(BASE_DIR / 'product_information.db') as conn:
        # Проверяем наличие таблицы в БД
        if conn.execute(
                """SELECT name
                FROM sqlite_master
                WHERE type = 'table' AND name = 'product_information';""").fetchone():
            update_db()
        else:
            conn.execute("""CREATE TABLE product_information (
                        id INT NOT NULL PRIMARY KEY,
                        property TEXT NULL,
                        test_method TEXT NULL,
                        units TEXT NULL,
                        value TEXT NULL);""")
            update_db()
        print(*conn.execute("SELECT * FROM product_information;").fetchall(), sep="\n")


if __name__ == "__main__":
    main()
