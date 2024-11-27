from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Collection

class CollectionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book = Book.objects.create(title="Test Book", author="Author")
        self.client.login(username='testuser', password='testpassword')

    def test_create_collection(self):
        response = self.client.post('/api/collections/', {'name': 'My Collection'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Collection.objects.count(), 1)
        self.assertEqual(Collection.objects.first().user, self.user)

    def test_add_book_to_collection(self):
        collection = Collection.objects.create(user=self.user, name='My Collection')
        response = self.client.patch(f'/api/collections/{collection.id}/', {'books': [self.book.id]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.book, collection.books.all())
