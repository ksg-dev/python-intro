from project import food
from project import type
from project import main
import pytest

test_dict = {"name" : "Chopped", "eat_how" : "sit down", "category" : "light-healthy"}

def test_food():
    assert food("light-healthy") == "🥦"
    assert food("Asian") == "🍣"
    assert food("steaks/burgers") == "🥩"

def test_type():
    assert type("sit down") == "🍴"
    assert type("take out") == "🥡"
    assert type("fast food") == "🍔"

@pytest.fixture
def get_fix():
    get = test_dict
    return get

def test_main(get_fix):
    assert get_fix == {"name" : "Chopped", "eat_how" : "sit down", "category" : "light-healthy"}

def test_rest_pick(get_fix):
    assert "sit down" == get_fix["eat_how"]
    assert "light-healthy" == get_fix["category"]
    assert "Chopped" == get_fix["name"]







