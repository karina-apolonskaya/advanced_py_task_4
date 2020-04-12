from datetime import date
import json
from secretary import documents, directories


def log_decorator(old_function):
    def new_function(*args, **kwargs):
        date_today = str(date.today())
        decorated_file = old_function(*args, **kwargs)
        decorated_file = {'name': old_function.__name__, "date": date_today, "arguments": [args, kwargs],
                          "result": decorated_file
                          }
        with open(kwargs['path'], "w", encoding='utf-8') as w_file:
            w_file.write(json.dumps(decorated_file, indent=4, ensure_ascii=False))
        return decorated_file
    return new_function


@log_decorator
def get_shelf_number(directory, path):
    user_doc_number_1 = input("Введите номер документа:"'\t')
    shelf_number = ""
    for directory in directories:
        if user_doc_number_1 in directories[directory]:
            shelf_number = directory
    if shelf_number != "":
        return f"Номер полки: {shelf_number}"
    else:
        return "Такого номера нет в базе! Попробуйте еще раз!"


if __name__ == "__main__":
    print(get_shelf_number(directories, path='new_log_2.json'))