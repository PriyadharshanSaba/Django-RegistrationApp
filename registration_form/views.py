from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from registration_form.forms import Reg_page1 , Bib_form
from registration_form.models import Register
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import csv
from random import randint
from .render import Render
from django.views.generic import View
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.template.loader import render_to_string


@csrf_exempt
def register(request):

    if request.method == "POST":
        form = Reg_page1(request.POST)
        print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))

        if form.is_valid():
            print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return render(request, "registration_form/register.html", {'forms': form , 'success_reg' : "Registration successful!"})
    else:

        form = Reg_page1()

    return render(request, "registration_form/register.html", {'forms': form})


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    #result = StringIO.StringIO()
    result = io.BytesIO()

    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request):
    results = "<h1 style='align:center;'>Hi</h1>"
    return render_to_pdf(
                         'line_chart.html',
                         {
                         'pagesize':'A4',
                         'mylist': results,
                         }
                         )


def bib_update(request):
    if request.method == "POST":
        form = Bib_form(request.POST)


        print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
        if form.is_valid():
            Register.objects.filter(phno=form.data['phno']).filter(emailid=form.data['emailid']).update(bibno=form.data['bibno'])
            return render(request, "registration_form/bibupdate.html", {'forms': form,'success_reg' : "Bib successfully allocated! See you on the race day!"})
    else:
        form = Bib_form()
    return render(request, "registration_form/bibupdate.html", {'forms': form})


def bib_search(request):
    str = "Does not exist"
    if request.method == "GET":
        form = Bib_form(request.GET)


        print(request.GET, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
        if form.is_valid():
            if(Register.objects.filter(phno=form.data['phno']).exists()) :
                return render(request,"registration_form/bib_search.html" , {'obj': Register.objects.filter(phno=form.data['phno']) , 'forms':form })
            else :
                return render(request, "registration_form/bib_search.html" , {'message' :str ,'forms':form})

    else:

        form = Bib_form()

    return render(request, "registration_form/bib_search.html", {'forms': form})


def bib_exists(request):

    return render(request,"registration_form/exists.html" , {'obj': Register.objects.filter(phno=form.data['phno'])})

def details_data(request):

    male_count = Register.objects.filter(gender="m").count()
    female_count = Register.objects.filter(gender="f").count()
    total_count = male_count + female_count
    xs_count = Register.objects.filter(teesize="xs").count()
    s_count = Register.objects.filter(teesize="s").count()
    m_count = Register.objects.filter(teesize="m").count()
    l_count = Register.objects.filter(teesize="l").count()
    xl_count = Register.objects.filter(teesize="xl").count()
    bib_count_null = Register.objects.filter(bibno= 0).count()
    bib_count = total_count - bib_count_null
    b_count = Register.objects.filter(expr="beg").count()
    i_count = Register.objects.filter(expr="inter").count()
    p_count = Register.objects.filter(expr="pro").count()


    return render(request,"line_chart.html" , {'mc' : male_count, 'fc' : female_count, 'xsc' : xs_count, 'sc' : s_count, 'mc' : m_count, 'lc' : l_count, 'xlc' : xl_count, 'reg_c' : total_count,'bib_c' : bib_count, 'begg_count' : b_count , 'inter_count' :i_count, 'pro_count' : p_count})

def bib_edit(request):

    if request.method == "POST":
        form = Bib_form(request.POST)


        print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
        if form.is_valid():
            Register.objects.filter(phno=form.data['phno']).update(phno=form.data['phno'])
            Register.objects.filter(phno=form.data['emailid']).update(phno=form.data['emailid'])
            Register.objects.filter(phno=form.data['username']).update(phno=form.data['username'])
            Register.objects.filter(phno=form.data['bibno']).update(phno=form.data['bibno'])
            return redirect('/register/bib_edit')

    else:

        form = Bib_form()

    return render(request, "registration_form/bib_edit.html", {'forms': form , 'edit_msg' : "Bib successfully edited! See you on the race day!"})

def export(request):
    register_resource = RegisterResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response

def details_pass(request):

    return render(request, "registration_form/check_pass.html", {})
