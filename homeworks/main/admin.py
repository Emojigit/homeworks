from django.contrib import admin
from main import models

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('sort_key','short_code','name',)
    ordering = ('sort_key',)

admin.site.register(models.Subject,SubjectAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('subject_name','description','type','create_date','due_date',)
    list_filter = ('subject','type','create_date','due_date',)
    ordering = ('-create_date','-due_date','subject__sort_key','description',)
    list_display_links = ('description',)
    def subject_name(self, obj):
        if obj.subject:
            return obj.subject.short_code
        else:
            return 'OTH'
    subject_name.short_description = "Subject"

admin.site.register(models.Homework,HomeworkAdmin)
