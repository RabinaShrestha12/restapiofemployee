from django.urls import path
from .views.main_views import add_employee,get_employee,update_employee,get_employee_by_id,delete_employee,category_view,category_by_id,product_by_id,product_view,category_with_products,category_list
from .views.auth_view import register_user, login_user


urlpatterns = [
   path('add/', add_employee),
   path('get/', get_employee),
   path('update/<int:id>', update_employee),
   path('get_employee_by_id/<int:employee_id>', get_employee_by_id),
   path('delete/<int:id>', delete_employee),
   path('register/', register_user),
   path('login/', login_user),
   path('category/',category_view),
   path('category/<int:id>', category_by_id),
   path('product/', product_view),
    path('product/<int:id>', product_by_id),
    path('cat/<int:category_id>', category_list),
    path('catpro/', category_with_products)


]
