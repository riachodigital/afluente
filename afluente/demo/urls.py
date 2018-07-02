from django.urls import path

from afluente.demo import views

app_name = 'demo'
urlpatterns = [
    path('', views.index, name='index'),
]
