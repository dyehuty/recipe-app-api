from django.test import TestCase

from app.calc import add, substract

class CalcTEsts(TestCase):
    
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)
        """docker-compose run app sh -c "python manage.py test"""

    def test_substract_numbers(self):
        """Test that values are substracted and returned"""
        self.assertEqual(substract(5,11),6)
        """docker-compose run app sh -c "python manage.py test && flake8"""