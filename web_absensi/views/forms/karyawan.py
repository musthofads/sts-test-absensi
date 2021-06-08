from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','username','first_name','last_name','password', 'is_active')
        labels = {
            'email':'Email',
            'first_name':'Nama Depan',
            'last_name':'Nama Belakang',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
