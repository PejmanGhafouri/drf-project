# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from blog.models import Article
from rest_framework.permissions import IsAdminUser
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
    lookup_field ='slug'
    permission_classes = (IsStaffOrReadOnly , IsAuthorOrReadOnly) 
    
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,) 
    
    
class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)