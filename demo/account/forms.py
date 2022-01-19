from django import forms
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_id', 'u_name', 'u_password', 'email_id','mobile_num','mobile_num')
