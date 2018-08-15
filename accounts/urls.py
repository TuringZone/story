from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewset)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^auth/login/$', views.LoginAPI.as_view()),
    url(r'^auth/user/$', views.UserAPI.as_view()),
    url(r'^auth/', include('knox.urls')),
]
