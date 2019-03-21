#Forms isn't needed but helps with tidyness, could otherwise put in models.py
#1.) Create a model form class for each model to be rep as form
#2.) Customize forms
#3.) Create/update view to handle form
	#need to display form
	#need to save form data
	#need to flag errors if user input wrong info
#4.) Create/update template to display form
#5.) Add urlpatter to map to new view

#1.) ModelForm-helper class to create form from pre-existing model
from django import forms
from django.contrib.auth.models import User
from find.models import UserProfile, Discount, Review, Rating
from django.utils import timezone


class UserForm(forms.ModelForm):
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'size':40, 'placeholder':'Password'}))
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'help_text':None,'size':40, 'placeholder':'Username'}))
	class Meta:
		model = User
		fields =('username', 'email', 'password') 
		labels={'email':'',}
		widgets ={
			'email': forms.TextInput(attrs={'size':40,'placeholder':'Email'}),
		}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)

class ReviewForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={'size':40, 'placeholder':'Title'}))
	text = forms.CharField(label = '', widget=forms.Textarea(attrs={'style': 'border-color: gainsboro;', 'cols': 38, 'rows': 5, 'placeholder':'Do you enjoy using this water game? Enter your opinion here then hit "Submit a review".'}))
	class Meta:
		model = Review
		fields =('title', 'text',)

class RatingForm (forms.ModelForm):
	points = forms.ChoiceField(choices=[(x,x) for x in range (1,6)])
	class Meta: 
		model = Rating
		fields = ('points',)

class DiscountForm (forms.ModelForm):
	name = forms.CharField(label='', widget=forms.TextInput(attrs={'help_text':None,'size':40, 'placeholder':'Game_name'}))
	price = forms.CharField(label='', widget=forms.TextInput(attrs={'help_text':None,'size':40, 'placeholder':'Price'}))
	description = forms.CharField(label='', widget=forms.TextInput(attrs={'help_text':None,'size':40, 'placeholder':'Description'}))
	Is_Discount = forms.BooleanField()
	class Meta:
		model = Discount
		fields = ('name', 'price', 'description', 'image')

class BrokenDiscountForm (forms.ModelForm):
	broken = forms.BooleanField()
	class Meta:
		model = Discount
		fields = ('broken',)
	