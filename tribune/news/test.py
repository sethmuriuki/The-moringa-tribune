from django.test import TestCase
from .models import Editor,Articles,tags


class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.seth= Editor(first_name = 'Seth', last_name ='Muriuki', email ='sethmrk@gmail.com')

    # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.seth,Editor))

     # Testing Save Method
    def test_save_method(self):
        self.seth.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticlesTestClass(TestCase):

    def setUp(self):
        # Creating a new Editor and saving it
        self.seth = Editor(first_name = 'Seth', last_name = 'Muriuki', email = 'sethmrk@gmail.com')
        self.seth.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Articles', post = 'This is a random test post', editor = self.seth)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.today_news()
        self.assertTrue(len(today_news)>0)