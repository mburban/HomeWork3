# Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'. В этой строке указаны имя писателя
# и через символ * даты рождения и смерти. Даты указаны в формате "YYYY-MM-DD". Требуется написать программу,
# которая по переданной строке определит возраст писателя и распечает его имя и возраст.
# Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечает: 'Leo Tolstoy, 82'.
# Для строки 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'.

writer = 'Leo Tolstoy*1828-08-28*1910-11-20'
a = writer.find("*")
writer_name = writer[:a]
# print(writer_name)
b = writer.find('*', a + 1)
writer_birth_date = writer[a + 1:b]
# print(writer_birth_date)
writer_death_date = writer[b + 1:]
# print(writer_death_date)
writer_age = int(writer_death_date[:4]) - int(writer_birth_date[:4])
# print(writer_age)
print('Name and age of the writer: {0}, {1} years old'.format(writer_name, writer_age))
