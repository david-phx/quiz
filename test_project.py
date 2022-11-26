import pytest
from project import get_filename, get_quiz, hr


def test_get_filename():
    assert get_filename(["project.py", "quiz.json"]) == "quiz.json"
    assert get_filename(["project.py", "test.json"]) == "test.json"


def test_get_filename_emtpy():
    with pytest.raises(SystemExit):
        get_filename(["project.py"])


def test_get_filename_too_many():
    with pytest.raises(SystemExit):
        get_filename(["project.py", "foo", "bar"])


def test_get_quiz():
    with pytest.raises(SystemExit):
        get_quiz("quiz.foo")


def test_get_quiz_not_found():
    with pytest.raises(SystemExit):
        get_quiz("foo.json")


def test_hr():
    assert hr() == "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
    assert hr("=", 10) == "=========="
    assert hr("-", 20) == "--------------------"
