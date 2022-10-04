from django.db import models
from django.utils.translation import gettext as _
from django_enum import EnumField
import datetime

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50,help_text=_("The name of the subject"))
    short_code = models.CharField(max_length=10,help_text=_("A abbreviation of the subject name"))
    sort_key = models.CharField(max_length=10,help_text=_("A string, usually integers, to help sort the list of homeworks."))
    def __str__(self):
        return _("%(name)s (%(short_code)s)" % {'name': self.name, 'short_code': self.short_code})

class Homework(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, blank=True, null=True,help_text=_("The subject of the homework"))

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

    description = models.CharField(max_length=50,help_text=_("The content of the homework, including instructions from the teacher."))

    class TypeEnum(models.TextChoices): # CSS .hwtype-{key}
        HOMEWORK = 'hw', _("Homeworks")
        NOTIFY   = 'nt', _("Notifications")
        ALERT    = 'al', _("Alert")

    type = EnumField(TypeEnum, default=TypeEnum.HOMEWORK,help_text=_("Type of the homework"))

    due_date = models.DateField(help_text=_("The day students should hand in their homework"))
    create_date = models.DateField(default=datetime.date.today,help_text=_("The day the teacher assigned the homework"))

