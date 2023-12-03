from return_data_file import data_file
from return_data_file import data_file_copy


def copy_row():
    data, nf = data_file()
    
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки для перемещения"
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки для перемещения "
                               f"от 1 до {count_rows}: "))

    copy_inf_row = data[number_row-1] #Сохраняем данные для переноса в переменную 

    data_to, nf_to = data_file_copy() # Выбираем файл куда переносим данные 
    
    if nf == nf_to:
        print("Извини, но файл уже есть в даной папке, попробуйте другую")
        data_to, nf_to = data_file_copy()
    
    now_number_row_to = len(data_to) + 1


    with open(f'db/data_{nf_to}.txt', 'a', encoding='utf-8') as file:
        file.write(copy_inf_row) # Сохраняем данные в новой место

    del data[number_row-1] # Удаляем данные с старого места
    data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)    
    

    print(f"\n------------------\n\nДанные успешно перенесены!\n\n------------------\n")
