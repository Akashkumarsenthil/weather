from rest_framework import serializers

from .models import weatherdata

class weatherdataserializer(serializers.ModelSerializer):

    class Meta:
        model  = weatherdata
        # fields = '__all__'
        fields = (
            'city_name',
            'city_id',
            'latitude',
            'longitude',
            'dt_txt',
            'temp',
            'temp_min',
            'temp_max',
            'pressure',
            'sea_level',
            'grnd_level',
            'humidity',
            'main',
            'description',
            'clouds',
            'wind_speed',
            'wind_degree',
        )
