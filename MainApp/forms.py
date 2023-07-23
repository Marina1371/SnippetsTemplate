from django.forms import ModelForm
from MainApp.models import Snippet, Comment
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput
from django.core.exceptions import ValidationError


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'code', 'private']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
    password1 = CharField(label="password", widget=PasswordInput)
    password2 = CharField(label="password confirm", widget=PasswordInput)

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError("Пароли не совпадают")


