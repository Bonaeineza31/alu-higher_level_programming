#!/usr/bin/python3
"""
Unit tests for the Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_auto_increment(self):
        """
        Test automatic ID incrementation.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_explicit(self):
        """
        Test explicit ID assignment.
        """
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_to_json_string(self):
        """
        Test JSON string serialization.
        """
        data = [{"id": 1}, {"id": 2}]
        json_data = Base.to_json_string(data)
        self.assertEqual(json_data, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """
        Test JSON string deserialization.
        """
        json_data = '[{"id": 1}, {"id": 2}]'
        data = Base.from_json_string(json_data)
        self.assertEqual(data, [{"id": 1}, {"id": 2}])


if __name__ == "__main__":
    unittest.main()
    