import json

# 01  Ветка нового интерфейса
# • Создайте ветку feature/menu из main.
# • Добавьте файл menu.txt с четырьмя пунктами будущего меню.
# • Создайте коммит с понятным сообщением и покажите краткий лог всех веток.

# 02  История двух версий
# • В ветке feature/readme дополните README описанием Quest Tracker.
# • Сделайте два небольших коммита: сначала цель проекта, затем список файлов.
# • Командой git log --oneline сравните порядок коммитов.

# 03  Безопасное объединение
# • Создайте feature/settings, добавьте settings.json и коммит.
# • Вернитесь в main и объедините ветку.
# • Проверьте status и log --graph после merge.

# 04  Учебный конфликт
# • В двух ветках измените одну строку файла slogan.txt по-разному.
# • Выполните merge, найдите маркеры конфликта и оставьте согласованный вариант.
# • Завершите merge отдельным коммитом.

# 05  Паспорт Quest Tracker
# • Создайте quest_db.json с ключами next_id и players.
# • Добавьте двух игроков. У каждого должны быть id, nickname, level, inventory и quests.
# • Проверьте файл через json.load и выведите количество игроков.

with open("quest_db.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

players_count = len(data["players"])
print(f"Количество игроков в базе: {players_count}")

# 06  Надёжное хранилище
# • Напишите load_db и save_db.
# • При отсутствии файла или повреждённом JSON возвращайте пустую структуру базы.
# • Сохраняйте кириллицу без кодов Unicode и используйте отступ 4.

FILE_NAME = "quest_db.json"

def load_db():
    try:
        with open(FILE_NAME, "r", encoding = "utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"next_id": 1, "players": []}

def save_db(data):
    with open(FILE_NAME, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)







