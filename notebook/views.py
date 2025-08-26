from django.shortcuts import render
from rest_framework import generics, status
from .models import Notebook
from .serializers import NotebookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class NotebookListView(generics.ListAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class NotebookdeleteView(generics.DestroyAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class NotebookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            notebook = Notebook.objects.get(id=pk)
            serializer = NotebookSerializer(notebook).data
            info = {
                'status': 'All about this notebooks is here',
                'notebook': serializer
            }
            return Response(info, status=status.HTTP_200_OK)
        except:
            return Response({'status : There are problems with your serializer'}, status=status.HTTP_400_BAD_REQUEST)


class NotebookCreateApiView(APIView):
    def post(self, request):
        notebook = request.data
        serializer = NotebookSerializer(data=notebook)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotebookUpdateApiView(APIView):
    def put(self, request, pk):
        notebook = get_object_or_404(Notebook, pk=pk)
        serializer = NotebookSerializer(notebook, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            notebook = Notebook.objects.get(id=pk)
            serializer = NotebookSerializer(notebook, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'status : there is a problem, may be with serializer'}, status=status.HTTP_400_BAD_REQUEST)


class NotebookMixedApiView(APIView):
    def get(self, request, pk):
        try:
            student = Notebook.objects.get(id=pk)
            serializer = NotebookSerializer(student).data

            return Response(status=status.HTTP_200_OK)
        except:
            return Response({'status : There are problems with your serializer'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        notebook = Notebook.objects.get(id=pk)
        notebook.delete()
        return Response({'The notebook deleted successfully'})

    def put(self, request, pk):
        notebook = get_object_or_404(Notebook, pk=pk)
        serializer = NotebookSerializer(notebook, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            notebook = Notebook.objects.get(id=pk)
            serializer = NotebookSerializer(notebook, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'status : there is a problem with serializer'}, status=status.HTTP_400_BAD_REQUEST)























