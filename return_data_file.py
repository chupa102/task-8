from choice_file import choice_number_file
from choice_file import choice_number_file_copy

def data_file():
    nf = choice_number_file()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf

def data_file_copy():
    nf = choice_number_file_copy()
    with open(f'db/data_{nf}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data, nf
