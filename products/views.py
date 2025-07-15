from rest_framework import viewsets
from .models import Category, Product 
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class CategoryViewSet(viewsets.ModelViewSet):
    '''
    ViewSet para gerenciar categorias de produtos.
    Permite operações CRUD (Create, Read, Update, Delete).
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny] # Por enquanto permite acesso a todos os usuários

class ProductViewSet(viewsets.ModelViewSet):
    '''
    ViewSet para gerenciar produtos.
    Permite operações CRUD (Create, Read, Update, Delete).
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated] # Apenas usuários autenticados podem acessar produtos