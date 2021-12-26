# from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
from blog.models import Article
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import IsStaffOrReadOnly , IsAuthorOrReadOnly,IsSuperuserOrStaffReadOnly
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth.models import User
# Create your views here.
class ArticleList(ListCreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	
	
class ArticleDetail(RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field ='pk'
	permission_classes = (IsStaffOrReadOnly , IsAuthorOrReadOnly) 
	
class UserList(ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperuserOrStaffReadOnly,) 
	
	
class UserDetail(RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperuserOrStaffReadOnly,)
	

# class RevokeToken(APIView):
# 	permission_classes = (IsAuthenticated,)

# 	def delete(self,request):
# 		request.auth.delete()
# 		return Response(status=204)