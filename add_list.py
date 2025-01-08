name = str(input("Введите ваше имя: "))
date1 = str(input("Введите дату в формате дд/мм/гггг: "))
title1 = str(input("Введите заголовок заметки: "))
title2 = str(input("Введите заголовок заметки: "))
title3 = str(input("Введите заголовок заметки: "))
content1  = str(input("Введите вашу заметку: "))

title_list1 = [ title1, title2, title3]

print(f"Привет, {name}!")
print(f"Сегодня {date1[0:5]}")
print(f"Заголовки заметки: {title_list1}")


print(f"Содержимое заметки: {content1}")
issue_date = '23/12/2024'
print("Дедлайн:", issue_date[0:5])
