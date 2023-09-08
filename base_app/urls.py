from django.urls import include, path

from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('shots/', ShotsView.as_view(), name='shots'),
    path('videos/', include([
        path('', VideosView.as_view(), name='videos'),
        path('cinematic/', CinematicView.as_view(), name='cinematic'),
        path('gameplay/', GameplayView.as_view(), name='gameplay'),
    ])),
    path('audios/', include([
        path('', AudiosView.as_view(), name='audios'),
        path('soundtracks/', SoundtracksView.as_view(), name='soundtracks'),
        path('quotes/', QuotesView.as_view(), name='quotes'),
    ])),
]
