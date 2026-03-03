from django.urls import path
from . import views
from .views import PostDeleteView ,register,PostCreateView,PostUpdateView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('create/',PostCreateView.as_view(),name='create_post'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post_delete"),
    path('register/',views.register,name="register"),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
]
