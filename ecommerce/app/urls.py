from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('singleproduct/<str:pk>',views.singleproduct,name='singleproduct'),
    path('checkout/',views.checkout,name='checkout'),
    
]
