import os
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import UploadedImage

class ImageUploadTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.url = '/image-upload/upload/'

    def test_upload_image_basic(self):
        self.client.login(username='testuser', password='password')
        file_path = os.path.join(os.path.dirname(__file__), 'test.jpg')
        with open(file_path, 'rb') as image:
            response = self.client.post(self.url, {'image': image}, format='multipart')
        self.assertEqual(response.status_code, 201)

    def test_upload_image_invalid_format(self):
        self.client.login(username='testuser', password='password')
        file_path = os.path.join(os.path.dirname(__file__), 'invalid.txt')
        with open(file_path, 'rb') as image:
            response = self.client.post(self.url, {'image': image}, format='multipart')
        self.assertEqual(response.status_code, 400)

    def test_upload_image_unauthenticated(self):
        file_path = os.path.join(os.path.dirname(__file__), 'test.jpg')
        with open(file_path, 'rb') as image:
            response = self.client.post(self.url, {'image': image}, format='multipart')
        self.assertEqual(response.status_code, 403)


class ImageListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.url = '/image-upload/list-images/'

    def test_list_images_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_list_images_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)


class ThumbnailGenerationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.image = UploadedImage.objects.create(user=self.user, image='test.jpg')
        self.url = f'/image-upload/thumbnail/{self.image.id}/200/200/'

    def test_generate_thumbnail_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'image/jpeg')

    def test_generate_thumbnail_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)


class ExpiringLinkGenerationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.image = UploadedImage.objects.create(user=self.user, image='test.jpg')
        self.url = f'/image-upload/expiring-link/{self.image.id}/3600/'

    def test_generate_expiring_link_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('expiring_link', response.data)

    def test_generate_expiring_link_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
