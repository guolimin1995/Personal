# coding:utf-8
from django import forms
# from Blog.models import UserInfo


class USerInfo(forms.Form):
    user = forms.CharField(label='user', max_length=10)
    password = forms.CharField(label='password', max_length=30)

    def clean_user(self):
        pass
        # username = self.cleaned_data['user']
        # if not UserInfo.objects.filter(account=username).exists():
        #     raise forms.ValidationError('username not aleady exist!!')

    def clean_password(self):
        pass
        # password = self.cleaned_data['password']
        # user_info = UserInfo.objects.get(account='admin')
        # if password != user_info.passwd:
        #     raise forms.ValidationError('password error!')
