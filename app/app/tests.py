from django.test import TestCase
from app.calc import add
from app.calc import subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)

    def test_subtract_numbers(self):
        """Test that two numbers are subtracted together"""
        self.assertEqual(subtract(5,11),-6)
        self.assertEqual(subtract(12,11),1)
    