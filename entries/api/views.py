from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from entries.models import Entry
from entries.api.serializers import EntrySerializer


class EntriesListApi(APIView):
    def get(self, request):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = EntrySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = 201)

        return Response(status = 400, data = serializer.errors)


class ModifyEntriesListApi(APIView):
    def get(self, request, pk):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        entry = get_object_or_404(Entry, pk = pk)

        self.check_object_permissions(request, entry)

        serializer = EntrySerializer(instance=entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

class DeleteEntriesListApi(APIView):
    def get(self, request, pk):
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)

        return Response(serializer.data)

    def delete(self, request, pk):
        self.check_permissions(request)

        entry = get_object_or_404(Entry, pk=pk)

        self.check_object_permissions(request, entry)

        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)