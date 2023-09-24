from django.http import HttpResponse
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedImage
from .serializers import UploadImageSerializer
from rest_framework.views import APIView
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta
from hashlib import sha256


class UploadImageView(generics.CreateAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListImageView(generics.ListAPIView):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadImageSerializer


class GenerateThumbnailView(APIView):
    def get(self, request, image_id, width, height):
        try:
            image = UploadedImage.objects.get(id=image_id).image
            img = Image.open(image.path)
            img.thumbnail((int(width), int(height)))
            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG')
            return HttpResponse(thumb_io.getvalue(), content_type='image/jpeg')
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GenerateExpiringLinkView(APIView):
    def get(self, request, image_id, expiration_seconds):
        try:
            image = UploadedImage.objects.get(id=image_id).image
            expiration_time = datetime.now() + timedelta(seconds=int(expiration_seconds))
            token_data = f"{image_id}:{expiration_time.isoformat()}"
            token = sha256(token_data.encode()).hexdigest()
            expiring_link = f"http://example.com/image/{image_id}/?token={token}&expires={expiration_time.isoformat()}"
            return Response({'expiring_link': expiring_link})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)