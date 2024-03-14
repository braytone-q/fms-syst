from django.urls import path
from .views import UserList, AuthUserLoginView, UserListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("register/", UserList.as_view(), name="register"),
    path("login/", AuthUserLoginView.as_view(), name="login"),
    path("users/", UserListView.as_view(), name="users"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
