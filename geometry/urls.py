from django.urls import path
from geometry import views

urlpatterns = [
  path("students/", views.students, name='students'),
  path("contacts/", views.contacts, name='contacts'),
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("a_types/", views.a_types, name="a_types"),
  path("quiz1/", views.quiz1, name="quiz1"),
  path("results/", views.results, name="results"), 
  path("t_types/", views.t_types, name="t_types"),
  path("t_area/", views.t_area, name="t_area"),
  path("contact/", views.contact, name="contact"),
  path("register/", views.register, name="register"),
  path('contact/logmessage/', views.logmessage, name='logmessage'),
  path('register/addrecord/', views.addrecord, name='addrecord'),
  path('students/remove/<int:id>', views.remove, name='remove'),
  path('contacts/delete/<int:id>', views.delete, name='delete'),
]