from django import forms
from CRUD.models import crudDB


class CrudForm(forms.ModelForm):
    class Meta:
        model = crudDB
        fields = '__all__'
