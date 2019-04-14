from django.contrib import admin
from .models import PostEntry, Blogger, Comments

admin.site.register(PostEntry)
admin.site.register(Blogger)
admin.site.register(Comments)
