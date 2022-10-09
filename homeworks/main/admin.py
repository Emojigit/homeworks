from django.contrib import admin
from main import models

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('sort_key','short_code','name',)
    ordering = ('sort_key',)

admin.site.register(models.Subject,SubjectAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('subject','description','type','create_date','due_date',)
    list_filter = ('subject','type','create_date','due_date',)
    ordering = ('create_date','due_date','subject__sort_key','description',)

admin.site.register(models.Homework,HomeworkAdmin)
