from django.conf.urls import url
from bookkeeper import views


urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),
    url(r'^index/', views.IndexView.as_view(), name='index'),
]
