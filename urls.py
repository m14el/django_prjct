from django.contrib import admin
from django.urls import path, include
from . import views


from News.views import HomeNews, NewsByCategory, ViewNews, AddNews, register, user_login, user_logout
#from News.views import index, get_category, view_news, add_news, test




urlpatterns = [
    #path('', index, name='Home'),
    #path('category/<int:category_id>', get_category, name='Category'),
    #path('news/<int:pk>/', view_news, name='view_news'),
    #path('news/add_news', Add_news, name='add_news'),
    # path('test/', test, name='Test')
    path('', views.HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', AddNews.as_view(), name='add_news'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', views.user_logout, name='Logout'),

]


