from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dash),
    path('trans/', views.trans_list),
]
