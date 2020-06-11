from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

# post text mesajarın doğruluğunu kotrol eder
class PostModelTest(TestCase):
    #test ama.lı oluşturulan post
    #text değeri atanıyor
    def setUp(self):
        Post.objects.create(text='deneme text')
    
    #asıl test oluşturulan post text ile beklenen post textin eşitliğini kontrol eder
    def test_text_content(self):
        post = Post.objects.get(id=1)
        beklenen = f'{post.text}'
        self.assertEqual(beklenen,'deneme text')
    
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'home.html')