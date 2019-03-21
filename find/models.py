from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from django.utils import timezone

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True, default='profile_images/default.png')

	def __str__(self):
		return self.user.username

class Discount(models.Model):
	name = models.CharField(max_length=32, unique=False)
	image = models.ImageField(upload_to='game_images', blank=True, default='game_images/initial.jpg')
	description = models.CharField(max_length=2000, unique=False)
	price = models.CharField(max_length=32, unique=False)
	reviews = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	numberratings = models.IntegerField(default=0)
	avgrating = models.FloatField(blank=True, null=True, default=0)
	popularity = models.IntegerField(default=0)
	broken = models.BooleanField(default='False')
	judgediscount = models.BooleanField(default='False')
	url = models.URLField(max_length=200,help_text="Please enter the URL of the page.")
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.id)
		super(Discount, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Review(models.Model):
	title = models.CharField(max_length=32, unique=False) 
	datetime = models.DateTimeField(("Date"), default=timezone.now)
	text = models.CharField(max_length=250, unique=False) 
	user = models.ForeignKey(UserProfile)
	game = models.ForeignKey(Discount)

	def __str__(self):
		return self.title

class Rating(models.Model): 
	datetime = models.DateTimeField(("Date"), default=timezone.now)
	points = models.IntegerField(default=0, blank=False, null=False)
	user = models.ForeignKey(UserProfile)
	game = models.ForeignKey(Discount, related_name='+')

	def __str__(self):
		return self.game.name

# Create your models here.
