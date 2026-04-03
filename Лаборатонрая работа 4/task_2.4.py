# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:  # Конвертация CSV в JSON
    with open(INPUT_FILENAME, "r", encoding="utf-8") as csv_file:  # TODO считать содержимое csv файла
        reader = csv.reader(csv_file)
        rows = list(reader)  # Все строки, включая заголовки
    if not rows:
        data = []
    else:
        headers = rows[0]  # Заголовки
        data = []
        for row in rows[1:]:  # Перебираем все строки, кроме заголовков
            dict_ = {}
            for i in range(len(headers)):
                dict_[headers[i]] = row[i]
            data.append(dict_)

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as json_file:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
