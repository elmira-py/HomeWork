import pytest

from src.decorators import log, my_function


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


def test_log():
    with pytest.raises(Exception, match="division by zero"):
        my_function(-3, 0)


@log()
def my_function(x, y):
    return x + y


def test_log_add():
    result = my_function(1, 2)
    assert result == 3


def test_my_function(capsys):
    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert "my_function ok" in captured.out
