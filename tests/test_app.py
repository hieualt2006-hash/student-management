import unittest
from app import get_students, get_student, search_students

class TestApp(unittest.TestCase):
    def test_get_students(self):
        self.assertEqual(len(get_students()), 2)

    def test_get_student_found(self):
        student = get_student(1)
        self.assertIsNotNone(student)
        self.assertEqual(student["name"], "Nguyen Van A")

    def test_get_student_not_found(self):
        student = get_student(999)
        self.assertIsNone(student)

    def test_search_students(self):
        result = search_students("nguyen")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)

if __name__ == "__main__":
    unittest.main()
