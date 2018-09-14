from django.urls import path, include
from .views import index, home

urlpatterns = [
    path('login', index, name='index'),
    # path(r'^login/$', views.login, name='login'),
    # path(r'^logout/$', views.logout, name='logout'),
    path(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    path(r'', home, name='home'),
]
