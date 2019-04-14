from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.PostEntryListView.as_view(), name='list'),
    url(r'^create_entry/$', views.PostEntryCreateView.as_view(), name='create'),
]