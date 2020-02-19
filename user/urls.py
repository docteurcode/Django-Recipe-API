from django.urls import path
from .views import UserApiView, AuthTokenView, MenageUserApiView

app_name = 'user'

urlpatterns = [
    path("create/", UserApiView.as_view(), name="create"),
    path("token/", AuthTokenView.as_view(), name="token"),
    path("me/", MenageUserApiView.as_view(), name="me"),
]
