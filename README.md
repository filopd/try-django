# try-django
Learning Django Framework
Author: filopd
NOTES:
1. Create Django Project:
django-admin startproject <PROJECT_NAME> .
2. Execute the website on localhost.
python manage.py runserver
   http://127.0.0.1:8000
3. Check and update the settings
Edit file 'settings.py' in folder <PROJECT_NAME>
4. Synch the updated setting in 'settings.py' file.
python manage.py migrate
5. Open admin login page.
   http://127.0.0.1:8000/admin
6. Create a Super User with Admin role.
python manage.py createsuperuser
   http://127.0.0.1:8000/admin/ and try to login with above details.
   [Stop the server and try this command else you will get an error "auth_user__old"]
   [I tried to upgrade the django to latest version and tried as suggested but above step is enough i feel.]
   [Result after updating First and Last name: "The user “filopd” was changed successfully."]
   [We have used apps 'django.contrib.admin', 'django.contrib.auth']
7. Term 'root' location where manage.py is present.
8. Create apps in your project using startapp command.
python manage.py <appname>
   [This will create a dir in your root with appname and auto gen code inside it.]
9. These apps let you manage the data. Try to edit the models.py file of your app.
10. Create a class and inherit the "models.Model".
   Create few models.TextField(). You can also provide default values.
11. Assign this app in INSTALLED_APPS ('products',) in setting.py file.
12. Now create migrations inside products app and migrate it.
python manage.py makemigrations
python manage.py migrate
   Whenever you change the models.py file then you have two run above 2 commands.
13. Now Register above model by changing the admin.py file.
   from .models import Product
   Register your models here.
   admin.site.register(Product)
14. Above step register will add 'appname' inside http://127.0.0.1:8000/admin/.

