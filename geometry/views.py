from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Students, Contacts

def home(request):
    return render(request, "geometry/home.html")

def about(request):
    return render(request, "geometry/about.html")

def contact(request):
    return render(request, "geometry/contact.html")

def register(request):
    return render(request, "geometry/register.html")

def quiz1(request):
    return render(request, "geometry/quiz1.html")

# def results(request):
#     return render(request, "geometry/results.html")

def results(request):
  template = loader.get_template('geometry/results.html')
  return HttpResponse(template.render({}, request))

def a_types(request):
    return render(request, "geometry/a_types.html")

def t_types(request):
    return render(request, "geometry/t_types.html")

def t_area(request):
    return render(request, "geometry/t_area.html")

def students(request):
  mystudents = Students.objects.all().values()
  template = loader.get_template('geometry/students.html')
  context = {
    'mystudents': mystudents,
  }
  return HttpResponse(template.render(context, request))

def contacts(request):
  mycontacts = Contacts.objects.all().values()
  template = loader.get_template('geometry/contacts.html')
  context = {
    'mycontacts': mycontacts,
  }
  return HttpResponse(template.render(context, request))

def addlog(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render({}, request))

def logmessage(request):
  x = request.POST['firstname']
  y = request.POST['lastname']
  e = request.POST['email']
  t = request.POST['textarea']
  contacts = Contacts(firstname=x, lastname=y, email=e, textarea=t)
  contacts.save()
  return HttpResponseRedirect(reverse('contacts'))

def addreg(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['firstname']
  y = request.POST['lastname']
  e = request.POST['email']
  students = Students(firstname=x, lastname=y, email=e)
  students.save()
  return HttpResponseRedirect(reverse('students'))

def remove(request, id):
  students = Students.objects.get(id=id)
  students.delete()
  return HttpResponseRedirect(reverse('students'))

def delete(request, id):
  contacts = Contacts.objects.get(id=id)
  contacts.delete()
  return HttpResponseRedirect(reverse('contacts'))

