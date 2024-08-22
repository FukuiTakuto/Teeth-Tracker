from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from .models import User,MediaUploadModel

class SignupForm(forms.ModelForm):
    email = forms.EmailField(
        label="メールアドレス",
        error_messages={'required': '10文字以内'}
    )
    password1 = forms.CharField(
        label="パスワード", 
        widget=forms.PasswordInput, 
        help_text="必須項目です"
    )
    password2 = forms.CharField(
        label="確認用パスワード", 
        widget=forms.PasswordInput, 
        help_text="再度入力してください"
    )

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("パスワードが一致しません")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="メールアドレス",max_length=254)
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)


class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaUploadModel
        fields = "__all__"
        
class EventForm(forms.Form):
    start_date = forms.IntegerField(required=True)
    end_date = forms.IntegerField(required=True)
    event_name = forms.CharField(max_length=50, required=True) 

class CalendarForm(forms.Form):
    start_date = forms.IntegerField(required=True)
    end_date = forms.IntegerField(required=True)
    
