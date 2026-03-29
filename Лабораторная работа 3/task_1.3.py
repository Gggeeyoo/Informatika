# TODO Напишите функцию для поиска индекса товара
def find_index_item(list_, item):
    for index, fruit in enumerate(list_):  # Перебираем товары в списке до совпадения
        if fruit == item:  # fruit - элемент списка, index - его индекс
            return index  # Выводим индекс товара, если нашли нужный
    return None  # Возвращаем None, если не нашли в списке товаров нужный


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_item(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
