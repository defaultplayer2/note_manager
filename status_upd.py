#создаем коллекцию доступных статусов
status_book = {1:'выполнено', 2:'в процессе',3:'отложено',4:'начало работы'}
main_status = status_book.pop(4)
print (f"Статус заметки:{main_status}")

while True:  # Бесконечный цикл, который будет продолжаться, пока не получим стоп-слово или пустое значение
    status1 = input(f"Выберите новый статус заметки:{status_book.values()}") # Запрашиваем статус

    if status1 == "стоп-слово" or status1 == "": # Если введено стоп-слово или пустое значение, прерываем цикл
        print("Цикл завершен.")
        break  # Завершаем цикл
    else:
        #работа с доступными значениями статуса
        if status1 == '1':
            main_status = status_book.get(1)
        else:
            if status1 == '2':
                main_status = status_book.get(2)
            else:
                if status1 == '3':
                    main_status = status_book.get(3)
                else:
                    if status1 !='1' or status1 !='2' or status1 !='3' : #если статус введен не из списка
                        main_status = status_book.get(4)
        print(f"Вы ввели статус: {main_status}, желаете обновить?")