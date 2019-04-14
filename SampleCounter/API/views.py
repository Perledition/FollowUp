from rest_framework.generics import ListAPIView, CreateAPIView
from ..models import PostEntry, Comments, Blogger
from .serializer import PostEntrySerializer, CommentsSerializer


class PostEntryListView(ListAPIView):
    queryset = PostEntry.objects.all()
    serializer_class = PostEntrySerializer

    def create_new_blogger(self, request):
        if Blogger.objects.filter(nickname=request.POST['username']):
            pass
        else:
            model = Blogger()
            model.nickname = request.POST['username']
            model.save()


class PostEntryCreateView(CreateAPIView):
    queryset = PostEntry.objects.all()
    serializer_class = PostEntrySerializer


class CommentsListView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsCreateView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

