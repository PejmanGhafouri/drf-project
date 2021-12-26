from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ('title','slug','author','content','publish','status')  #selected fields
        # exclude = ('created','updated') #all fields except ...
        fields = '__all__'
        
        
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = ('title','slug','author','content','publish','status')  #selected fields
        # exclude = ('created','updated') #all fields except ...
        fields = '__all__'
