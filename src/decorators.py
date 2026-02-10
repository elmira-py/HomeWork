from functools import wraps
from time import ctime

""" Декоратор log, который будет автоматически логировать начало и конец выполнения функции,
а также ее результаты или возникшие ошибки. Декоратор должен принимать необязательный
аргумент filename, который определяет, куда будут записываться логи (в файл или в консоль):
Если filename задан, логи записываются в указанный файл.
Если filename не задан, логи выводятся в консоль. Логирование должно включать:
Имя функции и результат выполнения при успешной операции. Имя функции, тип возникшей ошибки
и входные параметры, если выполнение функции привело к ошибке."""


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = ctime()
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok\n"
                log_message = f"{start_time} - {message}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as fail:
                        fail.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as e:
                end_time = ctime()
                error_message = f"{end_time} - {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as fail:
                        fail.write(error_message)
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(1, 2))
# Ожидаемый вывод в лог-файл mylog.txt при успешном выполнении: my_function ok
# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.
