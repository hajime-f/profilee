from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = get_user_model()
        fields = ['email']
        labels = {'email': 'メールアドレス'}
        help_texts = {'email': ''}


class CustomUserChangeForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = get_user_model()
        fields = ['email', ]
        labels = {
            'email': 'メールアドレス',
        }
        help_texts = {
            'email': '',
        }
