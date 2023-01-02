from django.urls import path
from .import views
from django.contrib.auth import views as auth_view  
from .forms import LoginForm,MyPasswordResetForm

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('singleproduct/<str:pk>',views.singleproduct,name='singleproduct'),
    path('checkout/',views.checkout,name='checkout'),
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.adress,name='address'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path("logout/",  views.logout, name="logout")
]
