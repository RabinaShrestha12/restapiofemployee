from rest_framework import serializers
from .models import Employee
# from django.contrib.auth.models import User
from .models import Category,CustomUser, Product
from django.contrib.auth import get_user_model

User = get_user_model()
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_title = serializers.CharField(source='category.title', read_only = True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'category', 'user', 'created_at', 'updated_at', 'category_title']
        read_only_fields = ['id', 'user', 'created_at','category_title']
