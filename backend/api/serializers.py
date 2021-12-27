from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ['id','username','first_name','last_name']

class ArticleSerializer(serializers.ModelSerializer):
	
	# author = AuthorSerializer()
	author = serializers.HyperlinkedIdentityField(view_name='api:author-detail')
	class Meta:
		model = Article
		# fields = ('title','slug','author','content','publish','status')  #selected fields
		# exclude = ('created','updated') #all fields except ...
		fields = '__all__'
		
	def validate_title(self, value):
		filter_list = ['javascript','PHP','laravel']

		for i in filter_list:
			if i in value.lower():
				raise serializers.ValidationError("You Used Forbidden Word :{}".format(i))
		
		
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		# fields = ('title','slug','author','content','publish','status')  #selected fields
		# exclude = ('created','updated') #all fields except ...
		fields = '__all__'
