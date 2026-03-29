# TODO  Напишите функцию count_letters
def count_letters(str_):
    letters_count = {}  # Создаём пустой словарь
    for simbol in str_.lower():  # Перебираем символы в строке, с буквами  только нижнего регистра
        if simbol.isalpha():  # Проверяем является ли символ буквой
            if simbol in letters_count:  # Добавляем буквы в словарь и считаем их количество в тексте
                letters_count[simbol] += 1
            else:
                letters_count[simbol] = 1
    return letters_count


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_count):
    count = 0
    frequency = {}
    for item in letters_count:  # Перебираем буквы в словаре
        count += letters_count.get(item)  # Считаем общее количество букв
    for letter in letters_count:
        frequency[letter] = (letters_count.get(letter) / count)  # Считаем частоту каждой буквы

    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

main_count_letters = count_letters(main_str)  # Считаем количество каждой буквы в main_str
main_frequency = calculate_frequency(main_count_letters)    # Считаем частоту каждой буквы в main_str

# TODO Распечатайте в столбик букву и её частоту в тексте
for main_letter in main_frequency:
    print(f'{main_letter}: {main_frequency.get(main_letter):.2f}')
