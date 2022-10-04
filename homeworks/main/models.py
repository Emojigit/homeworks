from django.db import models
from django.utils.translation import gettext as _
from django_enum import EnumField
import datetime

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=20)
    short_code = models.CharField(max_length=10)
    sort_key = models.CharField(max_length=10)
    def __str__(self):
        return _("%(name)s (%(short_code)s)" % {'name': self.name, 'short_code': self.short_code})

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def subject_name(self):
        if not self.subject:
            return "Other Subjects"
        return self.subject.name
    @property
    def subject_short(self):
        if not self.subject:
            return "OTH"
        return self.subject.short_code

    description = models.CharField(max_length=50)

    class TypeEnum(models.TextChoices): # CSS .hwtype-{key}
        HOMEWORK = 'hw', _("Homeworks")
        NOTIFY   = 'nt', _("Notifications")
        ALERT    = 'al', _("Alert")

    type = EnumField(TypeEnum, default=TypeEnum.HOMEWORK)

    due_date = models.DateField()
    create_date = models.DateField(default=datetime.date.today)

