# from django import forms
# from django.contrib.auth import authenticate


# class UserLoginForm(forms.Form):
#     username             = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password             = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


#     def clean(self , *args, **kwargs):
#         username         = self.cleaned_data.get('username')
#         password         = self.cleaned_data.get('password') 

#         if username and password:
#             user = authenticate(username=username,password=password)
#             if not user:
#                 raise forms.ValidationError('Wrong User!')
#             if not user.is_active:
#                 raise forms.ValidationError('Wrong User!')
#         return super(UserLoginForm,self).clean(*args, **kwargs)
       


from django import forms
from django.contrib.auth.models import User
from .models import *



class daildddyscosst(forms.ModelForm):
    class Meta:
        model = post_models
        fields = ['channel_name','channel_slug','catgory','straming_url','channel_logo']
        widgets = {
            'channel_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Channel Name'}),
            'channel_slug':forms.TextInput(attrs={'class':'form-control','placeholder':'slug'}),
            'catgory':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'straming_url':forms.TextInput(attrs={'class':'form-control','placeholder':'20tk....'}),
   


          }


