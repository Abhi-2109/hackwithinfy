from rest_framework import serializers

from . import models



class CompileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RequestForAnalysis
        fields = '__all__'


class VideoPlaySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VideoPlayModel
        fields = '__all__'


class PictureSeeSerilizer(serializers.ModelSerializer):

    class Meta:
        model = models.PictureModel