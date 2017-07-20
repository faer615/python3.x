from api import views
from django.conf.urls import url

urlpatterns = [
    url(r'^asset$', views.AssetView.as_view()),
]
