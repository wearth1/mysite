from django.contrib import admin
from .models import ReadNum, ReadDetail


@admin.register(ReadNum)
class ReadNumadmin(admin.ModelAdmin):
    list_display=("read_num", "content_object")

@admin.register(ReadDetail)
class ReadDetailadmin(admin.ModelAdmin):
    list_display=("date", "read_num", "content_object")