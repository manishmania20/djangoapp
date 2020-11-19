# djangoapp

## Simple Django web application to generate weather report of any city

## Steps
1. Install django python module using pip (given, pip is present on system)
>pip install django

2. Best part of django is it’s automatic admin interface and to create that use
>django-admin startproject newsapp

3. A folder with the name of newsapp is created and along with it certain built-in python files are loaded like manage.py, urls.py, etc.
4. Check if the server is created by executing the command
>python manage.py runserver

5. Now enter http://127.0.0.1:8000/ in the browser and if done properly successful build kind of message is displayed
6. To create app, enter the following command inside newsapp directory
>python manage.py startapp main

7. Goto urls.py in the newsapp subfolder of newsapp and write your code. Basically, a path to the main.urls is added here because this file runs first using port 8000 on loopback address and now it would redirect to urls.py in main subfolder 

8. Goto urls.py in the main subfolder of newsapp and write your code
9. We know that Django app is made upon the Model-View-Template framework and urls.py now loads view form from views.py 
10. Goto views.py and write your code. In the urls.py,  a call was made to views.index i.e. to index function in views and request is the event. User enters the name of the city in a search field and weather for that city is generated.

11. Goto https://openweathermap.org/api to generate your own api key token.
12. After defining our View we now move onto Templates part so inside templates/main/index.html write your code. In this HTML file, JQuery is used for creating this Template or simply the response of the request event in views.py

13. Next save all your content and again execute 
>python manage.py runserver

14. Again goto http://127.0.0.1:8000/ and new Django application has been created
