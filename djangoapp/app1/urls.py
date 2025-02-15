from django.urls import path
from app1.views import index

app_name = 'app1'

urlpatterns = [
    path('', index, name='index'),
]