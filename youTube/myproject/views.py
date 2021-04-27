from youTube.myproject.models import Video
from serializer import VideoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class VideoList(APIView):

    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

