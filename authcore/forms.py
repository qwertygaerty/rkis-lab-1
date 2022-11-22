from django import forms
from django.core.files.images import get_image_dimensions
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    avatar = forms.FileField(help_text='Enter avatar', required=True)

    username = forms.CharField(
        help_text='Enter username',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
    )

    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    password = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required=True,
        help_text='Enter Password Again',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(avatar) > (200000 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20000k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar

    class Meta:
        model = CustomUser
        fields = ['avatar', 'username', 'email', 'password', 'password2']


class UpdateForm(forms.ModelForm):
    avatar = forms.FileField(help_text='Enter avatar', required=False, )
    username = forms.CharField(
        required=False,
        help_text='Enter username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
    )

    email = forms.EmailField(
        required=False,
        max_length=100,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100000
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(avatar) > (200000 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20000k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar

    class Meta:
        model = CustomUser
        fields = ['avatar', 'username', 'email', ]


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    password = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
