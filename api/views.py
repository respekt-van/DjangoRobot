from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Status
from .serializers import StatusSerializer
# Create your views here.

class StatusView(APIView):
    def get(self, request):
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return Response({"status": serializer.data})

    def post(self, request):
        status = request.data.get('status')
        # Create an article from the above data
        serializer = StatusSerializer(data=status)
        if serializer.is_valid(raise_exception=True):
            status_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(status_saved.status)})

    def put(self, request):
        saved_status = get_object_or_404(Status.objects.all())
        data = request.data.get('status')
        serializer = StatusSerializer(instance=saved_status, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "Status '{}' updated successfully".format(article_saved.status)
        })
