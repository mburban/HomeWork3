# Преобразовать строку с американским форматом даты в европейский. Например, '05.17.2016' преобразуется в '17.05.2016'

us_date = '07.17.1989'
eu_date = us_date[3:5] + str('.') + us_date[0:2] + str('.') + us_date[6:]
print('US format:', us_date)
print('EU format:', eu_date)
