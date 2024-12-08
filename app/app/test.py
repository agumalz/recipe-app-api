""" 
Sample Test
"""

from django.test import SimpleTestCase

from app import calc

class ClacTest(SimpleTestCase):
    def test_add_number(self):
        result = calc.add(5, 6)
        
        self.assertEqual(result, 11)
        
    def test_subtract_numbers(self):
        """Test Subtract numbers."""
        result = calc.subtract(10, 15)
        
        self.assertEqual(result, 5)
