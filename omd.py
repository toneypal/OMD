#  coding: utf-8
# toneypal - Antonina Palchikova

option = ''
options = {'да': True, 'нет': False}


def step1(option):
    print(
        'Утка-маляр     решила выпить зайти в бар.  '
        'Взять ей зонтик?   '
    )

    while option not in options:
        print('Выберете: {}/{}'.format(*options))
        option = input()

        if options[option]:
            step4_rain()
        else:
            step3_without_umbrella()


def step2_umbrella():
    print('Утка идет c зонтиком')


def step3_without_umbrella():
    print('Утка идет без зонтика')


def step4_rain():
    print('На улице идет дождь?')
    rain = input()
    if options[rain]:
        step2_umbrella()
    else:
        step5_cloudy()


def step5_cloudy():
    cloudy = input('На улице облачно?')
    if options[cloudy]:
        return step2_umbrella()
    else:
        return step3_without_umbrella()


if __name__ == '__main__':
    step1(option)
