from django.contrib import admin

# Register your models here.
from ghostpost.models import Post
admin.site.register(Post)
from ghostpost.models import Sorter
admin.site.register(Sorter)

