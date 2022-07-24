from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'post_category',
            'title',
            'text',
            'rating',
        ]


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")
        if title == text:
            raise ValidationError(
                "Текст не должен быть идентичен названию."
            )

        return cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['user']