import os
from pathlib import Path
import sqlite3

import pandas as pd
import pdfplumber

BASE_DIR = Path(__file__).resolve().parent

# Получаем пути ко всем pdf файлам в текущей директории
PDF_FILES = list(map(lambda file: BASE_DIR/"specifications"/file, filter(lambda file: file.endswith(".pdf"), os.listdir(BASE_DIR/"specifications"))))

TABLE_COLUMNS = ["property", "test_method", "units", "value"]

def parse_pdf(pdf_files: list) -> list:
    tables = []
    for file in pdf_files:
        with pdfplumber.open(file) as pdf:
            all_rows = []
            for page in pdf.pages:
                all_rows = all_rows + page.extract_table()
        tables.append(list(filter(lambda row: all(row), all_rows)))
    return tables

def update_db() -> None:
    tables = parse_pdf(PDF_FILES)
    with sqlite3.connect('product_information.db') as conn:
        for table in tables:
            df = pd.DataFrame(table[1:], columns=TABLE_COLUMNS)
            df.to_sql(
                name="product_information",
                con=conn,
                if_exists="append",
                index=False
            )

def main() -> None:
    with sqlite3.connect(BASE_DIR/"product_information.db") as conn:
        # Проверяем наличие таблицы в БД
        is_exist = conn.execute(
                """SELECT name
                FROM sqlite_master
                WHERE type = 'table' 
                    AND name = 'product_information';""").fetchone()
        if is_exist:
            update_db()
        else:
            conn.execute(
                f"""CREATE TABLE product_information (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {TABLE_COLUMNS[0]} TEXT NULL,
                {TABLE_COLUMNS[1]} VARCHAR(50) NULL,
                {TABLE_COLUMNS[2]} VARCHAR(15) NULL,
                {TABLE_COLUMNS[3]} VARCHAR(10) NULL);"""
            )
            update_db()
        print(*conn.execute("SELECT * FROM product_information;").fetchall(), sep="\n")


if __name__ == "__main__":
    main()
