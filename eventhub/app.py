import json

# 01  Паспорт EventHub
# Требования
# 1. Создайте папку eventhub и файлы app.py, eventhub_db.json и README.md.
# 2. В JSON создайте корневой словарь с ключами next_event_id и events.
# 3. Добавьте два мероприятия по образцу: у каждого должны быть id, title, category, date, price, capacity и participants.
# 4. В app.py загрузите JSON и выведите количество мероприятий.
# Повторение. Это задание восстанавливает навык прошлого урока и готовит основу общего проекта.

with open("eventhub_db.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

print(f"Мероприятий: {len(data["events"])}")

# 02  Надёжное хранилище
# Требования
# 1. Создайте функции load_db() и save_db(data).
# 2. Если файла нет или JSON повреждён, load_db должна вернуть пустую базу с правильными ключами.
# 3. Сохраняйте кириллицу читаемо и оформляйте JSON с отступом 4.
# Повторение. Это задание восстанавливает навык прошлого урока и готовит основу общего проекта.

FILE_NAME = "eventhub_db.json"

def load_db():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"next_event_id": 1, "events": []}

def save_db(data):
    with open(FILE_NAME, "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii = False, indent = 4)

# 03  Тестовое мероприятие
# Требования
# 1. Создайте функцию add_event(data, title, category, date, price, capacity).
# 2. Используйте next_event_id как уникальный номер и создавайте пустой список participants.
# 3. Добавьте мероприятие в список, увеличьте next_event_id и сохраните базу.
# Повторение. Это задание восстанавливает навык прошлого урока и готовит основу общего проекта.

def add_event(data, title, category, date, price, capacity):
    event = {
        "id": data["next_event_id"],
        "title": title,
        "category": category,
        "date": date,
        "price": price,
        "capacity": capacity,
        "participants": []
    }

    data["events"].append(event)
    data["next_event_id"] += 1
    return event

# 04  Удобная афиша
# Требования
# 1. Создайте функцию show_events(events).
# 2. Для каждого события покажите ID, название, дату, категорию и количество свободных мест.
# 3. Если список пуст, выведите понятное сообщение.

def show_events(events):
    if not events:
        print("Мероприятий пока нет!")
        return
    
    for event in events:
        free_places = event["capacity"] - len(event["participants"])
        print(f"{event['id']}{event['title']}")
        print(f"{event['date']}{event['category']}")
        print(f"{free_places}")

# 05  Поиск по номеру
# Требования
# 1. Создайте find_event(data, event_id).
# 2. Верните словарь мероприятия с нужным id.
# 3. Если совпадения нет, верните None.

def find_event(data, event_id):
    for event in data["events"]:
        if event["id"] == event_id:
            return event
        return None

# 06  Тематическая подборка
# Требования
# 1. Создайте filter_by_category(data, category).
# 2. Соберите и верните новый список подходящих мероприятий.
# 3. Поиск не должен зависеть от регистра букв.

def filter_by_category(data, category):
    found_events = []
    for event in data["events"]:
        if event["category"].lower() == category.lower():
            found_events.append(event)
    return found_events

# 07  Афиша по датам
# Требования
# 1. Создайте sort_by_date(data).
# 2. Верните новый список, отсортированный по полю date с помощью sorted и lambda.
# 3. Исходный список в базе не изменяйте. Используйте формат даты ГГГГ-ММ-ДД.

def sort_by_date(data):
    return sorted(
        data["events"], 
        key = lambda event: event["date"]
        )

# 08  Бронирование места
# Требования
# 1. Создайте book_ticket(data, event_id, participant).
# 2. Запрещайте бронь, если мероприятия нет, имя уже записано или свободные места закончились.
# 3. При успехе добавьте имя в participants и верните результат с понятным сообщением.

def book_ticket(data, event_id, participant):
    event = find_event(data, event_id)

    if event is None:
        return False, "Мероприятие не найдено!"

    if participant in event["participants"]:
        return False, "Такое имя уже зарегистрировано!"

    if event["capacity"] <= len(event["participants"]):
        return False, "Свободных мест нет!"
    
    event["participants"].append(participant)   
    return True, "Бронь добавлена!"

# 09  Отмена брони
# Требования
# 1. Создайте cancel_ticket(data, event_id, participant).
# 2. Удаляйте имя только из нужного мероприятия.
# 3. Верните True при успешной отмене и False, если событие или участник не найдены.

def cancel_ticket(data, event_id, participant):
    event = find_event(data, event_id)

    if event is None:
        return False

    if participant not in event["participants"]:
        return False

    event["participants"].remove(participant)
    return True

# 10  Редактор события
# Требования
# 1. Создайте edit_event(data, event_id, new_title, new_date, new_price).
# 2. Изменяйте только найденное мероприятие.
# 3. Верните логический результат, чтобы меню понимало, нужно ли сохранять файл.

def edit_event(data, event_id, new_title, new_date, new_price):
    event = find_event(data, event_id)

    if event is None:
        return False

    event["title"] = new_title
    event["date"] = new_date
    event["price"] = new_price
    return True

# 11  Удаление из афиши
# Требования
# 1. Создайте delete_event(data, event_id).
# 2. Найдите мероприятие через find_event и удалите весь словарь из events.
# 3. Несуществующий ID не должен останавливать программу.

def delete_event(data, event_id):
    event = find_event(data, event_id)

    if event is None:
        return False

    data["events"].remove(event)
    return True

# 12  Популярные события
# Требования
# 1. Создайте sort_by_popularity(data).
# 2. Расположите мероприятия от самого заполненного к наименее заполненному.
# 3. Используйте количество элементов participants как ключ сортировки.

def sort_by_popularity(data):
    return sorted(
        data["events"],
        key = lambda event: len(event["participants"]),
        reverse = True
    )

# 13  Статистика EventHub
# Требования
# 1. Создайте get_statistics(data).
# 2. Посчитайте количество мероприятий, число всех броней и возможный доход от уже забронированных мест.
# 3. Найдите название события с наибольшим количеством участников и верните результаты одним словарём.

def get_statistics(data):
    total_events = len(data["events"])
    total_bookings = sum(len(event["participants"]) for event in data["events"])
    potential_income = sum(event["price"] * len(event["participants"]) for event in data["events"])
    
    most_popular_event = max(
        data["events"], 
        key=lambda event: len(event["participants"])
        )["title"]

    return {
        "total_events": total_events,
        "total_bookings": total_bookings,
        "potential_income": potential_income,
        "most_popular_event": most_popular_event
    }

# 14  Отчёт для организатора
# Требования
# 1. Создайте export_report(data).
# 2. Запишите статистику в текстовый файл eventhub_report.txt.
# 3. Каждый показатель должен находиться на отдельной строке, а кириллица должна сохраняться правильно.

def export_report(data):
    with open("eventhub_report.txt", "w", encoding = "utf-8") as file:
        stats = get_statistics(data)
        file.write(f"Мероприятий: {stats["total_events"]}\n")
        file.write(f"Броней: {stats["total_bookings"]}\n")
        file.write(f"Возможный доход: {stats["potential_income"]}\n")
        file.write(f"Самое популярное мероприятие: {stats["most_popular_event"]}\n")

# 15  Готовый EventHub
# Требования
# 1. Соберите функции в одно циклическое меню: просмотр, добавление, фильтр, сортировка, бронь, отмена, редактирование, удаление, статистика, отчёт и выход.
# 2. После каждого успешного изменения вызывайте save_db(data). Неправильное число или пункт меню не должны завершать программу.
# 3. Заполните README.md: назначение проекта, файлы, запуск и возможности.
# 4. Проверьте git status, выполните git add ., создайте итоговый commit и отправьте проект командой git push. Ветки не используйте.

def main():
    data = load_db()

    while True:
        print("\n--- EventHub ---")
        print("1. Посмотреть мероприятия")
        print("2. Добавить мероприятие")
        print("3. Забронировать место")
        print("4. Статистика")
        print("0. Выход!")

        choice = input("Выберите пункт: ")

        if choice == "1":
            show_events(data["events"])

        elif choice == "2":
            title = input("Название: ")
            category = input("Категория: ")
            date = input("Дата: ")
            price = float(input("Цена: "))
            capacity = int(input("Вместимость: "))
            
            add_event(data, title, category, date, price, capacity)
            save_db(data)
            print("Добавлено!")

        elif choice == "3":
            event_id = int(input("ID мероприятия: "))
            name = input("Ваше имя: ")
            
            success, message = book_ticket(data, event_id, name)
            if success:
                save_db(data)
            print(message)

        elif choice == "4":
            stats = get_statistics(data)
            print(stats)

        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверно, попробуйте снова!")

main()