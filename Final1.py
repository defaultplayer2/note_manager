name = str(input("Введите ваше имя: "))
created_date = str(input("Введите дату создания в формате дд/мм/гггг: "))
issue_date = str(input("Введите дату изменений в формате дд/мм/гггг: "))
status1 = str(input("Введите статус задачи: "))
title1 = str(input("Введите заголовок заметки: "))
title2 = str(input("Введите заголовок заметки: "))
title3 = str(input("Введите заголовок заметки: "))
content1  = str(input("Введите вашу заметку: "))

title_list1 = [ title1, title2, title3]

note = [
"Имя пользователя: ", name,
"Содержание заметки: ", content1,
"Статус: ", status1,
"Дата создания: ", created_date[0:5],
"Дата изменения: ", issue_date[0:5],
"Заголовки: ", title_list1
]

print(note)
