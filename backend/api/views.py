from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser


from .serializer import ImageSerializer, AlbumSerializer
from .models import Image, Album


# Create your views here.

class AlbumsListView(APIView):
      # permission_classes = [IsAuthenticated]
      parser_classes = (MultiPartParser, FormParser)


      def get(self, req, format=None, *args, **kwargs):
            Albums = Album.objects.all()
            serializer = AlbumSerializer(Albums, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

      def post(self, req, *args, **kwargs):
            serializer = AlbumSerializer(data=req.data)

            if serializer.is_valid():
                  uploaded_images = req.FILES.get('cover_image')
                  serializer.save(cover_image=uploaded_images)

                  return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      




class ImagesListView(APIView):
      # permission_classes = [IsAuthenticated]
      parser_classes = (MultiPartParser, FormParser)


      def get(self, req, format=None, *args, **kwargs):
            images = Image.objects.all()
            serializer = ImageSerializer(images, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

      def post(self, req, *args, **kwargs):
            serializer = ImageSerializer(data=req.data)

            if serializer.is_valid():
                  uploaded_images = req.FILES.get('image')
                  serializer.save(image=image)

                  return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:
                  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      




class AlbumDetailAPIView(APIView):

      def get(self,req, id):
            album = Album.objects.filter(pk=id).prefetch_related('images').first()

            if not album:
                  return Response({'detail': 'Album not Found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = AlbumSerializer(album)
            return Response(serializer.data)



class ImageDetailAPIView(APIView):

      def get(self,req, id):
            image = Image.objects.filter(pk=id).prefetch_related('tags').first()

            if not image:
                  return Response({'detail': 'image not Found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = ImageSerializer(image)
            return Response(serializer.data)



class AddImageToAlbumAPIView(APIView):
    def post(self, request, album_id):
        # Retrieve the album instance
        album = Album.objects.filter(id=album_id).first()
        if not album:
            return Response({'error': 'Album not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Create an image serializer instance with the request data
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            # Save the image data to the album instance
            image = serializer.save()
            # Associate the image with the album
            album.images.add(image)
            # Optionally, update album cover image if needed
            if not album.cover_image:
                album.cover_image = image.image
                album.save()
            # Return a success response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return validation errors if serializer is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)