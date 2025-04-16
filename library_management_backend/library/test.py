# tests.py
from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Test Author", isbn="1234567890123")

    def test_book_str_representation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(str(book), "Test Book")