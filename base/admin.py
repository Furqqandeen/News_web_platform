from django.contrib import admin
from base.models import Categories,Articles
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','category','created_at','status','is_treanding']
    prepopulated_fields={'slug':('title',)}


admin.site.register(Categories)
admin.site.register(Articles,ArticleAdmin)