from django.conf.urls import include, url
from pages import views
urlpatterns = [
    url(r'^get_village/', views.get_names, name='get_names'),
]
