from django.urls import path
from . import views

app_name = 'blog'  # optional but helpful for namespacing

urlpatterns = [
    path('', views.post_list, name='post_list'),
]