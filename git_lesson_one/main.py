import json

# 05  Каталог игровых профилей
# Создайте players.json со списком из пяти словарей: id, nickname, level и active. Сохраните кириллицу читаемо и сделайте отступы.
# Проверяемый навык: Сериализация списка словарей

players = [
    {"id": 1, "nickname": "Ali"    , "level": 12 , "active": True },
    {"id": 2, "nickname": "Alisher", "level": 135, "active": True },
    {"id": 3, "nickname": "Danila" , "level": 18 , "active": False},
    {"id": 4, "nickname": "Damir"  , "level": 42 , "active": False},
    {"id": 5, "nickname": "Malika" , "level": 16 , "active": True },
    {"id": 6, "nickname": "Amirlan", "level": 169, "active": False},
    {"id": 7, "nickname": "Kanysh" , "level": 82 , "active": True },
    {"id": 8, "nickname": "Dmitriy", "level": 62 , "active": True }
]

with open("players.json", "w", encoding = "utf-8") as file:
    json.dump(players, file, ensure_ascii = False, indent = 3)

print(players)


# 06  Загрузка турнира
# Прочитайте players.json и выведите каждого игрока в формате: Mira — уровень 7 — активен. Для неактивного игрока выведите неактивен.
# Проверяемый навык: Десериализация и обход данных

with open("players.json", "r", encoding = "utf-8") as file:
    players = json.load(file)

for player in players:
    status = "активен" if player["active"] else "неактивен"
    print(f"{player["nickname"]} - {player["level"]} уровень {status}")


# 07  Новый игрок
# Напишите функцию add_player(nickname, level), 
# которая загружает players.json, создаёт следующий id, добавляет активного игрока и сохраняет файл.
# Проверяемый навык: Добавление записи

def add_player(nickname, level):
    with open("players.json", "r", encoding = "utf-8") as file:
        players = json.load(file)

    new_id = max((player["id"] for player in players), default = 0) + 1

    players.append(
        {"id": new_id, 
        "nickname": nickname, 
        "level": level, 
        "active": True}
        )

    with open("players.json", "w", encoding = "utf-8") as file:
        json.dump(players, file, ensure_ascii = False, indent = 3)

add_player("Ali213pro", 14)