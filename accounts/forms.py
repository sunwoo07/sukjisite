from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '사용자 이름'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='필수. 유효한 이메일 주소를 입력하세요.',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': '사용자 이름'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': '비밀번호 확인'})
