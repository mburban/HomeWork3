# Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase.
# Для простоты считаем, что имя переменной всегда состоит из 3-х слов.
# Например: 'employee_first_name' -> 'EmployeeFirstName'

snake_case_name = 'employee_first_name'
a = snake_case_name.find('_')
first_word = snake_case_name[:a]
# print(first_word)
b = snake_case_name.find('_', a + 1)
second_word = snake_case_name[a + 1: b]
# print(second_word)
third_word = snake_case_name[b + 1:]
# print(third_word)
camel_case_name = first_word.capitalize() + second_word.capitalize() + third_word.capitalize()
print('CamelCase format for {0} is {1}'.format(snake_case_name, camel_case_name))
