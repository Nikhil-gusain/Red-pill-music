from django.urls import path
from .VIEWS import songviews, artistviews,loginviews,genraviews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    #api logins
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', loginviews.api_register, name='api_register'),
    path('login/', loginviews.custom_login, name='api_login'),

    #artist api end points
    path('create-artist/',artistviews.create_artist,name='addartist'),
    path('update-artist/<int:artist_id>',artistviews.update_artist,name='editartist'),
    path('add-featured-artist',artistviews.add_featured_artist,name='addfeaturedartist'),
    path('delete-artist/<int:artist_id>',artistviews.delete_artist,name='deleteartist'),
    path('get-artist/<int:artist_id>',artistviews.get_artist,name='getartist'),#done
    path('get-all-artist/',artistviews.get_all_artists,name='getallartist'),#done
    path('get-artist-by-genra/<int:genra_id>',artistviews.get_artists_by_genra,name='getartistbygenra'),#done
    path('get-featured-artist',artistviews.get_featured_artist,name='getfeaturedartist'),#done
    path('get-featured-artist-by-genra/<int:genra_id>',artistviews.get_featured_artist_by_genra,name='getfeaturedartistbygenra'),#done
    
    #song api end points
    path('add-featured-song',songviews.add_featured_song,name='addfeaturedsong'),
    path('add-song/',songviews.add_song,name='addsong'),
    path('edit-song/<int:song_id>',songviews.edit_song,name='editsong'),
    path('delete-song/<int:song_id>',songviews.delete_song,name='deletesong'),
    path('get-featured-song',songviews.get_featured_song,name='getfeaturedsong'), #done
    path('get-song/<int:song_id>',songviews.get_song,name='getsong'),#done
    path('get-songs-by-genra/<int:genra_id>',songviews.get_songs_by_genra,name='getsongbygenra'),#done
    path('get-songs-by-artist/<int:artist_id>',songviews.get_songs_by_artist,name='getsongbyartist'),#done

    #genra api end points
    path('get-genra-by-id/<int:genra_id>',genraviews.get_genra_by_id,name='getgenrabyid'),#done
    path('get-genra/',genraviews.get_genras,name='getgenras'),#done
]