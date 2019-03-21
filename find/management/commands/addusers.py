import django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from find.models import UserProfile, Discount, Review, Rating

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def populate(self): 
		user1 = User(
			id=1,
			username = 'thirsty_student111', 
			email = 'dummy@dummy.com',
			password = 'gLV3cY**************************************',
			)
		user1.save()

		user2 = User(
			id=2,
			username = 'skullboy666', 
			email = 'dummy1@dummy.com',
			password = 'gLV3cY**************************************',
			)
		user2.save()

		user3 = User(
			id=3,
			username = 'waternaut', 
			email = 'dummy2@dummy.com',
			password = 'gLV3cY**************************************',
			)
		user3.save()

		user4 = User(
			id=4,
			username = 'ron_not_poet', 
			email = 'dummy3@dummy.com',
			password = 'gLV3cY**************************************',
			)
		user4.save()

		user5 = User(
			id=5,
			username = 'PHP_RULES', 
			email = 'dummy4@dummy.com',
			password = 'gLV3cY**************************************',
			)
		user5.save()

	def handle(self, *args, **options):
		self.populate()