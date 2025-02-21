from django.urls import path # type: ignore
from grocery import views


urlpatterns = [
    path('grocery/',views.grocery, name='grocery')
]