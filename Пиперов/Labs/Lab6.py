import sqlite3


def create_table():
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    cursor.execute("""
    INSERT INTO users (name, email) VALUES ("Alice", "alice@example.com")
    """)
    cursor.execute("""
    INSERT INTO users (name, email) VALUES ("BOB", "bob@example.com")
    """)
    cursor.execute("""
    INSERT INTO users (name, email) VALUES ("Charlie", "charlie@example.com")
    """)

    conn.commit()
    conn.close()


def get_records_by_field(table_name, field_name):
    """
    Написать функцию, которая принимает наименование таблицы,
    имя поля и возвращает все записи по полученному полю из
    указанной таблицы
    """

    create_table()

    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    query = f"SELECT {field_name} FROM {table_name}"

    cursor.execute(query)

    records = cursor.fetchall()

    conn.close()

    return records


table_name = "users"
field_name = "email"

print(get_records_by_field(table_name, field_name))
