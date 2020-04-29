import pytest
from src.timer import Timer

def test_exercise():
    timer = Timer()

    assert str(timer) == "00:00"

    timer.advance()
    assert str(timer) == "00:01"

    for i in range(100):
        timer.advance()

    assert str(timer) == "01:01"
