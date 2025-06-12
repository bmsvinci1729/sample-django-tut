from django.urls import path
from . import views # includeing all      our views here

urlpatterns = [
    path('', views.post_list, name = 'post_list'), # 
] 
