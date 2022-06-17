from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer,DirectorDetailSerializer,\
    MovieSerializer,MovieDetailSerializer,ReviweSerializer,ReviweDetailSerializer
from .models import Director,Movie,Review
from rest_framework import status


@api_view(['GET'])
def director_list_view(request):
    persons = Director.objects.all()
    data = DirectorSerializer(persons,many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_detail_view(request,id):
    try:

        persons = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': "Did not Director"}, status=status.HTTP_404_NOT_FOUND)
    data = DirectorDetailSerializer(persons,many=False).data
    return Response(data=data)




@api_view(['GET'])
def movie_list_view(request):
    persons = Movie.objects.all()
    data = MovieSerializer(persons,many=True).data
    return Response(data=data)

@api_view(['GET'])
def movie_detail_view(request,id):
    try:

        persons = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': "Did not movie "}, status=status.HTTP_404_NOT_FOUND)
    data = MovieDetailSerializer(persons,many=False).data
    return Response(data=data)


@api_view(['GET'])
def review_list_view(request):
    persons = Review.objects.all()
    data = ReviweSerializer(persons,many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_detail_view(request,id):
    try:

        persons = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error':"Did not Review"}, status=status.HTTP_404_NOT_FOUND)
    data = ReviweDetailSerializer(persons,many=False).data
    return Response(data=data)

