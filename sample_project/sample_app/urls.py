from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    # path('', views.get_updated_age, name='get_updated_age'),
    path('api/get-updated-age/', views.get_updated_age, name='age'),
]