from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from main.forms import PersonForm
from main.models import PersonModel

def showperson2(request):
    data = PersonModel.objects.all()
    context = {'personmodel_list': data}
    return render(request, 'main/personmodel_list.html', context)

class ShowPerson(generic.ListView):
    def get(self, request, **kwargs):
        data = PersonModel.objects.all()
        form = PersonForm
        context = {'personmodel_list': data, 'form': form}
        return render(request, 'main/personmodel_list.html', context)
    def post(self, request, **kwargs):
        form = PersonForm(request.POST)
        if form.is_valid():
            res = form.save(commit=False)
            res.set_password(form.cleaned_data['password'])
            print(res.password)
            res.save()
        else:
            return render(request, 'main/personmodel_list.html')
        return render(request, 'main/personmodel_list.html', {'otvet': 'Данные сохр'})



class ShowPersonList(generic.ListView):
    template_name = 'main/personmodel_list.html'
    model = PersonModel


class SavePerson(generic.CreateView):
    model = PersonModel
    form_class = PersonForm
    template_name = 'main/personmodel_list.html'
    # fields = ['first_name', 'last_name', 'username', 'password', 'email']
    success_url = reverse_lazy('main:show_person3')
