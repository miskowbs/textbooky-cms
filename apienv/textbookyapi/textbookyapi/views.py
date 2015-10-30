# -*- coding: utf-8 -*-
from textbookyapi.models import Listings, Reviews, Users, Listingphotos
from rest_framework import viewsets
from textbookyapi.serializers import UsersSerializer, ListingsSerializer, ListingphotosSerializer, ReviewsSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, _get_queryset


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ListingsViewSet(viewsets.ModelViewSet):

    queryset = Listings.objects.all()
    serializer_class = ListingsSerializer


class ListingphotosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Listingphotos.objects.all()
    serializer_class = ListingphotosSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer