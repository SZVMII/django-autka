import django_filters
from samochod.models import Part
from user.models import User

class AutoFilter(django_filters.rest_framework.FilterSet):

    user = django_filters.ModelMultipleChoiceFilter(to_field_name='id', queryset=User.objects.all())

    """def filter_auto(self, queryset, to_field_name, value):
    
        if value:
            return queryset.filter(mark__name__in=value)

        return queryset"""

    class Meta:
        model = Part
        fields = ('id', 'model', 'mark',)
