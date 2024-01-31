from rest_framework import generics
from .models import Dict
from .serializers import DictSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class DictListAPIView(generics.ListCreateAPIView):
    queryset = Dict.objects.all()
    serializer_class = DictSerializer

class DictDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dict.objects.all()
    serializer_class = DictSerializer

class TransTextAPIView(APIView):
    def post(self, request):
        lang = request.data.get('lang', '')
        text = request.data.get('text', '')

        dicts = Dict.objects.filter(lang=lang)
        for dict in dicts:
            text = text.replace(dict.origi, dict.dic)

        return Response({'result': text})