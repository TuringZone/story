from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginAPI.as_view()),
    url(r'^logout/$', views.LogoutAPI.as_view()),
    url(r'^user/$', views.UserAPI.as_view()),
    url(r'^knox/', include('knox.urls')),
]
