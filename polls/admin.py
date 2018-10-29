from django.contrib import admin
from .models import PollsType, Polls

# Register your models here.

@admin.register(PollsType)
class PollsTypeadmin(admin.ModelAdmin):
    list_display=("id","type_name")
  
@admin.register(Polls)
class pollsadmin(admin.ModelAdmin):
    list_display=("id", "title", "polls_type", "get_read_num", "author", "created_time", "last_updated_time")
    ordering=("-id", )   #排序

