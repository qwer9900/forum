from django import forms

class user_form(forms.Form):
    username = forms.CharField(label="用户名",max_length=10)
    password = forms.CharField(label="密码",max_length=10)
    password1 = forms.CharField(label="再次确认密码",max_length=10)
    birthday = forms.DateTimeField(label="生日")
    optionsRadios = forms.IntegerField(label="性别")
    email = forms.CharField(label="邮箱",max_length=40)
