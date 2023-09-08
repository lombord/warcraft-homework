from django.db import models


class MediaTypeBase(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name


class VideoType(MediaTypeBase):
    pass


class AudioType(MediaTypeBase):
    pass


class Screenshot(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/')


class GameVideo(models.Model):
    video = models.FileField(upload_to='videos/%Y/%m/%d/')
    video_type = models.ForeignKey(
        VideoType, on_delete=models.SET_NULL, null=True,
        related_name='videos')

    def __str__(self):
        return f"{self.video_type}: {self.pk}"


class GameAudio(models.Model):
    audio = models.FileField(upload_to='audios/%Y/%m/%d/')
    audio_type = models.ForeignKey(
        AudioType, on_delete=models.SET_NULL, null=True,
        related_name='audios')
