from django.test import TestCase
from .models import Post
# Create your tests here.


class ModelTesting(TestCase):
    def setUp(self):
        self.blog = Post.objects.create(
            title="Testing Title", author="Sunag", slug="Sunag")

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'Testing Title')
