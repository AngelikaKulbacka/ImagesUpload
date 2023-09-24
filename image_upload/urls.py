from django.urls import path
from . import views


urlpatterns = [
    path('upload/', views.UploadImageView.as_view(), name='upload-image'),
    path('list-images/', views.ListImageView.as_view(), name='list-images'),
    path('thumbnail/<int:image_id>/<int:width>/<int:height>/', views.GenerateThumbnailView.as_view(), name='generate-thumbnail'),
    path('expiring-link/<int:image_id>/<int:expiration_seconds>/', views.GenerateExpiringLinkView.as_view(), name='generate-expiring-link'),
]