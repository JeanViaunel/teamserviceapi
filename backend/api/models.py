from django.db import models
import os
# Create your models here.



def img_image_upload(instance,filename):
      base_file , file_ext = os.path.splitext(filename)
      new_file_name = f'{instance.title}{file_ext}'
      return f'Images/{new_file_name}'

class Album(models.Model):
      title = models.CharField(max_length=200)
      description = models.TextField(blank=True)
      cover_image = models.ImageField(upload_to=img_image_upload, blank=True, null=True)
      # tags = models.ManyToManyField('Tag', related_name='images', blank=True)
      images = models.ManyToManyField('Image', related_name='albums', blank=True)

      

      def __str__(self):
            return self.title




class Image(models.Model):
      title = models.CharField(max_length=200)
      description = models.TextField(blank=True)
      image = models.ImageField(upload_to=img_image_upload, blank=True, null=True)
      tags = models.ManyToManyField('Tag', related_name='images', blank=True)

      

      def __str__(self):
            return self.title


class Tag(models.Model):
      name = models.CharField(max_length=100)

      def __str__(self):
            return self.name