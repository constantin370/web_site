from django.urls import path

from main_application.views.index_view import index


app_name = 'main_application'

urlpatterns = [
    path('', index, name='index'),
    ]