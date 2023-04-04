from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("",VcardList.as_view()),
    path("<int:id>/",VcardDetails.as_view()),
    path("login/", MyObtainTokenPairView.as_view()),
    path("login/refresh/", TokenRefreshView.as_view()),
    path("register/", RegisterView.as_view()),
]
