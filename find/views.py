from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseNotFound
from django.template import RequestContext
from find.forms import UserForm, UserProfileForm, ReviewForm, RatingForm, DiscountForm, BrokenDiscountForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from find.models import Discount
from find.models import Review
from find.models import Rating
from find.models import UserProfile
from django.utils import timezone
from django.contrib import messages


def index(request):
	game_list = Discount.objects.order_by('name').distinct()
	price_list = Discount.objects.order_by('id').distinct()
	reviews = Review.objects.order_by('-datetime')
	ratings = Rating.objects.order_by('-datetime')
	context_dict = {'games': game_list, 'prices': price_list, 'reviews': reviews, 'ratings': ratings}
	review_list=list(reviews)
	rating_list=list(ratings)
	recent_activity = sum([review_list, rating_list], [])
	recent_activity.sort(key=lambda item: item.datetime, reverse=True)

	context_dict = {'games': game_list, 'prices': price_list, 'reviews': review_list, 'activity': recent_activity}

	return render(request, 'find/index.html', context_dict)

def get_game(request, game_id_slug):

	context_dict = {}
	review_form = ReviewForm()
	rating_form = RatingForm()
	brokendiscount_form = BrokenDiscountForm()

	if request.method=='POST' and 'reviewform' in request.POST:
		review_form = ReviewForm(request.POST)
		if review_form.is_valid(): 
			review_form = ReviewForm(request.POST)
			review = review_form.save(commit=False)
			review.user = UserProfile.objects.get(user=request.user)
			review.datetime = timezone.now()
			review.game = Discount.objects.get(id=game_id_slug)
			review.save() 
			return HttpResponseRedirect(reverse('submitted'))

	if request.method=='POST' and 'ratingform' in request.POST:
		rating_form = RatingForm(request.POST)
		if rating_form.is_valid():
			rating_form = RatingForm(request.POST)
			rating = rating_form.save(commit=False)
			rating.user = UserProfile.objects.get(user=request.user)
			rating.datetime = timezone.now()
			rating.game = Discount.objects.get(id=game_id_slug)
			rating.save() 
			return HttpResponseRedirect(reverse('submitted'))

	if request.method == 'POST' and 'broken' in request.POST:
		brokengame_form = BrokenDiscountForm(request.POST)
		game = Discount.objects.get(id=game_id_slug)
		broken = request.POST.get("broken", None) 
		if broken == 'True':
			game.broken = True
		elif broken == 'False':
			game.broken = False
		game.save()
		return HttpResponseRedirect(reverse('submitted'))
					
	try: 
		game = Discount.objects.get(id=game_id_slug)
		reviews = Review.objects.filter(game=game_id_slug).order_by('-datetime')
		ratings = Rating.objects.filter(game=game_id_slug).order_by('-datetime')

		context_dict['game'] = game
		context_dict['reviews'] = reviews
		context_dict['ratings'] = ratings
		context_dict['review_form'] = review_form
		context_dict['rating_form'] = rating_form
	except Discount.DoesNotExist:
		context_dict['game'] = None

	return render(request, 'find/game.html', context_dict)

def about(request):
	return render(request, 'find/about.html')

def page_not_found(request):
	return render(request, HttpResponseNotFound, 'find/404.html')

def contact(request):
	return render(request, 'find/contact.html')

def submit(request):
	if request.method =='POST':
		game_form = DiscountForm(data=request.POST)
		if game_form.is_valid():
			game = game_form.save(commit=False)
			# game.lat = request.POST.get("latitude", None)
			# game.lng = request.POST.get("longitude", None)
			game.judgediscount = request.POST.get('judgediscount')
			game.save()
			return HttpResponseRedirect(reverse('submitted'))
		else:
			print(game_form.errors)
	else:
		game_form = DiscountForm()

	return render(request, 'find/submit.html', {'game_form': game_form})

def submitted(request):
	return render(request, 'find/submitted.html', {})

def register(request):
	registered=False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
			user = user_login(request)
			return HttpResponseRedirect(reverse('index'))
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form=UserProfileForm()

	return render(request,'find/register.html', {'user_form': user_form,
'profile_form': profile_form,
'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your find account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.") 
	else:
		return render(request, 'find/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def page_not_found(request):
	data = {}
	return render(request, 'find/404.html', data)

def server_error(request):
	data = {}
	return render(request, 'find/500.html', data)

def gamelist(request):
	game_list = Discount.objects.order_by('name')
	
	context_dict = {'games': game_list}
	return render(request, 'find/gamelist.html', context_dict)