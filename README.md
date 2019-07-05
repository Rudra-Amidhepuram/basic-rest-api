# Django Rest-Framework
## Installation
we can install django using pip



```python
pip install django==2.2.3
```
Afrer installing django we have to start a project 
```python
django-admin startproject projectname
```
As soon as we have a project folder we need to start an application in our project 
```python
cd prjectname 
django-admin startapp app_name
```
After that we need to install rest_framework
```python
pip install pip install djangorestframework

```
Add 'rest_framework' and 'app_name'to your INSTALLED_APPS setting.
```python 
INSTALLED_APPS = (
    ...
    'rest_framework',
    'webapp'  #app_name
)
 ```
Now build your model.py,views.py,urls.py

## model.py
```python 

from django.db import models
#from django.contrib.auth.models import AbstractUser

class user(models.Model):

	name=models.CharField(max_length=200)
	p_name=models.CharField(max_length=50)
	mobile= models.IntegerField()
```

## views.py
```python 

from django.shortcuts import render
from rest_framework import generics
from .models import user
from .import models
from .import serializers
from .serializers import userList
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
# queryset = user.objects.all()
#serializer_class = userList

class userView(APIView):                                #generics.ListAPIView
 
    def get(self, request, format=None):
         users = user.objects.all()
         serializer = userList(users, many=True)
         return Response(serializer.data)

    def post(self, request, format=None):
        serializer = userList(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
	
class DeleteAPIView(APIView):
	def get(self, request, *args, **kwargs):
     
         try:
            users = request.users
            instance = user.objects.get(users=users)
            instance.delete()
            return Response({"message":"deleted successfuly"}, status=status.HTTP_200_OK)
         except:
            return Response({"message":"delete fail"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(generics.UpdateAPIView):
        queryset = user.objects.all()
        serializer_class = userList

        def update(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.name = request.data.get("name")
            instance.p_name = request.data.get("p_name")
            instance.mobile = request.data.get("mobile")
            #instance.last_updated_on = request.data.get("last_updated_on")
            instance.save()
            serializer = self.get_serializer(instance)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
```
## urls.py
```python 
from django.urls import path,include
from .views import userView,DeleteAPIView,UpdateView

urlpatterns = [
    path('user/', userView.as_view(), name="users-all"),
	path('delete/', DeleteAPIView.as_view(), name='delete'),
	path('update/',UpdateView.as_view(),name="update-data")
	
]
```

## Register your model in admin.py page
```python 
from django.contrib import admin

from .models import	user

admin.site.register(user)
```

That's it, we're done!, runserver using
```python 
python manage.py runserver
```
You can now open the API in your browser at http://127.0.0.1:8000/, and view your new 'users' API.
