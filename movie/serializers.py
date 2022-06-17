from .models import Director,Movie,Review
from rest_framework import serializers

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()
class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title'.split()
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class ReviweSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()
class ReviweDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'