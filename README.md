# try-django
Learning Django Framework
Author: filopd
NOTES:
1. Create Django Project:
django-admin startproject <PROJECT_NAME> .
2. Execute the website on localhost.
    * python manage.py runserver
        * http://127.0.0.1:8000
3. Check and update the settings
    * Edit file 'settings.py' in folder <PROJECT_NAME>
4. Synch the updated setting in 'settings.py' file.
    * python manage.py migrate
5. Open admin login page.
    * http://127.0.0.1:8000/admin
6. Create a Super User with Admin role.
    * python manage.py createsuperuser
        * http://127.0.0.1:8000/admin/ and try to login with above details.
        * [Stop the server and try this command else you will get an error "auth_user__old"]
        * [I tried to upgrade the django to latest version and tried as suggested but above step is enough i feel.]
        * [Result after updating First and Last name: "The user “filopd” was changed successfully."]
        * [We have used apps 'django.contrib.admin', 'django.contrib.auth']
7. Term 'root' location where manage.py is present.
8. Create apps in your project using startapp command.
    * python manage.py <appname>
        * [This will create a dir in your root with appname and auto gen code inside it.]
9. These apps let you manage the data. Try to edit the models.py file of your app.
10. Create a class and inherit the "models.Model".
    * Create few models.TextField(). You can also provide default values.
11. Assign this app in INSTALLED_APPS ('products',) in setting.py file.
12. Now create migrations inside products app and migrate it.
    * python manage.py makemigrations
    * python manage.py migrate
    * Whenever you change the models.py file then you have two run above 2 commands.
13. Now Register above model by changing the admin.py file.
    * from .models import Product
    * admin.site.register(Product)
14. Above step register will add 'appname' inside http://127.0.0.1:8000/admin/.
15. You can create objects of the above 'appname'.
16. Open the manage.py in InteractiveConsole.
    * python manage.py shell
    * Import the appname class file in it as follows:
        >>> from products.models import Product
    * Get the total count of app objects.
        >>> Product.objects.all()
    * Create new object
        >>> Product.objects.create(title="Product2",description="THis is Second Product",price="99.99",summary="This is average product.")
        <Product: Product object (2)>
    * Now switch to admin page and veriy the objects in app.
    * This useful for adding the data from the backend.
17. In models we have number of field types with their properties as per the data type (can refer documentation).
18. If there is any modifications in the model fields then you have two ways.
    1. Set default:
        * You can set the value of this new field as default for older records.
        * You will be prompted when you run makemigrations.
        * This will create one more <*>_initial.py file in migrations dir.
    2. You can also update the existing <*>_initial.py in migration dir.
        * makemigrations will compare the fields in intial.py and model.py files.
19. There are many input params out of which 'blank' and 'null' are useful.
    * blank 
        * = True : This field can be kept empty while providing the values.
        * = False : This field is mandatory and required while saving record.
    * null 
        * = True : This field can be kept as null in the db.
        * = False : This field can not be kept as null in the db.
20. Create a View for Home Page.
    * Create a new app called pages. Edit the views.py file and enter details as follows:
    1. Import HttpResonse from django.http
        * from django.http import HttpResponse
    2. Create  simple function as follows: 
        * def home_view(*args, **kwargs):
            return HttpResponse("<H6>This is View</H6>")
    3. Update the urls.py inside project.
        1. import the view from pages app library. Note this gives error for package import but this works fine for me now. Strange !!!
            * from pages import views
        2. Add inside urlpatterns
            * path('', views.home_view, name='home'),
        3. You can take reference from above documentation inside urls.py
21. Inside view function, try to add one more parameter request with existing *args, **kwargs.
    * Both *args and **kwargs will return empty. We are not passing any inputs while opening home page.
    * Parameter request will return '<WSGIRequest: GET '/'>'
    * Parameter request.user will return the user name which is currenlty logged in the browser.
    * Parameter request.user will return "AnonymousUser" if it is opened in incognito mode.
22. To add a sample home.html file as a template.
    1. Create dir (any) templates in root folder and create a simple html in it.
    2. In setting.py, update the TEMPLATES as 
        * "'DIRS': [os.path.join(BASE_DIR, "templates")],"
    3. Now go to views.py of pages app and set the last line of home_view function as 
        * "return render(request, "home.html", {})"



