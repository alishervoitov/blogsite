from django.forms import forms,fields,widgets,models

class LoginForm(forms.Form):
    username = fields.CharField(max_length=255)
    password = fields.CharField(widget=widgets.PasswordInput(),min_length=3)

class RegistrationForm(forms.Form):
    first_name = fields.CharField(max_length=100,min_length=1)
    last_name = fields.CharField(max_length=100, min_length=1)
    username = fields.CharField(max_length=100, min_length=4)
    email = fields.EmailField(max_length=100)
    password = fields.CharField(widget=widgets.PasswordInput(), min_length=3)
    password1 = fields.CharField(widget=widgets.PasswordInput(), min_length=3)