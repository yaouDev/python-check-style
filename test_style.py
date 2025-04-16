import program
import random

def test_add():
    a = random.random()
    b = random.random()
    result = a + b
    assert program.add(a, b) == result