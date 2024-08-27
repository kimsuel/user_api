from django.test import TestCase
from rest_framework import status

from api.models import User, Address


class UserTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(email='user1@test.com', username='user1', name='일유저', password='1111')
        user2 = User.objects.create_user(email='user2@test.com', username='user2', name='이유저', password='1111')
        user3 = User.objects.create_user(email='user3@test.com', username='user3', name='삼유저', password='1111')

        Address.objects.create(user=user1, address='경기도 광주시')
        Address.objects.create(user=user2, address='서울시 양천구')
        Address.objects.create(user=user3, address='인천광역시 간석동')

    def test_list(self):
        response = self.client.get('/api/address')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(len(response_data), Address.objects.count())

    def test_retrieve(self):
        user1 = User.objects.get(username='user1')
        addr = Address.objects.get(user=user1)
        response = self.client.get(f'/api/address/{addr.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['address'], Address.objects.get(pk=addr.pk).address)

    def test_update(self):
        user2 = User.objects.get(username='user2')
        addr = Address.objects.get(user=user2)

        response = self.client.put(f'/api/address/{addr.id}',
                                   data={'address': '서울시 강남구'}, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['address'], '서울시 강남구')

    def test_delete(self):
        user3 = User.objects.get(username='user3')
        addr = Address.objects.get(user=user3)

        response = self.client.delete(f'/api/address/{addr.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

