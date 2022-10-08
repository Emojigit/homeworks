from django.shortcuts import render
from main import models
import datetime
from django.db.models import Count
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
import pandas as pd

# Create your views here.

def index(request):
    today = datetime.date.today()
    yday  = today - datetime.timedelta(days=1)
    tmr   = today + datetime.timedelta(days=1)
    hwlist = models.Homework.objects.filter(due_date__gt = today).annotate(null_subject=Count('subject')).order_by("-null_subject","subject__sort_key","due_date","description")
    return render(request, "index.html", {**globals(),**locals()})

def subjects(request):
    subjects = models.Subject.objects.all().order_by("sort_key")
    return render(request, "subjects.html", {**globals(),**locals()})

def history(request,year,month,day):
    errmsg = ""
    try:
        today = datetime.date(year,month,day)
        yday  = today - datetime.timedelta(days=1)
        tmr   = today + datetime.timedelta(days=1)
    except OverflowError:
        errmsg = _("The provided integers are too large.")
    except ValueError:
        errmsg = _("The values are obviously out of range.")
    finally:
        if errmsg != "":
            return render(request, "error.html", {**globals(),**locals()},status=400)
    hwlist = models.Homework.objects.filter(create_date__lte = today, due_date__gt = today).annotate(null_subject=Count('subject')).order_by("-null_subject","subject__sort_key")
    return render(request, "index.html", {**globals(),**locals()})

def hist_formredirect(request):
    errmsg = ""
    if request.GET.get("d"):
        try:
            today = datetime.date.fromisoformat(request.GET.get("d"))
        except OverflowError:
            errmsg = _("The provided integers are too large.")
        except ValueError:
            errmsg = _("The values are obviously out of range.")
        finally:
            if errmsg != "":
                return render(request, "error.html", {**globals(),**locals()},status=400)
        return HttpResponseRedirect("/history/" + str(today.year) + "/" + str(today.month) + "/" + str(today.day))
    else:
        errmsg = _("No date given.")
        return render(request, "error.html", {**globals(),**locals()},status=400)
