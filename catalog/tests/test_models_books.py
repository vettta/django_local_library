from django.test import TestCase

# Create your tests here.

from catalog.models import Book

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Book.objects.create(title='Big Red House')

    def test_title_label(self):
        book=Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_title_max_length(self):
        book=Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length,200)

    def test_object_name_is_language_comma_title(self):
        book=Book.objects.get(id=1)
        expected_object_name = '%s, %s' % (book.language, book.title)
        self.assertEquals(expected_object_name,str(book))

    def test_get_absolute_url(self):
        book=Book.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(book.get_absolute_url(),'/catalog/book/1')