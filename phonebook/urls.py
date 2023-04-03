from django.urls import path
from .views import *


urlpatterns = [
    path("",VcardList.as_view()),
    path("<int:id>/",VcardDetails.as_view())
]
