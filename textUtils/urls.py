from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls), # this is taking us to admin pannel 
    path('', include("textApp.urls")), # this is taking us to the app's urls.py here dbCrude is app name 
]
                