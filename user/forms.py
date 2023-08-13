from django import forms
from .models import User
from argon2 import PasswordHasher, exceptions
import re

class RegisterForm(forms.ModelForm):
    user_name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-name',
                'placeholder' : '이름'
            }
        ),
        error_messages={'required' : '이름을 입력해주세요'}
    )
    user_email = forms.EmailField(
        label='이메일',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'user-email',
                'placeholder' : '이메일'
            }
        ),
        error_messages={'required' : '이메일을 입력해주세요'}
    )
    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요'}
    )
    user_pw_confirm = forms.CharField(
        label='비밀번호 확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw-confirm',
                'placeholder' : '비밀번호 확인'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다'}
    )

    field_order = [
        'user_email',
        'user_name',
        'user_pw',
        'user_pw_confirm'
    ]

    class Meta:
        model = User
        fields = [
            'user_email',
            'user_name',
            'user_pw'
        ]

    def clean(self):
        cleaned_data = super().clean()

        user_email = cleaned_data.get('user_email','')
        user_name = cleaned_data.get('user_name','')
        user_pw = cleaned_data.get('user_pw','')
        user_pw_confirm = cleaned_data.get('user_pw_confirm','')

        if user_pw !=user_pw_confirm:
            return self.add_error('user_pw_confirm','비밀번호가 다릅니다.')
        elif 8 > len(user_pw):
            return self.add_error('user_pw','비밀번호는 8자 이상으로 적어주세요.')
        elif not check_pw(user_pw):
            return self.add_error('user_pw','비밀번호 조합규칙에 맞지 않습니다. 3종 이상 문자로 구성된 8자리 이상 비밀번호를 입력해주세요')
        else:
            self.user_email = user_email
            self.user_name = user_name
            self.user_pw = PasswordHasher().hash(user_pw)
            self.user_pw_confirm = user_pw_confirm

def check_pw(password):
    PT1 = re.compile('^(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d!@#$%^&*]{8,}$') 
    PT2 = re.compile('^(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*]{8,}$')
    PT3 = re.compile('^(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$') 
    PT4 = re.compile('^(?=.*[a-z])(?=.*\d)[A-Za-z\d!@#$%^&*]{8,}$')
    PT5 = re.compile('^(?=.*[a-z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$') 
    PT6 = re.compile('^(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$')
    PT7 = re.compile('^[A-Za-z\d!@#$%^&*]{10,}$')

    for pattern in [PT1,PT2,PT3,PT4,PT5,PT6,PT7]:
        if pattern.match(password):
            return True
        return False

class LoginForm(forms.Form):
    user_email = forms.EmailField(
        max_length=128,
        label='이메일',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'user-email',
                'placeholder' : '이메일'
            }
        ),
        error_messages={'required' : '이메일를 입력해주세요'}
    )
    user_pw = forms.CharField(
        max_length=128,
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder' : '비밀번호'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    field_order = [
        'user_email',
        'user_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        user_email = cleaned_data.get('user_email','')
        user_pw = cleaned_data.get('user_pw','')

        if user_email == '':
            return self.add_error('user_email','이메일을 다시 입력해 주세요')
        elif user_pw == '':
            return self.add_error('user_pw','비밀번호를 다시 입력해 주세요')
        else:
            try:
                user = User.objects.get(user_email=user_email)
            except User.DoesNotExist:
                return self.add_error('user_email', '이메일이 존재하지 않습니다')
            
            try:
                PasswordHasher().verify(user.user_pw, user_pw)
            except exceptions.VerifyMismatchError:
                return self.add_error('user_pw','비밀번호가 다릅니다.')
            
            self.login_session = user.user_email