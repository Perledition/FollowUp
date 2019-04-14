from rest_framework.serializers import ModelSerializer
from ..models import PostEntry, Comments, Blogger


# List API View
class PostEntrySerializer(ModelSerializer):
    class Meta:
        model = PostEntry
        fields = [
            'username',
            'media_object_id',
            'media_type',
            'caption',
            'like_count',
            'comments_count',
            'media_url',
            'thumbnail_url',
            'permalink',
            'timestamp',
            'engagement',
            'impressions',
            'reach',
            'saved',
        ]


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'related_post',
            'timestamp',
            'text',
            'id_number',
        ]


class BloggerSerializer(ModelSerializer):
    class Meta:
        model = Blogger
        fields = [
            'nickname',
            'active_since',
        ]
