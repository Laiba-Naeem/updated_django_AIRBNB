from .views import RegisterAPI
from django.urls import path
from accounts.views import LogoutView, UserListView, SpecificUserView, RegisterGoogleSign


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/register/", RegisterAPI.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="accounts_logout"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("specificuser/", SpecificUserView.as_view(), name="specific_user_view"),
    path("registergoogle/", RegisterGoogleSign.as_view(),
         name="registergoogleuser"),
]
