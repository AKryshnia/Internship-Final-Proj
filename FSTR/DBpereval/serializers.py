from .models import *
from rest_framework import serializers


class PerevalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'winter', 'spring',
                  'summer', 'autumn', 'status']


class TouristSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Tourist
       fields = ['email', 'fam', 'name', 'otc', 'phone']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Coordinates
       fields = ['latitude', 'longitude', 'elevation', ]


class LevelSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Level
       fields = ['level', ]


class PerevalImageSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = PerevalImage
       fields = ['data', 'title', 'pereval', ]

