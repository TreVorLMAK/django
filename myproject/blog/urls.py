from django.urls import path
<<<<<<< HEAD
from .views.auth_view import renderRegisterForm,renderLoginForm
from .views.home_view import home,create_blog,blog_detail, delete_blog
from  django.contrib.auth import views as auth_views

urlpatterns  = [
    path('',home,name="home"),
    path('register',renderRegisterForm), 
    path('login',renderLoginForm), 
    path('logout',auth_views.LogoutView.as_view(),name='logout' ),
    path('create',create_blog), 
    path('<int:blog_id>', blog_detail,name='blog_detail'), 
    path("<int:blog_id>/delete/", delete_blog,name="delete_blog")
]
=======
from .views.auth_view import renderRegisterForm,  renderLoginForm
from  .views.home_view import renderHomepage


urlpatterns = [
    path('register',renderRegisterForm),
    path('login', renderLoginForm),
    path('index', renderHomepage),
]
>>>>>>> c464e3426f14e6979fe4607f8c4da5e52888b5d5
