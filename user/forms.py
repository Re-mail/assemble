from django import forms
from .models import Signup
from argon2 import PasswordHasher, exceptions

class RegisterForm(forms.ModelForm):
    person_email = forms.EmailField(
        label = '',
        required = True,
        widget = forms.EmailInput(
            attrs = {
                'class' : 'emailcheckbox'
            }
        ),
        error_messages={'required' : '이메일을 입력해주세요.'}
    )
    person_pw = forms.CharField(
        label = '',
        required = True,
        widget = forms.PasswordInput(
            attrs={
                'class' : 'wpwdbox'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )
    person_pw_confirm = forms.CharField(
        label = '',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'rwpwdbox'
            }
        ),
        error_messages={'required' : '비밀번호가 일치하지 않습니다.'}
    )

    field_order = [
        'person_email',
        '',
        'person_pw',
        'person_pw_confirm'
    ]

    class Meta:
        model = Signup
        fields = [
            'person_email',
            'person_pw'

        ]

    def clean(self):
        cleaned_data = super().clean()

        person_email = cleaned_data.get('person_email','')
        person_pw = cleaned_data.get('person_pw','')
        person_pw_confirm = cleaned_data.get('person_pw_confirm','')

        if person_pw != person_pw_confirm:
            return self.add_error('person_pw_confirm', ' 비밀번호가 다릅니다.')
        elif 8 > len(person_pw):
            return self.add_error('person_pw', '비밀번호는 8자 이상으로 적어주세요.')
        else:
            self.person_email = person_email
            self.person_pw = PasswordHasher().hash(person_pw)
            self.person_pw_confirm = person_pw_confirm

class LoginForm(forms.Form):
    person_email = forms.EmailField(
        max_length=128,
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'emailcheckbox'
            }
        ),
        error_messages={'required' : '이메일를 입력해주세요'}
    )
    person_pw = forms.CharField(
        max_length=128,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'wpwdbox'
            }
        ),
        error_messages={'required' : '비밀번호를 입력해주세요.'}
    )

    field_order = [
        'person_email',
        'person_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        person_email = cleaned_data.get('person_email','')
        person_pw = cleaned_data.get('person_pw','')

        if person_email == '':
            return self.add_error('person_email','이메일을 다시 입력해 주세요')
        elif person_pw == '':
            return self.add_error('person_pw','비밀번호를 다시 입력해 주세요')
        else:
            try:
                user = Signup.objects.get(person_email=person_email)
            except Signup.DoesNotExist:
                return self.add_error('person_email', '이메일이 존재하지 않습니다')
            
            try:
                PasswordHasher().verify(user.person_pw, person_pw)
            except exceptions.VerifyMismatchError:
                return self.add_error('person_pw','비밀번호가 다릅니다.')