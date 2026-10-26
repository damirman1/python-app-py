import json

# 01 Проверка данных
# 1. Создайте папку dronehub и перенесите образец dronehub.json из вводной части. Исходный файл прошлого проекта не перезаписывайте.
# 2. Загрузите JSON и выведите количество дронов и доставок.

with open("dronehub.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

    print(f"Кол-во дронов: {len(data["drones"])}")
    print(f"Кол-во дронов: {len(data["deliveries"])}")

# 02 Доставки выбранного статуса
# 1. Напишите filter_status(deliveries, status), возвращающую все доставки заданного статуса.
# 2. Верните новый список, не меняя исходные записи. Для неизвестного статуса верните [].

def filter_status(deliveries, status):
    result = []

    for delivery in deliveries:
        if delivery["status"] == status:
            result.append(delivery)
    return result

# 03 Завершённые доставки от заданной цены
# 1. Напишите completed_from(deliveries, min_price). Выбирайте только done с ценой не меньше min_price.
# 2. Граница включается: доставка с ценой ровно min_price тоже подходит.

def completed_from(deliveries, min_price):
    result = []

    for delivery in deliveries:
        if delivery["status"] == "done" and delivery["price"] >= min_price:
            result.append(delivery)
    return result

# 04 Доставки без завершения
# 1. Напишите not_completed(deliveries), выбирающую записи ready или cancelled.
# 2. Не включайте done и не меняйте статусы.

def not_completed(deliveries):
    result = []

    for delivery in deliveries:
        if delivery["status"] == "ready" or delivery["status"] == "cancelled":
            result.append(delivery)
    return result

deliveries = data["deliveries"]
print("=" * 30)
print(not_completed(deliveries))
print("=" * 30)
print(completed_from(deliveries, 1200))
print("=" * 30)
print(filter_status(deliveries, "done"))
print("=" * 30)

# 05 Карточки без лишних полей
# 1. Напишите short_rows(deliveries). Верните новый список словарей только с id и cargo.
# 2. Проверьте функцию на результате completed_from с min_price=1500.



# 06 Два самых дорогих результата
# 1. Напишите top_deliveries(deliveries, limit). Отсортируйте полученный список по цене по убыванию и верните первые limit записей.
# 2. Если limit <= 0, верните []. Если записей меньше limit, верните все. Сначала передайте результат completed_from, а не все доставки.



# 07 Итог завершённых доставок
# 1. Напишите delivery_summary(deliveries). Верните словарь count и total только по done.
# 2. Для пустого списка оба значения должны быть нулевыми.



# 08 Полезный отчёт
# 1. Напишите export_top_completed(data, min_price, limit), используя completed_from и top_deliveries из предыдущих заданий.
# 2. Запишите выбранные названия грузов и цены в top_completed.txt. Если выборка пуста, сохраните только заголовок. Верните количество строк доставок.
# 3. Запустите с min_price=1500 и limit=2. Обновите README и отправьте работу в Git без веток.


