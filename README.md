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
Edit file 'settings.py' in folder "<PROJECT_NAME>"
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

