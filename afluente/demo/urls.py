from django.urls import path

from afluente.demo import views

app_name = 'demo'
urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.new, name='new'),
    path('criar', views.create, name='create'),
]
