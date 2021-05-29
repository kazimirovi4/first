
from django.urls import path
from django.views.generic import ListView

from main.models import PersonModel
from main.views import ShowPerson, showperson2, SavePerson

app_name = 'main'

urlpatterns = [
    path('2/', ShowPerson.as_view(), name="show_person2"),
    path('1/', showperson2, name='show_person1'),
    path('3/', ListView.as_view(model=PersonModel), name='show_person3'),
    path('4/', SavePerson.as_view()),
]
