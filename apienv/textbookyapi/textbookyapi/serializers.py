# -*- coding: utf-8 -*-
from textbookyapi.models import Listings, Reviews, Users, Listingphotos
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('userid', 'username', 'password', 'phonenum', 'firstname',
            'lastname', 'photodir', 'location', 'transactioncount')


class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reviews
        fields = ('reviewid', 'userid', 'rating', 'body')


class ListingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listings
        fields = ('listingid', 'userid', 'isbn', 'title', 'edition',
            'author', 'price', 'condition', 'comments', 'negotiable', 'postdate',
            'expirationdate', 'longitute', 'latitude')


class ListingphotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listingphotos
        fields = ('listingphotoid', 'listingid', 'photodir')