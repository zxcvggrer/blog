from django.contrib import admin

# Register your models here.
from .models import Comment

class list_comment(admin.ModelAdmin):
    list_display=['name','created_time','post']
admin.site.register(Comment,list_comment)
