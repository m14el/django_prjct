from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Category, News
import re
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=150,
                               help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', max_length=150,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль', max_length=150,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='e-mail', max_length=150,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValueError('Заголовок не должен начинаться с цифр')
        return title

    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={
                'class': 'form-control'})

        }

    # title = forms.CharField(max_length=150, label='Заголовок',
    #                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Текст', required=False,
    #                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    # is_published = forms.BooleanField(label='Публикация', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),label='Категория',
    #                                   empty_label='Выберите категорию',
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
