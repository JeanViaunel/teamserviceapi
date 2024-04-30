from django.urls import path
from . import views

app_name= 'api'



urlpatterns = [

    path('albums/',views.AlbumsListView.as_view(), name='albums_list' ),
    path('albums/<int:id>/',views.AlbumDetailAPIView.as_view(), name='album_detail' ),
    path('images/',views.ImagesListView.as_view(), name='images_list' ),
    path('images/<int:id>/',views.ImageDetailAPIView.as_view(), name='image_detail' ),
    path('albums/<int:album_id>/add/image/',views.AddImageToAlbumAPIView.as_view(), name='add_image' ),
   
]


# import React, { useState } from 'react';

# const AlbumForm = () => {
#   const [albumTitle, setAlbumTitle] = useState('');
#   const [albumDescription, setAlbumDescription] = useState('');

#   const handleSubmit = (e) => {
#     e.preventDefault();
#     const formData = {
#       albumTitle,
#       albumDescription,
#     };
#     console.log(formData);
#     // You can send formData to your backend API for further processing
#   };

#   return (
#     <form onSubmit={handleSubmit}>
#       <label>
#         Album Title:
#         <input type="text" value={albumTitle} onChange={(e) => setAlbumTitle(e.target.value)} />
#       </label>
#       <br />
#       <label>
#         Album Description:
#         <textarea value={albumDescription} onChange={(e) => setAlbumDescription(e.target.value)} />
#       </label>
#       <br />
#       <button type="submit">Create Album</button>
#     </form>
#   );
# };

# export default AlbumForm;
