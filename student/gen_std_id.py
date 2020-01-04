from datetime import datetime
from random import randint


def get_prefix():
    current_year = str(datetime.now().year)
    prefix = current_year[2:]
    return prefix


def get_postfix():
    postfix = 0
    current_month = datetime.now().month

    if current_month >= 1 and current_month <= 3:
        postfix = 1
    elif current_month >= 4 and current_month <= 7:
        postfix = 2
    elif current_month >= 8 and current_month <= 11:
        postfix = 3

    return str(postfix)


def get_random_five():
    random = ''
    for x in range(5):
        random += str(randint(0, 9))

    return random


def get_std_id():
    student_id = get_prefix() + '-' + get_random_five() + '-' + get_postfix()
    return student_id
