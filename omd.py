#  coding: utf-8
# toneypal - Antonina Palchikova

def step1():
    print(
        'Утка-маляр     решила выпить зайти в бар.  '
        'Взять ей зонтик?   '
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print ('Выберете: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_umbrella()

if __name__ == '__main__':
    step1()