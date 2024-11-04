from django.urls import path
from .views.auth_view import renderRegisterForm,  renderLoginForm
from  .views.home_view import renderHomepage


urlpatterns = [
    path('register',renderRegisterForm),
    path('login', renderLoginForm),
    path('index', renderHomepage),
]
