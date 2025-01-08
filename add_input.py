name = str(input("Введите ваше имя: "))
date1 = str(input("Введите дату в формате дд/мм/гггг: "))
title1 = str(input("Введите заголовок заметки: "))
content1  = str(input("Введите вашу заметку: "))

print(f"Привет, {name}!")
print(f"Сегодня {date1[0:5]}")
print(f"Заголовок заетки: {title1}")
print(f"Содержимое заметки: {content1}")
issue_date = '23/12/2024'
print("Дедлайн:", issue_date[0:5])
