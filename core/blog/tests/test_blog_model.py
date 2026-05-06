from django.test import TestCase
from datetime import datetime

from django.contrib.auth import get_user_model
from ..models import Post, Category
from accounts.models import User, Profile

class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com",password="a/@1234567")
        self.profile = self.user.profile


    def test_create_post_with_valid_data(self):

        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "description",
            status = True,
            category = None,
            published_date = datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title,"test")