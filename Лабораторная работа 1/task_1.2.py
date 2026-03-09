# TODO Найдите количество книг, которое можно разместить на дискете
memory_size = 1.44
bytes_in_mb = 1024 * 1024
page_count = 100
row_count = 50
number_of_symbols = 25
simbol = 4

# Найдем объем дискеты в байтах
memory_size = memory_size * bytes_in_mb
# Найдём объём, занимаемый символами в книге
size = simbol * number_of_symbols * row_count * page_count
# Найдём количество книг, которые поместятся на дискете
number = int(memory_size // size)

print("Количество книг, помещающихся на дискету:", number)
