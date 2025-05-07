from redpillmusicapp.CONTROLLERS.SONGCONTROLLERS.featuredsongcontroller import FeaturedSongController
from redpillmusicapp.CONTROLLERS.SONGCONTROLLERS.songcontrollers import SongController
from redpillmusicapp.CONTROLLERS.ARTISTCONTROLLERS.artistcontroller import ArtistController
from redpillmusicapp.CONTROLLERS.ARTISTCONTROLLERS.featuredartistcontroller import FeaturedArtistController
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from redpillmusicapp.UTILITY.helperfunctions import json_to_dotsi
from redpillmusicapp.MESSAGES.Names import Names

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login/login.html')
def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    
    return render(request, 'login/register.html')




def home(request):
    featuredsongs = get_featured_songs()
    featuredartists= get_featured_artist()
    artists = get_artist()
    data = {
        Names.FEATURED_SONGS:featuredsongs,
        Names.FEATURED_ARTISTS:featuredartists,
        Names.ARTISTS:artists
    }

    return render(request, 'pages/home.html',data)
def discover(request):
    artists = get_artist()
    songs = get_featured_songs()

    data = {
        Names.ARTISTS:artists,
        Names.FEATURED_SONGS:songs
    }
    return render(request, 'pages/discover.html',data)
def artist(request):
    artists = get_artist()
    featuredartist  = get_featured_artist()
    data = {
        Names.ARTISTS:artists,
        Names.FEATURED_ARTISTS:featuredartist
    }
    return render(request, 'pages/artists.html',data)

def music(request):
    return render(request, 'pages/music.html')
def artistpage(request,artist_id):
    return render(request, 'pages/artist-solo.html')

def get_featured_songs():
    songs = None
    songresp = FeaturedSongController().get_featured_song()
    if songresp.code == 200:
        songs = songresp.data
    return songs

def get_featured_artist():
    featuredartists=None
    featartistresp = FeaturedArtistController().get_featured_artists()
    if featartistresp.code == 200:
        featuredartists = featartistresp.data
    return featuredartists

def get_artist():
    artists=None
    artistresp = ArtistController().get_artists()
    # print(artistresp)
    if artistresp.code == 200:
        artists = artistresp.data
    return artists