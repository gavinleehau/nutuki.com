from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('userpage/',views.userPage, name='userpage'),
    # re_path(r"^userpage/updateUser/(?P<pk>[0-9]+)$", views.UserUpdateView.as_view(), name='updateUser'),
    re_path(r"^userpage/updateUser", views.user_update, name='updateUser'),

    path('register',views.register_user, name='register'),
    path('login',views.login_user, name='login' ),
    path('logout',auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]