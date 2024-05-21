from .models import *
from rest_framework import serializers


class PerevalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'status']


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
       fields = ['winter', 'spring', 'summer', 'autumn']


class PerevalImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.URLField()

    class Meta:
       model = PerevalImage
       fields = ['image', 'title', 'pereval', ]


class PerevalAddedSerializer(serializers.Serializer):
    pereval = PerevalSerializer()
    user = TouristSerializer()
    coords = CoordinatesSerializer()
    level = LevelSerializer()
    images = PerevalImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user', 'coords', 'status', 'images',
                  'level']

    def create(self, validated_data, **kwargs):
        user = validated_data.pop('user')
        coords = validated_data.pop('coords')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        user, created = Tourist.objects.get_or_create(**user)

        coords = Coordinates.objects.create(**coords)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords, level=level, status='NW')

        for i in images:
            image = i.pop('image')
            title = i.pop('title')
            PerevalImage.objects.create(image=image, pereval=pereval, title=title)

        return pereval

