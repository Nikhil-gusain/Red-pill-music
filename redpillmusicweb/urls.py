"""
URL configuration for redpillmusicweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_view,logout_view,register_view,home,discover,artist,music,artistpage,join_us_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #logins
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    #pages
    path('',home,name='home'),
    path('discover/',discover,name='discover'),
    path('artist',artist,name='artist'),
    path('music',music,name='music'),
    path('artist/<int:artist_id>',artistpage,name='ArtistrSolo'),
    path('join-us/',join_us_view,name='joinus'),

    #api end points
    path('api/',include('redpillmusicapp.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)