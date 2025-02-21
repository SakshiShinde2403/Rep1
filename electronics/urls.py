from django.urls import path # type: ignore
from electronics import views


urlpatterns = [
    path('',views.home, name='home')
]