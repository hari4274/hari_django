Sample Django project - For development
----------------------------------------

Install setuptools

	sudo apt-get install python-setuptools

Install Django

	sudo pip3 install Django==2.1.5

Check Django version

	python3 -m django --version

Create Project

	django-admin startproject sample_site

Goto project

	cd sample_site/

Run Django project

	python3 manage.py runserver

Update Project:

	python3 manage.py migrate

To Create New app

	python3 manage.py startapp daily_status

Create Admin User

	python3 manage.py createsuperuser

		username : admin
		password : admin

Make database upgrades

	python3 manage.py makemigrations daily_status

To Check last updated

	python3 manage.py sqlmigrate daily_status 0001

To Collect Static Files
	Note: 
	Before add line the following "sample_site/settings.py",
	STATIC_ROOT = BASE_DIR + '/static/'
        
    python3 manage.py collectstatic