from django.shortcuts import render

from django.views.generic import (TemplateView, ListView, DetailView)

from .models import *


menu = [
    {'name': 'home', 'label': 'Home'},
    {'name': 'about', 'label': 'About'},
    {'name': 'shots', 'label': 'Shots'},
    {'name': 'videos', 'label': 'Videos'},
    {'name': 'audios', 'label': 'Audios'},
]


class BaseMixin:
    menu = menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = self.get_menu()
        return context

    def get_menu(self):
        return self.menu.copy()


class HomeView(BaseMixin, TemplateView):
    template_name = 'base_app/home.html'
    extra_context = {'title': 'Home'}


class AboutView(BaseMixin, TemplateView):
    template_name = 'base_app/about.html'
    extra_context = {'title': 'About'}


class ShotsView(BaseMixin, ListView):
    model = Screenshot
    template_name = 'base_app/shots.html'
    context_object_name = 'shots'
    extra_context = {'title': 'Screenshots'}


class VideosView(BaseMixin, TemplateView):
    template_name = 'base_app/videos-main.html'
    extra_context = {'title': 'Game Videos'}


class CinematicView(BaseMixin, ListView):
    model = GameVideo
    template_name = 'base_app/videos.html'
    context_object_name = 'videos'
    extra_context = {'title': 'Cinematic Videos'}

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(video_type__name__iexact='cinematic')


class GameplayView(BaseMixin, ListView):
    model = GameVideo
    template_name = 'base_app/videos.html'
    context_object_name = 'videos'
    extra_context = {'title': 'Gameplay Videos'}

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(video_type__name__iexact='gameplay')


class AudiosView(BaseMixin, TemplateView):
    template_name = 'base_app/audios-main.html'
    extra_context = {'title': 'Game Audios'}


class SoundtracksView(BaseMixin, ListView):
    model = GameAudio
    template_name = 'base_app/audios.html'
    context_object_name = 'audios'
    extra_context = {'title': 'Soundtracks'}

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(audio_type__name__iexact='soundtrack')


class QuotesView(BaseMixin, ListView):
    model = GameAudio
    template_name = 'base_app/audios.html'
    context_object_name = 'audios'
    extra_context = {'title': 'Quotes'}

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(audio_type__name__iexact='quote')
