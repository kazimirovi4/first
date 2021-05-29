from django.forms import ModelForm

from main.models import PersonModel


class PersonForm(ModelForm):
    def save(self, commit=True):
        res = super().save(commit=False)
        res.set_password(self.cleaned_data['password'])
        res.save()
        return res
    class Meta:
        model = PersonModel
        fields = ['first_name', 'last_name', 'password', 'email', 'username']

