import django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from find.models import UserProfile, Discount, Review, Rating

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def populate(self): 
		userprofile1 = UserProfile(
			user = User.objects.get(id=1),
			picture = 'profile_images/default.png',
			)
		userprofile1.save()

		userprofile2 = UserProfile(
			user = User.objects.get(id=2),
			picture = 'profile_images/default2.png',
			)
		userprofile2.save()

		userprofile3 = UserProfile(
			user = User.objects.get(id=3),
			picture = 'profile_images/default3.gif',
			)
		userprofile3.save()

		userprofile4 = UserProfile(
			user = User.objects.get(id=4),
			picture = 'profile_images/default4.png',
			)
		userprofile4.save()

		userprofile5 = UserProfile(
			user = User.objects.get(id=5),
			picture = 'profile_images/default5.png',
			)
		userprofile5.save()

	def handle(self, *args, **options):
		self.populate()