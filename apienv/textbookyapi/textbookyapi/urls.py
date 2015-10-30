"""textbookyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from rest_framework import routers
from textbookyapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'listings', views.ListingsViewSet)
router.register(r'listingphotos', views.ListingphotosViewSet)
router.register(r'reviews', views.ReviewsViewSet)

# Wire up our API using automatic URL routing.\
urlpatterns = [
    url(r'^', include(router.urls))
]