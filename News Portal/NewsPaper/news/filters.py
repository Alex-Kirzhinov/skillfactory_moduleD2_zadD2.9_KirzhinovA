from django_filters import FilterSet, DateFilter
from .models import Post
from django.forms import DateInput


class PostFilter(FilterSet):
    class Meta:

        model = Post
        fields = {
            'title': ['icontains'],
            'text': ['icontains'],
        }

    time_in = DateFilter(
        lookup_expr='gt',
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )


