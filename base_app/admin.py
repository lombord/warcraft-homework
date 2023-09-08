from django.contrib import admin

from .models import *

admin.site.register(Screenshot)
admin.site.register(VideoType)
admin.site.register(AudioType)
admin.site.register(GameVideo)
admin.site.register(GameAudio)
