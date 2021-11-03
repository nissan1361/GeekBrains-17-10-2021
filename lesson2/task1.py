import re
import csv
main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]


def get_data():
    for i in range(3):
        num = i + 1
        file = 'info_' + str(num) + '.txt'
        f = open(file, 'r')

        lines = f.readlines()

        for line in lines:
            print(line.strip())
            ls = line.split(',')
            main_data.append(ls)

        f.close()


get_data()
print(main_data)


def write_to_csv():
    with open('data_file.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in main_data:
            f_n_writer.writerow(row)


write_to_csv()