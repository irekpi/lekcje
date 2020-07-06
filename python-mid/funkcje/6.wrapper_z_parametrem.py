import os
from datetime import datetime as dt


def wrapper_with_log_file(log_action, log_file_path):
    def wrapper_with_log_to_know_file(func):
        def real_wrapper(path):
            with(open(log_file_path, 'a')) as file:
                file.write(
                    'Action {} executed on {} on {}\n'.format(log_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            return func(path)

        return real_wrapper

    return wrapper_with_log_to_know_file


@wrapper_with_log_file("File create", r'pomoce/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file("File delete", r'pomoce/delete_create.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'pomoce/dummy_file.txt')
delete_file(r'pomoce/dummy_file.txt')
create_file(r'pomoce/dummy_file.txt')
delete_file(r'pomoce/dummy_file.txt')
