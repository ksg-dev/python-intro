from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5)
    assert str(jar)== "🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    jar.withdraw(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

def test_over(capfd):
    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(15)

def test_under(capfd):
    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(1)

def test_capacity(capfd):
    with pytest.raises(ValueError):
        jar = Jar()
        jar.capacity = -3








