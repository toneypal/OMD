# toneypal - Antonina Palchikova
# Программа робот-помощник-информатор


import os
import sys
import platform

# ниже некоторые инструкции
# print("os.name = ", os.name)
# ModuleNotFoundError: No module named 'psutil'
# print("os.cpu_count = ", os.cpu_count())
# print("os.cpu_count = ", os.cpu_count())
# print("os.getcwd = ", os.getcwd())
# print("os.getegid = ", os.getegid())
# print("os.getuid = ", os.getuid())
# print("os.getlogin = ", os.getlogin())
# print("os.getpid = ", os.getpid())
# print(help(sys))
# print("os.name - ", os.system('uname - o'))
# print("os.getcwd = ", os.getcwd())
# print("os.getlogin = ", os.getlogin())
# print("os.name - ", platform.system())
# print("file systen encoding = ", sys.getfilesystemencoding())
# print("os.cpu_count = ", os.cpu_count())
# print('\n')

print( '\n', "Ваше имя?")
name = input()

print("Привет,", name, '\n')
# print()

answer = ''
FILE_LIST_IN_DIR = os.listdir()

CHOISE = (1, 2, 3, 4, 5)

while answer != 'q':
    answer = input("\n хотите поработать? [y/n/q]")

    try:

        if answer == 'y':
            # print('\n')
            print("Тогда выберете из списка:")
            print('\n')
            print(" [1] - вывести список файлов")
            print(" [2] - вывести инфо о системе")
            # print(" [3] - вывести список процессов")
            print(" [3] - вывести путь до текущего файла")
            print(" [4] - Дублирование указанного файла")
            print(" [5] - Удаление файлов .dupl в указанной директории")

            choise = input("Введите ваш выбор:")
            # print(type(choise), type(int))
            if  type(choise) is not int and int(choise) not in CHOISE:
                print(type(int(choise)), type(choise))
                print("Answer is not recognazed")

            elif int(choise) == 1:
                print(os.listdir('../py_less'))

            elif int(choise) == 2:
                print('\n')
                print("ОС name: ", os.uname().nodename)
                print("release: ", os.uname().release)
                print("version: ", os.uname().version)
                print("Разрядность: ", os.uname().machine)
                print("Имя ОС: ", platform.system())
                print("Логин пользователя: ", os.getlogin())
                print("Имя текущей директории: ", os.getcwd())
                print("Название кодировки файловой системы: ", sys.getfilesystemencoding())
                print('\n')

            elif int(choise) == 3:
                print("Путь до текущей дирректории: ", os.getcwd())

            elif int(choise) == 4:
                print(FILE_LIST_IN_DIR)
                print("выберете файл для копирования [имя_файла]")
                fn_for_copy = input()
                if fn_for_copy in FILE_LIST_IN_DIR:
                    new_file = fn_for_copy + '.dupl'
                    print(FILE_LIST_IN_DIR)
                    print("Файл успешно скопировался")
                else:
                    print(f'Я не смог найти файл {fn_for_copy}')

            elif int(choise) == 5:
                print(FILE_LIST_IN_DIR)
                fn_for_remove = input("выберете файл для удаления [имя_файла]")
                if fn_for_remove in FILE_LIST_IN_DIR:
                    os.remove(fn_for_remove)
                    print("Файл успешно удален")
                else:
                    print(f'Я не смог найти файл {fn_for_remove}')

            elif type(choise) is not int:
                print("Answer is not recognazed")

            else:
                print("Answer is not recognazed")
                # break


            # file_list = os.listdir()
            # i = 0
            # while i < len(file_list):
            #     new_file = file_list[i] + '.dupl'
            #     shutil.copy(file_list[i], new_file)
            #     i += 1.txt

        elif answer == 'n':
            print("Good bay!")
            exit()
        elif answer == 'q':
            exit()
        else:
            print("Answer is not recognazed")

    except Exception as e:
        print("Некорректный ввод!")
        # print(f'e = {e} /n trace: {e.with_traceback()}')

