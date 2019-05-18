# Дана строка с именем студента, в которой имя предшествует фамилии, например  ‘Mark Zuckerberg‘.
# Написать программу, которая преобразует эту строку, ставя фамилию на первое место, а имя на второе.
# Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.

example_name = 'Ivan Ivanov'
a = example_name.find(' ')
transform_name = example_name[a:] + str(' ') + example_name[:a]
transformed_name = transform_name[1:]
print('Example name is:', example_name)
print('Transformed name is:', transformed_name)
