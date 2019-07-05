from django.urls import path,include
from .views import userView,DeleteAPIView,UpdateView
#from rest_framework import viewset





urlpatterns = [
    path('user/', userView.as_view(), name="users-all"),
	path('delete/', DeleteAPIView.as_view(), name='delete'),
	path('update/',UpdateView.as_view(),name="update-data")
	#path('create/', createU.as_view(), name="create"),
]