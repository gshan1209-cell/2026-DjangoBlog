# pyrefly: ignore [missing-import]
from django.contrib import admin
from article.models import Post

admin.site.register(Post)

# Register your models here.
