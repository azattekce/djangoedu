from django.contrib import admin

# Register your models here.
from .models import Article

# Register your models here.

#admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date","content","article_image"]
    list_display_links=["author"]
    search_fields=["title"]
    class Meta:
          model:Article

