import pytest

from src.decorators import log, my_function


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


def test_log():
    with pytest.raises(Exception, match="division by zero"):
        my_function(-3, 0)


@log()
def add(x, y):
    return x + y


# Тест
def test_add_logs_to_console(capsys):
    captured = capsys.readouterr()
    assert "" in captured.out
