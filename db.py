import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

# 05 Подключение из Python
# 1. Реализуйте connect_db в db.py с загрузкой .env рядом с файлом.
# 2. Подключитесь через Psycopg 3 с dict_row и выполните 
# SELECT 1 AS result.
# 3. При отсутствии DATABASE_URL выдайте понятную ошибку.
# Закройте соединение через with.

def connect_db():
    load_dotenv(Path(__file__).with_name(".env"))
    url = os.getenv("DATABASE_URL")
    if not url:
        return ValueError("Добавьте DATABASE_URL в .env")
    return psycopg2.connect(url, connect_timeout=15 )
    
with connect_db() as conn, conn.cursor() as cur:
    cur.execute("SELECT 1 AS result")
    print(cur.fetchone()[0])

connect_db()

# 06 Список дронов
# 1. Подготовьте образец готовым импортом из README один раз.
# 2. Реализуйте list_drones с полями id, name, model и порядком по id.
# 3. Верните список словарей. Для пустой таблицы допустим пустой список.

def list_drones():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name, model FROM drones ORDER BY id")
        rows = cur.fetchall()
        return [{"id": row[0], "name": row[1], "model": row[2]} for row in rows]

# 07 Новый дрон с необычным именем
# 1. Реализуйте add_drone с параметрами name и model.
# 2. Уберите пробелы по краям, отклоните пустые значения, верните созданный ID.
# 3. Передайте значения отдельно от SQL. Проверьте имя Дрон O'Brien и обработайте повтор имени в меню.

def add_drone(name, model):
    name = name.strip()
    model = model.strip()
    if not name or not model:
        raise ValueError("Имя и модель не могут быть пустыми")
    
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO drones (name, model) VALUES (%s, %s) RETURNING id", (name, model))
        return cur.fetchone()[0]

# 08 Понятный журнал
# 1. Реализуйте list_deliveries через JOIN, показывая имя дрона вместо одного drone_id.
# 2. Верните id доставки, drone, cargo, price, status с сортировкой по id доставки.
# 3. На неизменённом образце должно быть шесть строк, без случайных повторов от неверного соединения.

def list_deliveries():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT d.id, dr.name AS drone, d.cargo, d.price, d.status
            FROM deliveries d
            JOIN drones dr ON d.drone_id = dr.id
            ORDER BY d.id
        """)
        rows = cur.fetchall()
        return [{"id": row[0], "drone": row[1], "cargo": row[2], "price": row[3], "status": row[4]} for row in rows]

# 09 Срочная посылка
# 1. Реализуйте add_delivery с ID существующего дрона, грузом и целой неотрицательной стоимостью.
# 2. Новая заявка должна получать ready из DEFAULT. Верните её ID.
# 3. Проверьте отрицательную цену, пустой груз и неизвестный ID дрона. Исходные заявки не изменяйте.

def add_delivery(drone_id, cargo, price):
    cargo = cargo.strip()
    if not cargo:
        raise ValueError("Груз не может быть пустым!")
    if price < 0:
        raise ValueError("Цена не может быть отрицательной!")
    
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id FROM drones WHERE id = %s", (drone_id,))
        if cur.fetchone() is None:
            raise ValueError("Неизвестный ID дрона!")
        
        cur.execute("INSERT INTO deliveries (drone_id, cargo, price) VALUES (%s, %s, %s) RETURNING id", (drone_id, cargo, price))
        return cur.fetchone()[0]