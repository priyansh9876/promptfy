from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


INPUT_CLASS = """
w-full px-3 py-2
rounded-lg
bg-slate-800
border border-slate-700
text-white
placeholder-slate-400
outline-none
focus:border-cyan-400
focus:ring-1 focus:ring-cyan-400/20
transition
text-xs
"""


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': 'Username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': 'Confirm Password'
        })


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': 'Username'
        })

        self.fields['password'].widget.attrs.update({
            'class': INPUT_CLASS,
            'placeholder': 'Password'
        })