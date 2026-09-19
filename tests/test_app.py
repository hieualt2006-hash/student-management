from app import get_students, get_student, search_students

def test_get_students():
    assert len(get_students()) == 2

def test_get_student_found():
    assert get_student(1)["name"] == "Nguyen Van A"

def test_get_student_not_found():
    assert get_student(99) is None

def test_search_students():
    result = search_students("nguyen")
    assert len(result) == 1
    assert result[0]["name"] == "Nguyen Van A"
