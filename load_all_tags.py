import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')


def load_all_tags():
    all_tags = []
    all_tags_filename = 'database_200.txt'
    with open(os.path.join(APP_STATIC, all_tags_filename), "r") as file:
        all_tags = eval(file.readline())
    return all_tags