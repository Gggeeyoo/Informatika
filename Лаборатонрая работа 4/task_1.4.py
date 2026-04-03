# TODO решите задачу
import json  # Подключаем модуль json для работы с JSON-файлами


def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as file:  # Открываем файл в режиме чтения с кодировкой UTF-8
        data = json.load(file)  # Преобразуем содержимое файла в список словарей
        sum_ = sum(item['score'] * item['weight'] for item in data)  # Суммируем произведения значений из словарей
    return round(sum_, 3)  # Возвращаем значение суммы произведений, округленное до 3 знаков после запятой


print(task())
