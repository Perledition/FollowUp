from django.db import models
import datetime


class Blogger(models.Model):
    nickname = models.CharField(max_length=100, default='NaN')
    active_since = models.DateField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.nickname


class PostEntry(models.Model):
    username = models.ForeignKey(Blogger, default=1, on_delete=models.CASCADE)
    media_object_id = models.CharField(max_length=18, default='0')
    media_type = models.CharField(max_length=100, default='NaN')
    caption = models.CharField(max_length=2500, default='NaN')
    like_count = models.IntegerField(default=0.0)
    comments_count = models.IntegerField(default=0.0)
    media_url = models.CharField(max_length=250, default='NaN')
    thumbnail_url = models.CharField(max_length=250, default='NaN')
    permalink = models.CharField(max_length=100, default='NaN')
    timestamp = models.DateTimeField(default=datetime.datetime.now, blank=True)
    engagement = models.CharField(max_length=100, default='NaN')
    impressions = models.FloatField(default=0.0)
    reach = models.FloatField(default=0.0)
    saved = models.FloatField(default=0.0)

    def __str__(self):
        return '{}: {}'.format(self.username, str(self.media_object_id))


class Comments(models.Model):
    related_post = models.ForeignKey(PostEntry, default=1, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.datetime.now, blank=True)
    text = models.CharField(max_length=100, default='NaN')
    id_number = models.CharField(max_length=18, default='NaN')

    def __str__(self):
        return 'Comment for: {}'.format(self.related_post)
