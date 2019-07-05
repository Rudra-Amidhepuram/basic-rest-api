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