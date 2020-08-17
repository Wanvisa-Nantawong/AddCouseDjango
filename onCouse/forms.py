from django import  forms
from .models import AddCouse
class AddCouseForm(forms.ModelForm) :
    class Meta :
        model = AddCouse
        fields = ['addCouse_name',
                  'addCouse_ID',
                  'teacher_name',
                  'teacher_Period'
                  ]