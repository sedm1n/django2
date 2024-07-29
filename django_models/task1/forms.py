from django import forms

class UserRegister(forms.Form):
      username = forms.CharField(label="username", max_length=30, required=True)
      password = forms.CharField(label="password", min_length=8 )
      repeat_password = forms.CharField(label="repeat_password", min_length=8)
      age = forms.CharField(label="Age", max_length=3)


    
