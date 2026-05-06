from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import PostListView,PostDetailView

# Create your tests here.

class TestUrl(SimpleTestCase):

    def test_blog_post_list_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEqual(resolve(url).func.view_class,PostListView)

    def test_blog_post_detail_url_resolve(self):
        url = reverse('blog:post-detail',kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class,PostDetailView)