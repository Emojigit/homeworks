from django.contrib import admin
from main import models

# Register your models here.

admin.site.register(models.Subject)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('subject','description','type','due_date' )
    list_filter = ('subject','type','due_date' )

admin.site.register(models.Homework,HomeworkAdmin)
