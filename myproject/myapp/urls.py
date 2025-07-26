from django.urls import path
from .views.main_views import add_employee,get_employee,update_employee,get_employee_by_id,delete_employee
from .views.auth_view import register_user


urlpatterns = [
   path('add/', add_employee),
   path('get/', get_employee),
   path('update/<int:id>', update_employee),
   path('get_employee_by_id/<int:employee_id>', get_employee_by_id),
   path('delete/<int:id>', delete_employee),
   path('register/', register_user)
]
