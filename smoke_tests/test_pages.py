from datetime import timedelta
from django.conf import settings
from django.test import Client, TestCase
from django.utils import timezone
from article.models import Post

class PageSmokeTests(TestCase):
    def test_database_is_memory_only(self):
        self.assertIn('memory', settings.DATABASES['default']['NAME'])

    def test_empty_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Welcome to MyBlog')
        self.assertEqual(list(response.context['posts']), [])

    def test_post_order_is_newest_first(self):
        older = Post.objects.create(title='older', slug='older', content='synthetic')
        newer = Post.objects.create(title='newer', slug='newer', content='synthetic')
        Post.objects.filter(pk=older.pk).update(pub_date=timezone.now()-timedelta(days=1))
        response = self.client.get('/')
        self.assertEqual(list(response.context['posts']), [newer, older])

    def test_title_html_is_escaped(self):
        Post.objects.create(title='<script>alert(1)</script>', slug='x', content='synthetic')
        response = self.client.get('/')
        self.assertContains(response, '&lt;script&gt;alert(1)&lt;/script&gt;')
        self.assertNotContains(response, '<script>alert(1)</script>')

    def test_admin_requires_authentication(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/admin/login/?next='))

    def test_admin_login_rejects_missing_csrf(self):
        response = Client(enforce_csrf_checks=True).post('/admin/login/', {
            'username': 'synthetic', 'password': 'not-a-real-password',
        })
        self.assertEqual(response.status_code, 403)
