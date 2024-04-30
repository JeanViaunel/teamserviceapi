from rest_framework import serializers
from .models import  Album,Image, Tag



class ImageSerializer(serializers.ModelSerializer):
      tags = serializers.SerializerMethodField()
      
      class Meta:
            model = Image
            fields = ['id', 'title','description', 'image','tags' ]


      def get_tags(self, obj):
            tag_indices = obj.tags.all()
            tag_names = [tag.name for tag in tag_indices ]

            return tag_names




class AlbumSerializer(serializers.ModelSerializer):
      images = ImageSerializer(many=True, read_only=True)
      
      class Meta:
            model = Album
            fields = ['id', 'title','description','cover_image', 'images']




# import React, { useState } from 'react';

# const AlbumForm = () => {
#   const [albumTitle, setAlbumTitle] = useState('');
#   const [albumDescription, setAlbumDescription] = useState('');
#   const [coverImage, setCoverImage] = useState(null);

#   const handleTitleChange = (e) => {
#     setAlbumTitle(e.target.value);
#   };

#   const handleDescriptionChange = (e) => {
#     setAlbumDescription(e.target.value);
#   };

#   const handleCoverImageChange = (e) => {
#     setCoverImage(e.target.files[0]);
#   };

#   const handleSubmit = (e) => {
#     e.preventDefault();
#     const formData = new FormData();
#     formData.append('albumTitle', albumTitle);
#     formData.append('albumDescription', albumDescription);
#     formData.append('coverImage', coverImage);
#     console.log(formData);
#     // You can send formData to your backend API for further processing
#   };

#   return (
#     <form onSubmit={handleSubmit}>
#       <label>
#         Album Title:
#         <input type="text" value={albumTitle} onChange={handleTitleChange} />
#       </label>
#       <br />
#       <label>
#         Album Description:
#         <textarea value={albumDescription} onChange={handleDescriptionChange} />
#       </label>
#       <br />
#       <label>
#         Cover Image:
#         <input type="file" accept="image/*" onChange={handleCoverImageChange} />
#       </label>
#       <br />
#       <button type="submit">Create Album</button>
#     </form>
#   );
# };

# export default AlbumForm;
