# incomplete
from io import StringIO
import seasons
from datetime import date
from datetime import timedelta
import pytest

year_test = timedelta(days=365)
today_test = date.today()
bday = today_test - year_test
birthday_input = StringIO(bday.isoformat())
bad = StringIO('January 18, 2023\n')


def test_good_get(monkeypatch):
    monkeypatch.setattr('sys.stdin', birthday_input)
    assert seasons.get() == 525600

def test_bad_get(monkeypatch):
    monkeypatch.setattr('sys.stdin', bad)
    assert seasons.get() == None

## reading from stdin while output called error
def test_error_get(monkeypatch):
    with pytest.raises(AttributeError):
        monkeypatch.setattr('sys.stdin', bad)
        get = seasons.get()







