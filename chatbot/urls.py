from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', view=views.index, name='index'),
    # path('article/<int:article_id>', views.article, name ='article')
    path('getResponse', view=views.getResponse,name='getResponse'),
    path('login/', view=views.CustomLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', view=views.RegisterPage.as_view(), name = 'register'),
]