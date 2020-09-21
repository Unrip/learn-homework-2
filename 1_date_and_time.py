"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta, datetime


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = date.today()
    print(f'Вчера было {today - timedelta(days=1)}.')
    print(f'Сегодня - {today}.')
    print(f'А 30 дней назад было {today - timedelta(days=30)}.')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = '01/01/25 12:10:03.234567'
    dt_obj = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return dt_obj


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
