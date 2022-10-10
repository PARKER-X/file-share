from distutils.filelist import FileList
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from home.serializers import FileListSerializer
from .serializers import *
from rest_framework.parsers import MultiPartParser

def home(request):
    return render(request, 'home/home.html')

def download(request , uid):
    return render(request , 'home/download.html' , context = {'uid' : uid})

# Create your views here.
class HandleFileUpload(APIView):

    def post(self, request):
        try:
            data = request.data 
            serializer = FileListSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    'message':'files uploaded successfuly'
                })
            return Response({
                'status':400,
                'message':'something wenr wrong',
                'data':serializer.errors
            })

        except Exception as e:
            print(e)

            
        