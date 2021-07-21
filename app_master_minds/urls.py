from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('home', views.home),
    path('create_page', views.create_page),
    path('create_quiz', views.create_quiz),
    path('account', views.account),
    path('view_quiz/<int:quiz_id>', views.view_quiz),
    path('edit_page/<int:quiz_id>', views.edit_page),
    path('edit_quiz/<int:quiz_id>', views.edit_quiz),
    path('delete/<int:quiz_id>', views.delete),
    path('logout', views.logout),
]