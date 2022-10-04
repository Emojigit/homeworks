from django.contrib import admin
from main import models

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('sort_key','short_code','name' )

admin.site.register(models.Subject,SubjectAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('subject','description','type','create_date','due_date' )
    list_filter = ('subject','type','create_date','due_date' )

admin.site.register(models.Homework,HomeworkAdmin)
