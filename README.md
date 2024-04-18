gas utility company project
This web application is designed to streamline the process of submitting and tracking service requests for gas utilities, providing both customers and support representatives with an efficient and user-friendly platform.
Features:
For Customers:
Service Requests: Submit service requests online, including selecting the type of request, providing details, and attaching files.
Request Tracking: Track the status of submitted service requests, view submission timestamps, and monitor resolution progress.
View their account information.

**** STRUCTURE OF DJANGO APPLICATION CODEBASE ****
Implemented Model-View-Template (MVT) architectural pattern
1) Project Directory:
   This is the main directory containing the entire Django project.
   here, 'bynry/'

 2) Django App Directory:
   Inside the project directory, can have one or more Django applications.
   here 'home/'

 3) Settings:
    settings.py: Configuration settings for the Django project.
    It includes database configuration, static files, middleware, and more.

 4) URLs:
    urls.py: Contains URL patterns for the entire project or individual apps.
    Routes requests to the appropriate view functions.

 5) Static Files:
    Directory for static files such as CSS, JavaScript, and images.
    Usually located in each app's directory or a common directory.

 6) Templates:
    Directory for HTML templates used by Django views.
    Also usually located in each app's directory or a common directory.

 7) Models:
    models.py: Contains database models (classes) defined using Django's ORM.
    Defines the structure and behavior of data stored in the database.

 8) Views:
    views.py: Contains view functions or classes that handle requests and return responses.
    May contain logic for processing requests, interacting with models, and rendering templates.

 9) Admin Configuration:
    admin.py: Configuration for Django's admin interface.
    Allows you to register models for administration.

 10) makemigrations and migrate:
     makemigrations and migrate are two commands used in conjunction with Django's ORM (Object-Relational Mapping) system to manage database schema changes.

