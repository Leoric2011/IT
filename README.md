Check us out on Python Anywhere at https://find.pythonanywhere.com/

The website makes use of Google Maps geolocation and it is highly recommended to run it as a secure HTTPS site, with location services enabled. 

To Start the Project:

1.) Create a folder on your computer

2.) Create a virtual environment (python -m venv myvenv) MAKE SURE IT IS PYTHON 3.6

3.) On Mac ACTIVATE venv (source myvenv/bin/activate) 
 	On Windows Activate venv (myvenv/Scripts/activate)
	
4.) Clone github repository (git clone https://github.com/dmayers340/itech.git)

5.) CD into itech (cd itech)

6.) Install Django (pip install django~=1.11.0)

7.) pip install pillow

8.) pip install bcrypt

9.) python manage.py makemigrations

10.) python manage.py migrate

11.) python manage.py addgames

12.) python manage.py addusers

13.) python manage.py addprofiles

14.) python manage.py addreviews


Itech Folder Structure:

	-game (PROJECT FOLDER-has settings/urls/wsgi)
	
	-find (app--has app shit)
	
	-static 
	
		-css
		
		-img
		
		-jquery
		
		-js
		
	-templates
	
	-manage.py 

