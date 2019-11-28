# Exercises for revision

1. Getting started

	Install Django

	Init a Django project

	Run default Django project

2. Application and routes

	Create an application inside a project

	Custome routes

3. How backend comunication with frontend: Templates

	Add an application to a list of installed apps

	Parse data from code to template		

		for loop

		if else
	
	Add boostrap to out templates

	Add navigation bar and glocally style your site

		Dont use hard code to reference url in navigation bar

		
4. Admin page

	
5. Databases and migration

	How to create a db models in python code

	How to see migration sql code:

		python manage.py sqlmigrate <app name> <app number>

	How to run migration to db

	Query database
		
		python manage.py shell

	Day formatting to display

	Register database model to admin page

6. User registration

	Use form and validation

	csrf token

	Validation

	Use crispy form
	
		pip install django-crispy-forms

7. Login/logout system

	Check if user are logging in or logging out

8. Degin user profile page

	Use signal to create profile everytime a user is created

9. Update User Profile

	
	Create form for UserUpdate and ProfileUpdate

	Resize avatar to thumbnail

10. Create, Update, and Delete Post

	Class-base view and function-base view

11. Pagination 

12. Password reset

	Create password reset template

	Sending email to guide user reset email

	Understand UIDB64 and TOKEN

	Two steps verifiacation gmail

13. Using AWS S3 for files uploading

	Create IAM user for programmical purpose: access key, secret key

	Using boto3

	Using django-storages

14. Deploy to heroku

	Install heroku CLI then login

		sudo snap install --classic heroku

		heroku login

	Create requirements.txt

	pip install gunicorn

		
