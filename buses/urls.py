from django.urls import path

from . import views

app_name = 'buses'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('table', views.TableView.as_view(), name='table')
]
