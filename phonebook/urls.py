from django.urls import path
from .views import *


urlpatterns = [
    path("",VcardList.as_view())
]
