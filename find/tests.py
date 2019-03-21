from django.test import TestCase
from find.models import UserProfile, Discount, Review, Rating
from django.contrib.auth.models import User
from django.urls import reverse



class DiscountTest(TestCase):
    def setUp(self):
        Discount.objects.create(
            name='Hellblade: Senuas Sacrifice',
            description='Hellblade: Senuas Sacrifice is a dark fantasy action-adventure game developed and published by the British video game development studio Ninja Theory. Self-described as an "independent AAA game", it was created by a team of approximately twenty developers led by writer and director Tameem Antoniades. It was released worldwide for Microsoft Windows and PlayStation 4 in August 2017, with an Xbox One version in April 2018. The game features support for virtual reality, which was added in an update in 2018. A Nintendo Switch version is planned for a Spring 2019 release.',
            image='game_images/default.jpg',
            price='original £24.99,now at £12.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            judgediscount=True,
            url='https://www.youtube.com/embed/HVWigiK4NTs')
    def test_ensure_name_is_not_none(self):
        x=Discount.objects.get(url='https://www.youtube.com/embed/HVWigiK4NTs')
        self.assertIsNotNone(x.name)
    def test_ensure_description_is_not_none(self):
        x=Discount.objects.get(name='Hellblade: Senuas Sacrifice')
        self.assertIsNotNone(x.description)
    def test_ensure_image_is_not_none(self):
        x=Discount.objects.get(name='Hellblade: Senuas Sacrifice')
        self.assertIsNotNone(x.image)
    def test_ensure_price_is_not_none(self):
        x=Discount.objects.get(name='Hellblade: Senuas Sacrifice')
        self.assertIsNotNone(x.price)
    def test_ensure_reviews_is_not_none(self):
        x=Discount.objects.get(name='Hellblade: Senuas Sacrifice')
        self.assertIsNotNone(x.reviews)
    def test_ensure_rating_is_not_none(self):
        x=Discount.objects.get(name='Hellblade: Senuas Sacrifice')
        self.assertIsNotNone(x.rating)
    def test_ensure_url_is_not_none(self):
        x=Discount.objects.get(name='Hellblade: Senuas Sacrifice')
        self.assertIsNotNone(x.url)


class IndexViewTests(TestCase):
    def test_index_view(self):
        response=self.client.get(reversed('index'))
        self.assertEqual(response.status_code,200)
    def test_game_view(self):
        response=self.client.get(reversed('game'))
        self.assertEqual(response.status_code,200)
    def test_contact_view(self):
        response=self.client.get(reversed('contact'))
        self.assertEqual(response.status_code,200)
    def test_login_view(self):
        response=self.client.get(reversed('login'))
        self.assertEqual(response.status_code,200)
    def test_logout_view(self):
        response=self.client.get(reversed('logout'))
        self.assertEqual(response.status_code,200)
    def test_submit_view(self):
        response=self.client.get(reversed('submit'))
        self.assertEqual(response.status_code,200)
    def test_register_view(self):
        response=self.client.get(reversed('register'))
        self.assertEqual(response.status_code,200)
    def test_submitted_view(self):
        response=self.client.get(reversed('submitted'))
        self.assertEqual(response.status_code,200)
    def test_gamelist_view(self):
        response=self.client.get(reversed('gamelist'))
        self.assertEqual(response.status_code,200)


