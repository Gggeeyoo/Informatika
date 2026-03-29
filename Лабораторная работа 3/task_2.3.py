# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, n=","):
    str_one = set(first_group.split(n))  # Разделяем строку на список подстрок, а после преобразовываем в множество
    str_two = set(second_group.split(n))
    common = list(str_two.intersection(str_one))  # Находим пересечения множеств и преобразовываем в список
    common.sort()  # Сортируем в алфавитном порядке
    return common


participants_first_group = "Иванов|Петров|Сидоров"  # Проверка с разделителем |
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой

part_first_group = "Иванов,Петров,Сидоров"  # Проверка с разделителем по умолчанию
part_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(part_first_group, part_second_group))

participant_first_group = "Южный Сидоров Петров"  # Проверка с разделительным пробелом
participant_second_group = "Южный Сидоров Смирнов"

print(find_common_participants(participant_first_group, participant_second_group, " "))
