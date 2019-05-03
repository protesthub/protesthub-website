from rest_framework import serializers

from main.models import Demo


class searchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Demo
        fields = ("title", "adress", "starting_time", "ending_time", "organizer","description")
