# from django.shortcuts import render
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.generics import RetrieveAPIView
from blog.models import Article
from rest_framework.viewsets import ModelViewSet
from .permissions import IsStaffOrReadOnly , IsAuthorOrReadOnly,IsSuperuserOrStaffReadOnly
from .serializers import ArticleSerializer,UserSerializer
from django.contrib.auth import get_user_model
# Create your views here.
# class ArticleList(ListCreateAPIView):
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerializer
	
	
# class ArticleDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerializer
# 	lookup_field ='pk'
# 	permission_classes = (IsStaffOrReadOnly , IsAuthorOrReadOnly) 
	

class ArticleViewSet(ModelViewSet):
	
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filterset_fields = ['status', 'author']
	ordering_fields =  ['publish','status']
	ordering = ['-publish']
	search_fields = ['title', 'content','author__username','author__first_name','author__last_name']


	# def get_queryset(self):
	# 	queryset = Article.objects.all()
	# 	status = self.request.query_params.get('status')
	# 	if status is not None:
	# 		queryset = queryset.filter(status=status)

	# 	author = self.request.query_params.get('author')
	# 	if author is not None:
	# 		queryset = queryset.filter(author__username=author)
	# 	return queryset



	def get_permissions(self):

		if self.action in ['list','create']:
			permission_classes = [IsStaffOrReadOnly]
		else:
			permission_classes = [IsStaffOrReadOnly , IsAuthorOrReadOnly ]
		return [permission() for permission in permission_classes]

# class UserList(ListCreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	permission_classes = (IsSuperuserOrStaffReadOnly,) 
	
	
# class UserDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
# 	permission_classes = (IsSuperuserOrStaffReadOnly,)
	

class UserViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	permission_classes = (IsSuperuserOrStaffReadOnly,)



# class AuthorRetrieve(RetrieveAPIView):
# 	queryset = get_user_model().objects.filter(is_staff=True)
# 	serializer_class = AuthorSerializer



# class RevokeToken(APIView):
# 	permission_classes = (IsAuthenticated,)

# 	def delete(self,request):
# 		request.auth.delete()
# 		return Response(status=204)