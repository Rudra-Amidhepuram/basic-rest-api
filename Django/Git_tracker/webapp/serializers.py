from rest_framework import serializers
from .models import user

class userList(serializers.ModelSerializer):

	class Meta:
		model=user
		fields=('id','name','p_name','mobile')