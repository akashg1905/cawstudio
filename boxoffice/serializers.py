from rest_framework import serializers

from boxoffice.models import City, Theatre


class CitySerilaizer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name']

class TheatreSerilaizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theatre
        fields =['id','name','city']